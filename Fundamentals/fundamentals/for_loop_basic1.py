# for i in range(0,151,1):
#     print(i)
# print("^"*50)

# for i in range(5,1001,5):
#     print(i)

# print("^"*50)

# for i in range(1,101,1):
#     if i%10 == 0:
#         print("Coding Dojo")
#     elif i%5 == 0:
#         print("Coding")   
#     else:
#         print(i)



# print("^"*50)
# sum = 0
# for i in range (1,500001,2):
#     sum+=i
# print(sum)

# print("^"*50)
# for i in range (2018,0,-4):
#     print(i)

print("^"*50)
def printmults(lowNum,highNum,mul):
    for i in range(lowNum, highNum+1,mul):
        print(i)


printmults(2,10,3)