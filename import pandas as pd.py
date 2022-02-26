import pandas as pd

#Check the Pandas Version
print("Check the pandas version: " + pd.__version__)
   
#Three field name, site, age
nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]
   
#Dictionary
dict = {'name': nme, 'site': st, 'age': ag}
     
df = pd.DataFrame(dict)

print(df.to_string)
 
#Save dataframe
#df.to_csv('site.csv')
print("--------------------------------")
csvOutput = pd.read_csv('D:/Python/site.csv');
print(csvOutput.to_string)
print("--------------------------------")

#Filter the duplicate records by using Pandas
print("************************************")
print("#Filter the duplicate records by using Pandas")
person = {
    "name":['Amy','Mike','Amy','Jeff'],
    "age":[21,40,21,50]
}
dp=pd.DataFrame(person)
# if it's duplicated(), return: True，else: False
print(dp.duplicated())
#If want to delete the duplicate records, use method: drop_duplicates() 
print(dp.drop_duplicates(inplace=True))
print(dp)
print("************************************")

 