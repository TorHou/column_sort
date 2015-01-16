#!/usr/bin/env python
import pandas as pd

# read input file, separator can be specified with sep attribute
# the created object is a Pandas.DataFrame
table=pd.read_csv('/home/thouwaar/testdata/baseball.csv',)
# sort lexigraphically, can be changed to whatever
sorted_table = table[sorted(table.columns)]
# write without index, seperated by tabs
sorted_table.to_csv('/home/thouwaar/testdata/sortedbb.csv',sep='\t',index=False)




