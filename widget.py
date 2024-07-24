import flet as ft
from main import page
import pymysql
config = {
    'host': 'srv865.hstgr.io',
    'user': 'u441049818_SDP',
    'password': 'Flexwave@193708',
    'database': 'u441049818_SDP',
}

name = ft.TextField(label="Name", hint_text="Enter your name", width=300,  )
father_name = ft.TextField(label="F_Name", hint_text="Enter Father name", width=300,)
clas = ft.TextField(label="Class", width=300,)
btn = ft.ElevatedButton("Login", on_click=lambda _: page.go("/DASHBOARD"))
    
box = ft.Container(
        content=ft.Column(
            [
                name,
                father_name,
                clas,
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

def insert(table):
 conn=pymysql.connect(**config)
 cursor=conn.cursor()
 cursor.execute("SELECT* FROM table")
 data=cursor.fetchall()
 for x in data:
  table.rows.append(
   ft.DataRow(
    ft.DataCell(ft.text(value=x[1])),
    ft.DataCell(ft.text(value=x[2])),
    ft.DataCell(ft.text(value=x[3])),
   )  
  )


table=ft.DataTable(
    columns=[
        ft.DataColumn(ft.Text(value="User Name")),
        ft.DataColumn(ft.Text(value="Email")),
        ft.DataColumn(ft.Text(value="Password")),
    ],
    rows=[]
)
