def desk_view(page):
    load_visitor_table(vb_table1)
    print("Adding Desk view")
    
    page.views.append(
        ft.View(
            "/visitor_book",
            [
                 ft.AppBar(title=ft.Text("FIMS Management System"), bgcolor=ft.colors.BLUE_900,color='white'),
                 vb_box1,vb_table
            ],
            drawer=navbar,
            padding=10,bgcolor='white',horizontal_alignment='center',scroll=True
        )
    )
    page.update()
    return page.views
