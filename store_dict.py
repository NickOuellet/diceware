import pickle

def store_dict(dictionary, file_path):
    f = open(file_path, "w")
    for line in dictionary:
        f.write(line + ":" + dictionary[line] + "\n")
    f.close

def get_dict(file_name):
    dictionary = dict()
    f = open(file_name, "r")
    for line in f:
        new_line = line.replace("\n", "")
        new_line = new_line.split(":")
        dictionary[new_line[0]] = new_line[1]
    return dictionary
#actual solution using pickling
def save_dict(dictionary, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(dictionary, file)

def retrieve_dict(file_name):
    with open(file_name, 'rb') as file:
        return pickle.load(file)

dictionary = {"a":"1","b":"2", "c":"3", "d": "cheese", "e":"fart"}


# store_dict(dictionary, "Dict_Storage.txt")
# print(get_dict("Dict_storage.txt"))
