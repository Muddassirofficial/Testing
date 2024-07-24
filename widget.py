import flet as ft
import pymysql
config = {
    'host': 'srv865.hstgr.io',
    'user': 'u441049818_SDP',
    'password': 'Flexwave@193708',
    'database': 'u441049818_SDP',
}
#login function
def Login(name, father_name, cls, page):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS USERS (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            NAME VARCHAR(256),
            F_NAME VARCHAR(256),
            Class VARCHAR(256)
        )
    """)
    conn.commit()
    cur.execute("""
        INSERT INTO USERS (NAME, F_NAME, Class)
        VALUES (%s, %s, %s)
    """, (name.value, father_name.value, cls.value))
    conn.commit()
    #izza
    cur.execute("SELECT* FROM USERS")
    data=cur.fetchall()
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
    conn.close()
    page.go("/DATABASE")
    page.update()