print("Welcome to Pizza delivery")
size= input("what size of pizza do you want? S,M,L ")
add_pepperoni= input("Do you want Pepperoni? Y or N ")
add_cheese= input("Do you want a extra cheese? Y or N ")
bill=0

if size == "S":
    bill=10
    print(f"Your Bill for small pizza is {bill} RS")
    if add_pepperoni =="Y":
        bill+=10
    if add_cheese=="Y":
        bill+=30    
elif size=="M":
    bill=20
    print(f"Your Bill for medium pizza is {bill} RS")
    if add_pepperoni =="Y":
        bill+=20
    if add_cheese=="Y":
        bill+=30    
elif size=="L":
    bill=30
    print(f"Your Bill for large pizza is {bill} RS")
    if add_pepperoni =="Y":
        bill+=20
    if add_cheese=="Y":
        bill+=30
    
if add_cheese=="Y" and add_pepperoni=="Y":
    print(f"Your total bill with extra cheese and pepperoni is {bill}")
if add_cheese=="Y" and add_pepperoni=="N" :
    print(f"Your total bill with extra cheese and no extra pepperoni is {bill}")
if add_cheese=="N" and add_pepperoni=="Y":
    print(f"Your total bill with extra pepperoni and no extra cheese is {bill}")
       