from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=127)
    menu = models.ForeignKey(Menu, null=True, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        "self", null=True, blank="True", on_delete=models.CASCADE
    )
    path = models.CharField(max_length=100, null=True, blank="True")

    def __str__(self):
        return f"{self.id}-{self.name}-{self.path}"
