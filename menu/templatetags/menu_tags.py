from django import template
from django.db.models import Prefetch
from menu.models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    try:
        menu = Menu.objects.prefetch_related(
            Prefetch('items', queryset=MenuItem.objects.all())
        ).get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu': None}

    def build_tree(item):
        children = item.children.all()
        for child in children:
            child.active = request.path == child.get_url()
            build_tree(child)
        item.children_list = children

    menu_item = None
    if menu:
        menu_item = menu.items.filter(parent=None)
        for item in menu_item:
            item.active = request.path == item.get_url()
            build_tree(item)

    return {'menu': menu, 'menu_item': menu_item, 'request': request}
