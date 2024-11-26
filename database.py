import sqlite3


# データベースに接続する関数
def get_connection_db():
    conn = sqlite3.connect("todo.db")
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_connection_db()
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            due_date DATE NOT NULL,
            status TEXT NOT NULL CHECK(status IN('未着手','進行中','完了')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
"""
    )


# タスク一覧を取得する関数
def get_tasks():
    conn = get_connection_db()
    c = conn.cursor()
    tasks = c.execute("SELECT * FROM tasks").fetchall()  # 全部所得できる
    c.close()
    return tasks


# タスクを追加する関数
def add_tasks(title, content, due_date, status):
    conn = get_connection_db()
    c = conn.cursor()
    c.execute(
        "INSERT INTO tasks (title, content, due_date, status) VALUES (?, ?, ?, ?)",
        (
            title,
            content,
            due_date,
            status,
        ),
    )
    conn.commit()
    c.close()


# タスクの詳細を取得する関数
def show_tasks(id):
    conn = get_connection_db()
    c = conn.cursor()
    task = c.execute("SELECT * FROM tasks WHERE id = ?", (id,)).fetchone()
    c.close()
    return task


# タスクを編集する関数
def edit_task(id, title, content, due_date, status):
    conn = get_connection_db()
    c = conn.cursor()
    c.execute(
        "UPDATE tasks SET title = ?, content = ?, due_date = ?, status = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
        (title, content, due_date, status, id),
    )
    conn.commit()
    c.close()


# タスクを削除する関数
def delete_task(id):
    conn = get_connection_db()
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (id,)).fetchone()
    conn.commit()
    c.close()
