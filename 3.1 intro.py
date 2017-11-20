import numpy as np
import pandas as pd

# s = pd.Series([1,None,44,1])
# print(s)
#
# dates = pd.date_range('20160101',periods = 6)
# print(dates)

df = pd.DataFrame(
    np.random.randn(3,4),
    index=["row1","row2","row3"],
    columns=["col1","col2","col3","col4"]
)
# print(df)
# print(df['col1'])
#
# df2 = pd.DataFrame({
#     'col0' : ["(0,0)","(1,0)","(2,0)"],
#     "col1" : "sameValueInCol1",
#     "col2" : pd.Categorical(["(0,2)","(1,2)","(2,2)"])
# })
# print(df2)
# print(df2.iloc)

# print(df["col1"])
# print(df[1,1])
print(df.get_value("row1","col1"))
df.set_value("row1","col1",1)

pass

