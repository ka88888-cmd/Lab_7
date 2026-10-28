"""Асинхронный доступ к БД с помощью databases."""
import asyncio
import databases
import sqlalchemy

DATABASE_URL = "sqlite:///async_demo.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

async def async_demo() -> None:
    """Асинхронная запись и чтение."""
    await database.connect()
    
    query = notes.insert().values(text="Асинхронная запись")
    await database.execute(query)
    
    rows = await database.fetch_all(notes.select())
    print(f"Прочитано из БД: {rows[0]['text']}")
    
    await database.disconnect()

if __name__ == "__main__":
    asyncio.run(async_demo())