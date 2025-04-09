def check_number(num):
    if num >= 0:
        return "+ san"
    else:
        return  "- san"
numIn = int(input("san: "))
print(check_number(numIn))