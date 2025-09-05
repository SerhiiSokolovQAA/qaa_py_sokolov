import psycopg2
from psycopg2.extras import RealDictCursor

class Database:
    def __init__(self, host, dbname, user, password, port=5432):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.port = port
        self.conn = None
        self.cur = None
        self.connect()

    def connect(self):
        if self.conn is None:
            self.conn = psycopg2.connect(
                host=self.host,
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                port=self.port
            )
            self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            );
        """)
        self.conn.commit()

    def insert_user(self, name, email):
        self.cur.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;",
            (name, email)
        )
        user_id = self.cur.fetchone()["id"]
        self.conn.commit()
        return user_id

    def get_user(self, user_id):
        self.cur.execute(
            "SELECT * FROM users WHERE id = %s;", (user_id,)
        )
        return self.cur.fetchone()

    def update_user(self, user_id, new_name):
        self.cur.execute(
            "UPDATE users SET name = %s WHERE id = %s;",
            (new_name, user_id)
        )
        self.conn.commit()

    def delete_user(self, user_id):
        self.cur.execute(
            "DELETE FROM users WHERE id = %s;", (user_id,)
        )
        self.conn.commit()

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
