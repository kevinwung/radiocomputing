#计算出民航频段（118MHz ~ 136.975MHz）中以25kHz间隔为步进的740个频点的所有
#三阶互调关系组

frequencies = list( 118 + x * 0.025 for x in range(int((136.975 - 118) / 0.025 + 2)))
print(frequencies)

