import pandas

#Create a dataframe from scratch
data_dict = {
    "students": ["aa", "bb", "cc"],
    "scores" : [76, 56, 65],
    }
data_f = pandas.DataFrame(data_dict)
#print(data_f)


for (index, row) in data_f.iterrows():
    print (row["students"])
