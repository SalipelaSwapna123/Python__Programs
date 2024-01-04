num=int(input("Enter num :"))
temp=num
rev=0
sum=0
while(num>0):
 rem=num%10
 sum=sum+rem*rem*rem
 num=num/10
if sum==temp:
  print("Armstrong")
else:
  print("Not a Armstrong")