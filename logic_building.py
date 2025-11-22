list1 = [0,0,0,0,0,0,0,1]

userinput = int(input("Enter no ")) 
counter = 0

length = len(list1)

for i in range(0, length):
    fposition= i - 1
    lposition= i + 1
    cposition= i
    if fposition >= 0 and lposition < length:
        if list1[fposition] == 0 and list1[lposition] == 0:
            list1[cposition] = 1
            counter += 1

if counter == userinput:
    print("True")
else:
    print("False")
