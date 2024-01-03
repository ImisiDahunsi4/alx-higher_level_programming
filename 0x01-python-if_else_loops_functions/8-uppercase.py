def uppercase(str):
    for char in str:
        uppernum = char
        if uppernum >= "a" and uppernum <= "z":
            uppernum = chr(ord(uppernum)- 32)
            print(uppernum, end="")
    print("\n")
