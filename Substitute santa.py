#oliver stafferöd.
#substitute santa.


filename = input("filename: ")

print("Wellcome to your substitue santa.")
namn = input("please write your name: ")





with open(filename, "w") as leksaker:
    while True:
        leksaker.write(input("what do you want from santa this year?: "))
        if '#' in leksaker:
            break
