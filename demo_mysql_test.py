import pandas as pd

# mydataset = {
#   'sites': ["Google", "Runoob", "Wiki"],
#   'number': [1, 2, 3]
# }

df = pd.read_csv('address.csv')
print(df.to_string())

# myvar = pd.DataFrame(mydataset)
# print(myvar)