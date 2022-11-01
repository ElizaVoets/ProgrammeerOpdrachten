stuff = ['c',5645,9393.77,"hello", True, False, "Good morning",88, -90, 777.777, 90,665.33,"F"]
strings = []
ints = []
floats = []
bools = []



for datatype in stuff:
    if type(datatype) is str:
        print("string found")
        strings.append(datatype)
    if type(datatype) is int:
        print("int found")
        ints.append(datatype)
    if type(datatype) is float:
        print("float found")
        floats.append(datatype)
    if type(datatype) is bool:
        print("bool found")
        bools.append(datatype)
    

print(strings)
print(ints)
print(floats)
print(bools)