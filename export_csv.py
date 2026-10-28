"""Экспорт данных из SQLite в CSV."""
import sqlite3
import csv

def export_to_csv() -> None:
    """Читает данные из БД и сохраняет в users.csv."""
    conn = sqlite3.connect("basic.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    
    with open("users.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "age"])  # Заголовки
        writer.writerows(rows)
    
    print("Данные успешно экспортированы в users.csv")
    conn.close()

if __name__ == "__main__":
    export_to_csv()