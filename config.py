from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from webapp import config
# todo: admin localhost i ostalo stavit u config.py
DATABASE_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/zavrsni'

engine = create_engine(DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
