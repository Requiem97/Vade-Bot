import os, psycopg2

conn = None
def connect():
    global conn
    db_url = os.environ['DATABASE_URL']
    try:    
        conn = psycopg2.connect(db_url, sslmode='require')
        print("success")
    except:
        print("unable to connect to db")