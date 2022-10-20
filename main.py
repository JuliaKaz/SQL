import sqlalchemy

db = "postgresql://postgres:VJK-1824-skn@localhost:5432/music"
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

