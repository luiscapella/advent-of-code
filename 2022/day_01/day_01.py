#!/usr/bin/python3
a = open("day_01.txt").read()
a = [[int(j) for j in i.split("\n") if j] for i in a.split("\n\n")]

for i in len(a):
    
#one line solution
print(max(sum(i) for i in a))

#more readable solution using pandas dataframe
#import pandas as pd
#df = pd.DataFrame(columns=['elf', 'food_item_count', 'calories', 'description'])


