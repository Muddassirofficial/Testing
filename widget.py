import flet as ft
import pymysql
config = {
    'host': 'srv865.hstgr.io',
    'user': 'u441049818_SDP',
    'password': 'Flexwave@193708',
    'database': 'u441049818_SDP',
}
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
