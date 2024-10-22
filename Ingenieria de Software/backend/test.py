#! /usr/bin/env python
import connection
import json
from psycopg2.extras import RealDictCursor


conn = connection.connection()
cur = conn.cursor(cursor_factory=RealDictCursor)
username = "test"

query = """SELECT * FROM users WHERE username = '{0}'""".format(username)
cur.execute(query)
result = cur.fetchone()
data = result['password']
print(data)
