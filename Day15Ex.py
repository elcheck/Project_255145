import sqlite3
def create_connection(dbpath):
    return sqlite3.connect(dbpath)
def create_artist(conn, artist_name):
    cur = conn.cursor()
    artist_id=cur.execute('select max(artistid) from artists')
    results_list = [row for row in artist_id]
    cur.execute('INSERT INTO artists (Name, ArtistId) VALUES (?,?)',(artist_name,results_list[0][0]+10))

con=create_connection('chinook.db')
create_artist(con, 'Anna Vanna')
con.commit()
con.close()







