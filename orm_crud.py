"""CRUD операции через SQLAlchemy ORM."""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class Student(Base):
    """Модель студента."""
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

engine = create_engine("sqlite:///orm_demo.db")
Base.metadata.create_all(engine)

def crud_operations() -> None:
    """Демонстрация Create, Read, Update, Delete."""
    with Session(engine) as session:
        # Create
        student = Student(name="Алексей")
        session.add(student)
        session.commit()
        print(f"Создан: {student.name}")

        # Read
        all_students = session.query(Student).all()
        print(f"Всего студентов: {len(all_students)}")

        # Update
        student.name = "Алексей Петров"
        session.commit()
        print(f"Обновлён: {student.name}")

        # Delete
        session.delete(student)
        session.commit()
        print("Удалён.")

if __name__ == "__main__":
    crud_operations()