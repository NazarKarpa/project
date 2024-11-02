import sqlite3 as sq
cars = [
    ('AUDI', 12455),
    ('BMV', 124554),
    ('CAPTIVA', 122455),
    ('MERS', 1245),
    ('GAY', 1245225)

]
with sq.connect('saper.db') as con:
    con.row_factory = sq.Row
    cur = con.cursor()
    cur.execute('DROP TABLE cars')
    cur.executescript('''CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER
            ava BLOB    

        );
        CREATE TABLE IF NOT EXISTS cust(name TEXT, tr_int INTEGER, buy INTEGER);
    ''')

    # cur.executemany('INSERT INTO cars VALUES(NULL, ?, ?)', cars)
