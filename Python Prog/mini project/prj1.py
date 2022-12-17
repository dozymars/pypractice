# This is a question game

print("Welcome to my question game!!!")
print("Lets start")

score = 0
question_1 = input("Do you want to play this game? ").lower()
if question_1 != "yes":
    print("Bye!")
    quit()
else:
    question_2 = input("What is a cpu? ").lower()
    if question_2 == "central processing unit":
        print("That is correct")
        score+=1
    else: 
        print("That is wrong!")
question_3 = input("what is psu? ").lower()
if question_3 == "power supply unit":
    print("That is correct")
    score+=1
else:
    print("wrong")

question_4 = input("what is ram? ").lower()
if question_4 == "random access memory":
    print("That is correct")
    score+=1
else:
    print("You are wrong")

if score < 3:
    print(f"This is what you scored = {score}. Please try again")
if score == 3:
    print(f"This is what you scored = {score}. CONGRATULATIONS")




    
    