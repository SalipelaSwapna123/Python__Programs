print("Introduction to Python Programming : Rs 499.00")
print("Python Libraries Cookbook : Rs.855.00")
print("Data Science in Python : Rs. 645.00")
a=499.00
b=855.00
c=645.00
d=250.00
while(True):
    choice=int(input("choose any option : "))
    if choice==1:
        n=int(input("Enter no.of books do you want : "))
        print("Total amount after including taxes and delivery charges : ",n*a*(12/100)+d )
        if choice==2:
            n=int(input("Enter no.of books do you want : "))
            print("Total amount after including taxes and delivery charges : ",n*b*(12/100)+d )
            if choice==3:
               n=int(input("Enter no.of books do you want : "))
               print("Total amount after including taxes and delivery charges : ",n*c*(12/100)+d )
    else:
        print("Please enter a valid option!")

