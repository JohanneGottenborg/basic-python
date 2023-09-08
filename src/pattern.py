
# Print the pattern

print("*"*5)

l = list(range(1,10))
p = ""
for i in l:
    if i <= 5:
        p = "* " * (i-1) + "*"
    else:
        p = "* " * (9-i) + "*"
    print(p)

