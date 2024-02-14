from django import template

from main.models import MenuItem


register = template.Library()


@register.inclusion_tag("menu_inclusion.html", takes_context=True)
def draw_menu(context, menu_name):
    query = """
    (
    WITH RECURSIVE parents AS 
    (
    SELECT main_menuitem.*, 0 AS relative_depth 
    FROM main_menuitem
    INNER JOIN main_menu ON (main_menu.id = main_menuitem.menu_id)
    WHERE main_menuitem.path = %(path)s and main_menu.name = %(name)s
    UNION ALL
    SELECT main_menuitem.*, parents.relative_depth - 1 
    FROM main_menuitem, parents 
    WHERE main_menuitem.id = parents.parent_id
    )
    SELECT id, name, path, relative_depth 
    FROM parents
    )
    UNION
    (
    SELECT main_menuitem.id, main_menuitem.name, main_menuitem.path, 999 
    FROM main_menuitem 
    INNER JOIN main_menuitem T2 ON (main_menuitem.parent_id = T2.id)
    INNER JOIN main_menu ON (main_menu.id = main_menuitem.menu_id)
    WHERE T2.path = %(path)s and main_menu.name = %(name)s
    );"""

    path = context["request"].resolver_match.view_name.split(sep=":")[1]
    menu_local_tree = MenuItem.objects.raw(
        raw_query=query, params={"path": path, "name": menu_name}
    )
    menu_local_tree = list(menu_local_tree)
    menu_local_tree = sorted(menu_local_tree, key=lambda x: x.relative_depth)

    return {"menu_local_tree": menu_local_tree}
