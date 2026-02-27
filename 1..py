def removeDupeString():
    data = "aaabbcddeee"
    new = []
    for char in data:
        if char not in new:
            new.append(char)

    return "".join(new)

# print(removeDupeString())

def sortList():
    data = ["apple", "kiwi", "banana", "fig"]
    print(sorted(data, key=len))

# sortList
import  re

data = 'abc12xyz34p5'

numbersOnly = re.findall(r"\d+",data)
print(sum(map(int,numbersOnly)))
