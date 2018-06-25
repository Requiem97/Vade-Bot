import os, psycopg2, datetime
from src.commands import VadeDeets 

conn = None


def connect():
    global conn
    db_url = os.environ['DATABASE_URL']
    try:
        conn = psycopg2.connect(db_url, sslmode='require')
        print("success")
    except:
        print("unable to connect to db")


def uploadData(userID, amount, dt):
    print("updating data")
    global conn
    cur = conn.cursor()
    cur.execute("SELECT fund from bot.daily WHERE user_id = %s;", (str(userID),))
    row = cur.fetchall()
    fund = int(row[0][0])
    fund += amount
    cur.execute("UPDATE bot.daily SET fund = %s, last_used = %s where user_id = %s;",
                (fund, dt, str(userID),))
    conn.commit()
    print("success")

def hasData(userId):
    print("checking data")
    global conn
    cur = conn.cursor()
    cur.execute("SELECT * from bot.daily WHERE user_id = %s;", (str(userId),))
    print("success")
    return True if cur.fetchone() else False

def createData(userID, amount, dt):
    print("creating data")
    global conn
    cur=conn.cursor()
    cur.execute("INSERT into bot.daily (user_id, fund, last_used) VALUES(%s, %s, %s)", (str(userID), amount, dt,))
    conn.commit()
    print("success")

def canUse(userID):
    print("checking if v!daily is allowed")
    global conn
    cur=conn.cursor()
    cur.execute("SELECT last_used from bot.daily WHERE user_id = %s;", (str(userID),))
    row = cur.fetchall()
    last_used = row[0][0]
    current = datetime.datetime.now()
    delta = current - last_used
    VadeDeets.wait = str(datetime.timedelta(seconds = 75600 - delta.seconds))
    print("success")
    if (delta//3600 >= 21 or delta.days > 0):
        print("Allowed")
        return True
    else:
        print("Not Allowed")
        return False
