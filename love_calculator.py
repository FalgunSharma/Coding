print("WELCOME TO THE LOVE CALCULATOR!")
name1=(input("Enter your name "))
name2=(input("Enter your patner name "))

combined_names= name1+name2
lower_names= combined_names.lower()
t=lower_names.count("t")
r=lower_names.count("r")
u=lower_names.count("u")
e=lower_names.count("e")
first_digit=t+r+u+e 

l=lower_names.count("l")
o=lower_names.count("o")
v=lower_names.count("v")
e=lower_names.count("e")
second_digit=l+o+v+e

score= int(str(first_digit)+ str(second_digit))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go like coke and mentos")
elif (score>=40) and (score<=50):
    print(f"your score is {score},you are alright together")
else:
    print(f"your score is {score}")
