import sqlite3
import sys

#IsMod()函数：freq1,freq2是否有互调关系
#ModList()函数：列出某个频率的全部互调关系组

#IsMod()函数：freq1,freq2是否有互调关系
db = 'modulated3.db'

def IsMod(f1, f2, database):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('SELECT MOD3FREQ FROM MOD3 WHERE ? = FREQ1 AND ? = FREQ2;',(f1, f2))
    print(c.fetchall())
    conn.close()

def ModList(f1, database):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('SELECT FREQ2, MOD3FREQ FROM MOD3 WHERE ? = FREQ1;',(f1, ))
    print('All the modulations of the {0}MHz: '.format(f1))
    print(c.fetchall())

script, freq1, freq2 = sys.argv

IsMod(freq1, freq2, db)
ModList(freq1, db)