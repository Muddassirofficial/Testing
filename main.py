import flet as ft
from view import Login
def main(page: ft.Page):
    
    page.theme_mode="dark"     
    name = ft.TextField(label="Name", hint_text="Enter your name", width=300,  )
    father_name = ft.TextField(label="F_Name", hint_text="Enter Father name", width=300,)
    cls = ft.TextField(label="Class", width=300,)
    btn = ft.ElevatedButton("Login", on_click=lambda _:Login(name,father_name,cls))
    a=ft.IconButton(ft.icons.WB_SUNNY_OUTLINED,on_click= lambda _:theme())
    def theme():
                 
         if page.theme_mode=="dark":
              page.theme_mode="light"
              a.icon=ft.icons.DARK_MODE
         elif  page.theme_mode=="light":
               page.theme_mode="dark"
               a.icon=ft.icons.SUNNY
               page.update()
    box = ft.Container(
        content=ft.Column(
            [
                name,
                father_name,
                cls,
                btn
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=20,
        border_radius=10,
        bgcolor=ft.colors.GREY,
        width=350,
        height=300,
        alignment=ft.alignment.center
    )

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Login"), bgcolor="blue",
                              actions=[
                                  a
                              ] 
                              ),
                    ft.Container(
                        content=box,
                        alignment=ft.alignment.center,
                        expand=True
                    ),
                ]
            )
        )
        if page.route == "/DATABASE":
            page.views.append(
                ft.View(
                    "/DATABASE",
                    [
                        ft.AppBar(title=ft.Text("DATABASE"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ]
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)