#计算出民航频段（118MHz ~ 136.975MHz）中以25kHz间隔为步进的740个频点的所有
#三阶互调关系组

import io

#计算出全部民航VHF频点
frequencies = list( 118 + x * 0.025 for x in range(int((136.975 - 118) / 0.025 + 2)))

fileHandle = open('modulated3.txt', 'w')

count = 0
for freq1 in frequencies:
    for freq2 in frequencies:
        if freq1 == freq2:
            continue
        elif freq1 * 2 - freq2 in frequencies:
            freq3 = freq1 * 2 - freq2
            fileHandle.write(f'三阶互调组： {freq1}MHz 与 {freq2}MHz 互调 {freq3}MHz \n')
#            print(f'三阶互调组： {freq1}MHz 与 {freq2}MHz 互调 {freq3}MHz \n')
            count += 1
        elif freq1 * 2 + freq2 in frequencies:
            freq3 = freq1 * 2 + freq2
            fileHandle.write(f'三阶互调组： {freq1}MHz 与 {freq2}MHz 互调 {freq3}MHz \n')
#            print(f'三阶互调组： {freq1}MHz 与 {freq2}MHz 互调 {freq3}MHz \n')
            count += 1

#print('一共有{0}组互调组'.format(count))
fileHandle.write('一共有{0}组互调组'.format(count))

fileHandle.close()

