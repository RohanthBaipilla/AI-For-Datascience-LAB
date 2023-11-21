print ('Hello I am chatty')
print('What is your good name?')
name = input()
print("How are you",name,"?")
dec = input()

print("Do you want sum of two numbers? Y/N")
a = input()
if a=="Y":
    print("Ok!Enter two numbers")
    b = int(input())
    c = int(input())
    print(b+c)
    print("Do you want to continue ? Y/N")
    aa = input()
    if aa=="Y":
        print("Ok!Enter two numbers")
        d = int(input())
        e = int(input())
        print(d+e)
    else:
        print("Ok")
else:
    print("Ok")
