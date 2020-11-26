from config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from webapp import config
# todo: admin localhost i ostalo stavit u config.py
DATABASE_URI = 'postgres+psycopg2://postgres:' + Config.psql_user + '@' + Config.psql_ip + ':' + Config.psql_port + '/' + Config.psql_db_name

engine = create_engine(DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
