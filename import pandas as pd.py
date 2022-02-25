import pandas as pd

print("Check the pandas version: " + pd.__version__)
   
# 三个字段 name, site, age
nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]
   
# 字典
dict = {'name': nme, 'site': st, 'age': ag}
     
df = pd.DataFrame(dict)

print(df.to_string)
 
# 保存 dataframe
#df.to_csv('site.csv')
print("--------------------------------")
csvOutput = pd.read_csv('D:/Python/site.csv');
print(csvOutput.to_string)
print("--------------------------------")
 