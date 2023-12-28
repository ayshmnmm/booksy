import psycopg2


conn = psycopg2.connect(
    host="dpg-cm4io7vqd2ns73ekh6a0-a.singapore-postgres.render.com",
    database="booksydb",
    user="root",
    password="8GyJIlNQHbtULlJK0T0GYbeBNg2Lh5tI"
)

cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(255), email VARCHAR(255) UNIQUE, username VARCHAR(255) UNIQUE, password VARCHAR(255))")
