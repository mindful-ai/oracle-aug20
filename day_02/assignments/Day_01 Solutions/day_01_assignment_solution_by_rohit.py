string = input("Please enter String : ")

for ch in string:
    if ch not in list1:
        list1.append(ch)
        print(str(ch) + '-->' + str(string.count(ch)))