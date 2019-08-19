from getDBData import dbdata

data = dbdata('ALK','2015/1/1')
df = data.CombinedData()

print(df)