from django.core.management.base import BaseCommand

from menu.models import Menu, MenuItem


class Command(BaseCommand):
    help = 'Create test menus and menu items'

    def handle(self, *args, **kwargs):
        main_menu = Menu.objects.create(name='main_menu')

        home = MenuItem.objects.create(
            name='Home',
            url='/',
            menu=main_menu
        )
        about = MenuItem.objects.create(
            name='About',
            url='/about/',
            menu=main_menu
        )
        services = MenuItem.objects.create(
            name='Services',
            menu=main_menu
        )
        MenuItem.objects.create(
            name='Consulting',
            url='/services/consulting/',
            parent=services,
            menu=main_menu
        )
        MenuItem.objects.create(
            name='Development',
            url='/services/development/',
            parent=services,
            menu=main_menu
        )

        self.stdout.write(
            self.style.SUCCESS(
                'Successfully created test menus and menu items'
                )
            )
