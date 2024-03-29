import pandas

data = pandas.read_csv("Day25-pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": [ "Gray","Cinnamon", "Black" ],
    "Count": [grey_squirrel_count,red_squirrel_count, black_squirrel_count ]
}

df = pandas.DataFrame(data_dict)
df.to_csv("sqcount.csv")