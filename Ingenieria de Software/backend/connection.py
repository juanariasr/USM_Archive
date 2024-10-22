import psycopg2
import time

def connection():
    while True:
        try:
            conn = psycopg2.connect(host="postgres.atlas53.duckdns.org",
                                    database="Proyecto",
                                    user="root",
                                    password="root")
            break

        except Exception as e:
            if e:
                print(e)
            else:
                print("Waiting for postgres to be ready")
                time.sleep(1)

    return conn
