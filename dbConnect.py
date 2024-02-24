import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="root",
                     db="bot")
cur = db.cursor()