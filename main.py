import flet as ft
from view import (register)

from widget import set_global_page

def route_change(route_event, page):
    route = route_event.route
    print("Route change:", route)
    if route == "/":
        print("Fiirst page")
        register(page)
    
    
    print("Current views:", page.views)
    page.update()

def view_pop(view, page):
    page.views.pop()
    top_view = page.views[-1]
    page.go(top_view.route)

def main(page: ft.Page):
    page.title = "Routes Example"
    set_global_page(page)
    #page.window_width = 370
    page.on_route_change = lambda route: route_change(route, page)
    page.on_view_pop = lambda view: view_pop(view, page)
    page.go(page.route)
    page.theme_mode = 'dark'

ft.app(target=main,view=ft.WEB_BROWSER)
