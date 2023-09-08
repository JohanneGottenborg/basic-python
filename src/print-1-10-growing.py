
# Print the numbers described in the exercise

# l = list(range(1,11))
# m = []
# for i in l:
#     print(i )
#     #for j in l[0:i]:
#     #    print(j)
#     # print(l[0:i])
    

# for i in range(1,11):
#     print(range(1,i+1))


# x = [1,11] 
# print(x)


l = list(range(1,11))
print(l)

x = "1"
for i in l:
    if i == 1:
        x = "1"
    else:
        x = x + " " + str(i)
    print(x)
    
