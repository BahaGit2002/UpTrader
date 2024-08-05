from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='items'
        )
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE,
        related_name='children'
        )
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        unique_together = ('menu', 'name')

    def __str__(self):
        return self.name

    def get_url(self):
        if self.url:
            return self.url
        return '#'
