from datetime import datetime
import pandas as pd
import numpy as np
df = pd.read_excel('mttrgross.xlsx')

t1 = pd.to_datetime(df['Created Time'], format='%b %d, %Y %H:%M %p')
t2 = pd.to_datetime(df['Completed Time'], format='%b %d, %Y %H:%M %p')

mttr = t2 - t1

print(mttr)
