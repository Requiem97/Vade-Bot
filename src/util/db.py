import os
import psycopg2
import datetime
import src.VadeBot as vade_bot

conn = None
cur = None


def connect():
    global conn, cur
    db_url = os.environ['DATABASE_URL']
    try:
        conn = psycopg2.connect(db_url, sslmode='require')
        cur = conn.cursor()
        print("success")
    except:
        print("unable to connect to db")


def upload_data(user_id, amount, dt):
    global conn, cur
    cur.execute("SELECT fund from bot.daily WHERE user_id = %s;",
                (str(user_id),))
    row = cur.fetchall()
    fund = int(row[0][0])
    fund += amount
    cur.execute("UPDATE bot.daily SET fund = %s, last_used = %s where user_id = %s;",
                (fund, dt, str(user_id),))
    conn.commit()


def has_data(user_id):
    global conn, cur
    cur.execute("SELECT * from bot.daily WHERE user_id = %s;", (str(user_id),))
    return True if cur.fetchone() else False


def create_data(user_id, amount, dt):
    global conn, cur
    cur.execute("INSERT into bot.daily (user_id, fund, last_used) VALUES(%s, %s, %s)", (str(
        user_id), amount, dt,))
    conn.commit()


def can_use(user_id):
    global conn, cur
    cur.execute(
        "SELECT last_used from bot.daily WHERE user_id = %s;", (str(user_id),))
    row = cur.fetchall()
    last_used = row[0][0]
    current = datetime.datetime.now()
    delta = current - last_used
    vade_bot.wait = str(datetime.timedelta(seconds=75600 - delta.seconds))
    delta = current.timestamp() - last_used.timestamp()
    if delta >= 75600:
        return True
    else:
        return False


def get_fund(user_id):
    global conn, cur
    if has_data(user_id):
        cur.execute(
            "SELECT fund from bot.daily WHERE user_id = %s;", (str(user_id),))
        row = cur.fetchall()
        fund = row[0][0]
        vade_bot.fund = str(fund)
        return fund
    else:
        vade_bot.fund = str(0)
        return 0

def create_number(user_id, server_id, number):
    global conn, cur
    cur.execute("INSERT into bot.contact_numbers (user_id, server_id, contact) VALUES(%s, %s, %s)", (str(
        user_id), str(server_id), str(number),))
    conn.commit()

def has_number(user_id, server_id):
    global conn, cur
    cur.execute("SELECT * from bot.contact_numbers WHERE user_id = %s and server_id = %s;", (str(user_id),  str(server_id),))
    return True if cur.fetchone() else False

def get_number(user_id, server_id):
    global conn, cur
    if has_number(user_id ,server_id):
        cur.execute(
            "SELECT contact from bot.contact_numbers WHERE user_id = %s, server_id;", (str(user_id), str(server_id)))
        row = cur.fetchall()
        number = row[0][0]
        return number
    else:
        return "no number"

def update_number(user_id, server_id, number):
    global conn, cur
    if has_number(user_id, server_id):
        cur.execute("UPDATE bot.contact_numbers SET contact = %s where user_id = %s and server_id = %s;",
                (str(number), str(user_id), str(server_id),))
        conn.commit()
    else:
        create_number(user_id, server_id, number)
