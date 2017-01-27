import pg

db = pg.DB(host='localhost', user="postgres", passwd="bigboss", dbname='demo')
db.debug = True
query = db.query("select * from album")
result_list = query.namedresult()
db.insert('album', name='another album', artist_id=3)
for result in result_list:
    print "album name is %s artist_id is %d" % (result.name, result.artist_id)
