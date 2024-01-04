num1 = int(input("enter number"))
num2 = int(input("enter number"))
for i in range(1, max(num1, num2)):
    if num1 % i == num2 % i == 0:
        hcf = i
lcm = (num1*num2)//hcf
print("hcf of",num1,"and",num2,"is",hcf)
print("LCM of", num1, "and", num2, "is", lcm)
