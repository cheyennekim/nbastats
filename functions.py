from sqlalchemy import sql, orm, create_engine
from app import db
engine = create_engine('postgres://xgovjbcwxkflgv:e22a9f7f8bf7b708a04f70dbac7ebbbf131283956d4ee8a1cef7cda576c66ae0@ec2-3-234-169-147.compute-1.amazonaws.com:5432/d8fsuve7dqtlcj')
connection = engine.connect()
metadata = db.MetaData()

def test():
	census = db.Table('offStat', metadata, autoload=True, autoload_with=engine)
	query = db.select([census])
	ResultProxy = connection.execute(query)
	ResultSet = ResultProxy.fetchall()
	print(ResultSet[:3])



