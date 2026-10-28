"""Создание БД SQLite, таблицы и использование параметров запроса."""
import sqlite3

def main() -> None:
    """Создаёт таблицу, вставляет и выбирает данные по параметру."""
    conn = sqlite3.connect("basic.db")
    cur = conn.cursor()
    
    # Задание 1: Создание таблицы
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    
    # Задание 6: Использование параметров запроса (защита от SQL-инъекций)
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Екатерина", 20))
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Иван", 25))
    conn.commit()

    # Выборка с параметром
    cur.execute("SELECT * FROM users WHERE age > ?", (21,))
    print("Пользователи старше 21:", cur.fetchall())
    
    conn.close()

if __name__ == "__main__":
    main()