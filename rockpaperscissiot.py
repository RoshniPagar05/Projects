import random
item_list = ['Rock','Paper','Scissor']
user_choice =(input("Enter your move : Rock,Paper,Scissor = "))
comp_choice = random.choice(item_list)

print(f"user choice = {user_choice} and computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("both choose same = ,match Tie")
elif user_choice == "Rock":
    if comp_choice == "paper":
        print("paper cover Rock:Computer Win")
    else:
        print("Rock Smaches Scissor :You Win")
elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("paper cover Rock : You Win")
    else:
        print("scissor cut paper: Computer Win")
elif user_choice == "Scissor":
    if comp_choice =="Paper":
        print("Scissor cuts paer: You Win")
    else:
        print("Rock Smaches Scissor: Computer Win")





