import pandas as pd
x = [23, 48, 19]
my_first_series = pd.Series(x)
print(my_first_series)

import pandas as pd
data = {
    "students" :['emma', 'john', 'bob'],
    "grades" : [12 , 18 , 17]
}
my_first_dataFrame = pd.DataFrame(data)
print(my_first_dataFrame)
print()
import pandas as pd
data = {
    "students":['Emma', 'John', 'Bob'],
    "grades": [12 ,18 ,17]
}
my_first_df = pd.DataFrame(data)
print(my_first_df['students'])
print()

import pandas as pd
data = {
    "students": ['Emma', 'John', 'Bob'],
    "grades": [12, 18, 17]
}
my_first_df = pd.DataFrame(data, index=["a", "b", "c"])
first_row = my_first_df.loc["a"]
print(first_row)
print()
import pandas as pd
data = {
    "students": ['Emma', 'John', 'Bob'],
    "grades": [12, 18, 17]
}
my_first_df = pd.DataFrame(data, index=["a", "b", "c"])
second_row = my_first_df.iloc[1]
print(second_row)