# # is a tree, . is an open square
f = open("input.txt", "r")
input = []
for i in f:
    j = i.rstrip("\n")
    input.append(j)

print(input)