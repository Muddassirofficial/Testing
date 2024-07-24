# views.py

import flet as ft
from widget import (box)
from time import sleep
#jhdsf

def register(page):
    print("Adding Income view")
    
    page.views.append(
        ft.View(
            "/register",
            [    
                 ft.AppBar(title=ft.Text("FIMS Management System"), bgcolor=ft.colors.BLUE_900,color='white'),
                 ft.Container(height=20),
                 ft.Text(value="Enter Fee Details",color='black',size=18),
                 box
                 
                 
            ],
            #drawer=navbar,
            padding=40,bgcolor='white',horizontal_alignment='center',scroll=True,
        )
    )
    
    page.update()
    return page.views
