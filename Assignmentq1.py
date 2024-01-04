print("Introduction to Python Programming : Rs 499.00")
print("Python Libraries Cookbook : Rs.855.00")
print("Data Science in Python : Rs. 645.00")
b1=499.00
b2=855.00
b3=645.00
d=250.00
c1,c2,c3=0,0,0
while(True):
        choice=int(input("choose any option : "))
        if choice==1:
               n=int(input("Enter no.of books do you want : "))
               c1=n*b1
               print(" amount : ",c1)        
        elif choice==2:
               n=int(input("Enter no.of books do you want : "))
               c2=n*b2
               print(" amount: ",c2)
        elif choice==3:
               n=int(input("Enter no.of books do you want : "))
               c3=n*b3
               print(" amount : ",c3)
        else:
               print("Please enter a valid option!")
               break
        ch2=input("Enter another choice :")
        if ch2=='n':
               break 
sum=c1+c2+c3
amount=sum+sum*(12/100)+d
print("Total Amount : ",amount)
