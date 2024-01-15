import json

try:
    data_file = open("Day30-Exceptions/data.txt", "r")
except(FileNotFoundError):
    data_file = open("Day30-Exceptions/data.txt", "w")
    a_dict = {
        "key1": 1,
        "key2": 2
    }
    data_file.write(json.dumps(a_dict))
else:
    content = data_file.read()
    print(content)
finally:
    data_file.close()
    print("File is closed")