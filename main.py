from sqlalchemy import *
import time
# from dotenv import load_dotenv # целая библиотека чтобы прочитать один файл...
import os
from generator import Generate_data

# load_dotenv()
engine  = create_engine(os.getenv('PG_URL'))


meta = MetaData()
orders = Table(
    'orders', meta,
    Column('id', BigInteger, primary_key=True),
    Column('date_time', TIMESTAMP),
    Column('from_node', ForeignKey('nodes.id')),
    Column('to_node', ForeignKey('nodes.id')),
    Column('distance', Float),
    Column('cost', Integer),
    Column('rating', Integer)
)

with engine.connect() as conn:
    while True:
        date_time, from_node, to_node, dist, cost, rating = Generate_data()

        stmt = insert(orders).values(date_time=date_time, from_node=from_node, to_node=to_node, distance=dist, cost=cost, rating=rating)
        conn.execute(stmt)
        conn.commit()

        time.sleep(2)