import pandas

#data = pandas.read_csv("Day25-pandas/weather_data.csv")

# print(data["temp"])


# print(data.to_dict())

# print(data["temp"].max())

#print(data[data.temp == 12])

#print(data[data.temp == data.temp.max()])


# monday = data[data.day == "Monday"]
# print(monday)
# monday_temp = monday.temp[0]
# print(monday_temp, type(monday_temp))

#Create a dataframe from scratch
data_dict = {
    "students": ["aa", "bb", "cc"],
    "scores" : [76, 56, 65],
    }
data = pandas.DataFrame(data_dict)
print(data)