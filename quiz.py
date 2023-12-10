print("welcome to the quiz game!")
asking=input("do you want to play this game? ")
if asking.lower() != "yes":
    quit()
print("okya let's play this game :)")
score=0
answer=input("what does cpu stand for? ")
if answer.lower()=="central processing unit":
    print("hey, you're answer is correct")
    score+=1
else:
    print("sorry, you're answer is wrong")
answer=input("what does gpu stand for? ")
if answer.lower()=="graphical processing unit":
    print("hey, you're answer is correct")
    score+=1
else:
    print("sorry, you're answer is wrong")
answer=input("what does ram stand for? ")
if answer.lower()=="random access memory":
    print("hey, you're answer is correct")
    score+=1
else:
    print("sorry, you're answer is wrong")
answer=input("what does js stand for? ")
if answer.lower()=="javascript":
    print("hey, you're answer is correct")
    score+=1
else:
    print("sorry, you're answer is wrong")
answer=input("what does ror stand for? ")
if answer.lower()=="ruby on rails":
    print("hey, you're answer is correct")
    score+=1
else:
    print("sorry, you're answer is wrong")
print("your have answered "+str(score)+" questions correct out of 5 questions!")
print("you have got "+str((score/5)*100)+" %.")
