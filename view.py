import pymysql
#login function
def Login(name, father_name, cls, page):
    conn = pymysql.connect(
        host='srv865.hstgr.io',
        user='u441049818_SDP',
        password='Flexwave@193708',
        database='u441049818_SDP'
    )
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
    conn.close()
    page.go("/DATABASE")
    page.update()
