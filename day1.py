# q: count the number of times a depth measurement increases from the previous measurement

import pandas as pd

# text file can be read from read csv
# col name has to be passed otherwise the first value is taken as default

data_1 = pd.read_csv("input1.txt", names=['depth'])
data_1['prev']=data_1['depth'].shift(1)

# remove the first row as it has no baseline to measure if
# its important to reassign the drop
data_1 = data_1.drop(0)
data_1['increase'] = data_1['depth']>data_1['prev']

# TRUE is consider 1 and FALSE as 0, so just summing up will give total increases.
print(data_1['increase'].sum())
