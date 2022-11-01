stuff = ['c',5645,9393.77,"hello", True, False, "Good morning",88, -90, 777.777, 90,665.33,"F"]
strings = []
integers = []
floats = []
booleans = []

while len(stuff) != 0:
    if type(stuff[0]) is str:
        print("string found")
        strings.append(stuff.pop(0))
        continue
    if type(stuff[0]) is int:
        print("Integer found")
        integers.append(stuff.pop(0))
        continue
    if type(stuff[0]) is float:
        print("Float found")
        floats.append(stuff.pop(0))
        continue
    if type(stuff[0]) is bool:
        print("Boolean found")
        booleans.append(stuff.pop(0))
        continue

while len(stuff) == 0:
    print(strings)
    print(integers)
    print(floats)
    print(booleans)
    break