import sqlite3
import sys

#IsMod()函数：freq1,freq2是否有互调关系
#ModList()函数：列出某个频率的全部互调关系组

#IsMod()函数：freq1,freq2是否有互调关系
def IsMod(f1, f2):
    conn = sqlite3.connect(modulated3.db)
    c = conn.cursor()
    c.execute('SELECT FREQ1, FREQ2 FROM MOD3 WHERE ? = FREQ1 AND ? = FREQ2;',(f1, f2))
    print(c.fetchall())
    c.close()

script, freq1, freq2 = sys.argv

IsMod(freq1, freq2)