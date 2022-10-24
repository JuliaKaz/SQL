import sqlalchemy

db = "postgresql://postgres:пароль@localhost:5432/music"
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

