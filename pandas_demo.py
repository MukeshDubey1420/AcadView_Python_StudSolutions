#Don't forget to run these
# pip install pandas (Python 2.x)
# pip3 install pandas (Python 3.x)

# Series
#   Basic example
# import the pandas library and aliasing as pd
# import pandas as pd
# s = pd.Series()
# print(s)            # Series([], dtype: float64)

#   Series using ndarray
#import the pandas library and aliasing as pd
# import pandas as pd
# import numpy as np
# data = np.array(['a','b','c','d'])
# print(data)
# s = pd.Series(data)
# print(s[0])

#   Series using dict
# #import the pandas library and aliasing as pd
# import pandas as pd
#
# data = {'a' : 0., 'b' : 1., 'c' : 2.}
# s = pd.Series(data)
# print(s)


# Reading CSV
# import pandas as pd
#
# df=pd.read_csv('EventSample.csv')
# print(type(df))         # <class 'pandas.core.frame.DataFrame'>
#
# df=pd.read_csv('EventSample.csv',header=None)
# print(df)

#Creating Dataframe from dict of ndarrays/lists

import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
df.loc[4]=['Lala',24]
print(df)            #     Name  Age
                    # 0    Tom   28
                    # 1   Jack   34
                    # 2  Steve   29
                    # 3  Ricky   42
                    # 4   Lala   24



#Change indexes from default
# import pandas as pd
# data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
# df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
# print(df)

#Dataframes basics

# import pandas as pd
#
# #Create dictionary fo series
# d={'Name':pd.Series(['Tom','James','Ricky','Vin']),
#    'Age':pd.Series([25,26,27,28]),
#    'Ratings':pd.Series([4.23,3.52,2.2,1.5])
# }
# #Create Dataframe
# df= pd.DataFrame(d)
# print(df)
# #Tranpose
# print(df.T)
# #Axes - returns row and column axis labels
# print(df.axes)
# #dtypes
# print(df.dtypes)
# #shape
# print(df.shape)
# #value
# print(df.values)
# #head- returns top n rows
# print(df.head(2))
# #tail- returns last n rows
# print(df.tail(2))

