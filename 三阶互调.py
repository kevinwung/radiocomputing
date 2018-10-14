#coding:utf-8
#计算出民航频段（118MHz ~ 136.975MHz）中以25kHz间隔为步进的740个频点的所有
#三阶互调关系组
#保存f1/f2/f3到modulated3.db数据库中

import io
import sqlite3

#计算出全部民航VHF频点
frequencies = list( 118 + x * 0.025 for x in range(int((136.975 - 118) / 0.025 + 2)))

fileHandle = open('modulated3.txt', 'w')

#count是三阶互调组的计数器
count = 0
#ID计数
i = 0

#在modulated3.db数据库中创建表MOD3
conn = sqlite3.connect('modulated3.db')
print('Open database successfully.')
c = conn.cursor()
c.execute('''CREATE TABLE MOD3
            (ID INT PRIMARY KEY    NOT NULL,
            FREQ1           REAL   NOT NULL,
            FREQ2           REAL   NOT NULL,
            MOD3FREQ        REAL   NOT NULL);''')
print('table created successfully.')

#两重循环，寻找符合2f1-f2=f3，其中f1/f2/f3属于frequencies
#输出三阶互调组到文件modulated3.txt
#保存f1/f2/f3到modulated3.db数据库中
for freq1 in frequencies:
    for freq2 in frequencies:
        if freq1 == freq2:
            continue
        elif freq1 * 2 - freq2 in frequencies:
            i += 1
            freq3 = freq1 * 2 - freq2
            fileHandle.write(f'三阶互调组： {freq1}MHz 与 {freq2}MHz 互调 {freq3}MHz \n')
#            print(f'三阶互调组： {freq1}MHz 与 {freq2}MHz 互调 {freq3}MHz \n')
            c.execute(f'INSERT INTO MOD3 (ID, FREQ1, FREQ2, MOD3FREQ)\
                VALUES({i}, {freq1}, {freq2}, {freq3});')
            count += 1
#        elif freq1 * 2 + freq2 in frequencies:
#            freq3 = freq1 * 2 + freq2
#            fileHandle.write(f'三阶互调组： {freq1}MHz 与 {freq2}MHz 互调 {freq3}MHz \n')
#            print(f'三阶互调组： {freq1}MHz 与 {freq2}MHz 互调 {freq3}MHz \n')
#            count += 1

#print('一共有{0}组互调组'.format(count))
fileHandle.write('一共有{0}组互调组'.format(count))

conn.commit()
print('Record created successfully.')
conn.close()
fileHandle.close()

