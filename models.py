import sqlite3

# Database connection function
def connect_db():
    conn = sqlite3.connect('tasks.db')
    return conn

# Task Model
class Task:
    def __init__(self, id=None, title=None, description=None, status=None):
        self.id = id
        self.title = title
        self.description = description
        self.status = status

    # Create tasks table
    @staticmethod
    def init_table():
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    # Add a new task to the database
    def save(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tasks (title, description, status)
            VALUES (?, ?, ?)
        ''', (self.title, self.description, self.status))
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()
        return self

    # Get all tasks from the database
    @staticmethod
    def get_all():
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
        conn.close()

        return [Task(id=row[0], title=row[1], description=row[2], status=row[3]) for row in tasks]

    # Get a task by ID
    @staticmethod
    def get_by_id(task_id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return Task(id=row[0], title=row[1], description=row[2], status=row[3])
        else:
            return None

    # Update a task in the database
    def update(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE tasks SET title = ?, description = ?, status = ?
            WHERE id = ?
        ''', (self.title, self.description, self.status, self.id))
        conn.commit()
        conn.close()

    # Delete a task from the database
    @staticmethod
    def delete(task_id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        conn.close()

# Placeholder for User Model
class User:
    def __init__(self, id=None, username=None, email=None, password=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    # Add methods here for user functionality: init_table, save, get_by_id, etc.

    @staticmethod
    def init_table():
        # Initialize the user table (empty for now)
        pass
