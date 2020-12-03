f = open("input.txt","r")
input = f.readlines()
f.close()


def findbad1(input):
    total_count = 0
    for i in input:
        ranges, x, password = i.split()
        key = x.rstrip(":")
        b, e = ranges.split("-")
        counts = 0
        for letter in password:
            if letter == key:
                counts = counts + 1
        if (counts >= int(b)) and (counts <= int(e)):
            total_count = total_count + 1
    return total_count


def findbad2(input):
    total_count = 0
    for i in input:
        ranges, x, password = i.split()
        key = x.rstrip(":")
        b, e = ranges.split("-")
        b = int(b)-1
        e = int(e)-1
        counts = 0
        if password[b] == key:
            counts = counts + 1
        if password[e] == key:
            counts = counts + 1
        if counts == 1:
            total_count = total_count + 1
    return total_count


print(findbad2(input))
