import os
import psycopg2
import datetime
from src.commands import VadeDeets

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


def uploadData(userID, amount, dt):
    global conn, cur
    cur.execute("SELECT fund from bot.daily WHERE user_id = %s;",
                (str(userID),))
    row = cur.fetchall()
    fund = int(row[0][0])
    fund += amount
    cur.execute("UPDATE bot.daily SET fund = %s, last_used = %s where user_id = %s;",
                (fund, dt, str(userID),))
    conn.commit()


def hasData(userId):
    global conn, cur
    cur.execute("SELECT * from bot.daily WHERE user_id = %s;", (str(userId),))
    return True if cur.fetchone() else False


def createData(userID, amount, dt):
    global conn, cur
    cur.execute("INSERT into bot.daily (user_id, fund, last_used) VALUES(%s, %s, %s)", (str(
        userID), amount, dt,))
    conn.commit()


def canUse(userID):
    global conn, cur
    cur.execute(
        "SELECT last_used from bot.daily WHERE user_id = %s;", (str(userID),))
    row = cur.fetchall()
    last_used = row[0][0]
    current = datetime.datetime.now()
    delta = current - last_used
    VadeDeets.wait = str(datetime.timedelta(seconds=75600 - delta.seconds))
    delta = current.timestamp() - last_used.timestamp()
    if delta >= 75600:
        return True
    else:
        return False


def getFund(userID):
    global conn, cur
    if hasData(userID):
        cur.execute(
            "SELECT fund from bot.daily WHERE user_id = %s;", (str(userID),))
        row = cur.fetchall()
        fund = row[0][0]
        VadeDeets.fund = str(fund)
        return fund
    else:
        VadeDeets.fund = str(0)
        return 0
