f = open("input1.txt","r")
nums = []

for i in f:
    j = i.rstrip("\n")
    nums.append(j)

f.close()


def solve1(nums):
    print("Solving for two entries...")
    for k, val in enumerate(nums):
        value = int(val)
        if value >= 2020:
            continue
        for w, val2 in enumerate(nums, k+1):
            value2 = int(val2)
            if value+value2 == 2020:
                print("Value 1:", val, "Value 2:", val2)
                mul = value*value2
                return mul


def solve2(nums):
    print("Solving for three entries...")
    for x, val in enumerate(nums):
        value = int(val)
        if value >= 2020:
            continue
        for z, val2 in enumerate(nums, x+1):
            value2 = int(val2)
            for y, val3 in enumerate(nums, z+1):
                value3= int(val3)
                if value+value2+value3 == 2020:
                    print("Value 1:", val, "Value 2:", val2, "Value 3:", val3)
                    mul = value * value2 * value3
                    return mul


print(solve1(nums))
print(solve2(nums))
