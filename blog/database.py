from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

sqlalchemy_database_url = 'postgresql+psycopg2://postgres:1104@127.0.0.1:5432/blog'

engine = create_engine(sqlalchemy_database_url)


Sessionlocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


Base = declarative_base()


def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
