print("Welcome to the simple Quiz Game!")
player = input("What is your player name: ")
print("Welcome " + player)
playing = input("Type 'Yes' to continue or 'No' to quit: ")

def check_score(score):
    check_the_score = print("Total score is " + str(score))
        
def startgame():
     #quiz 1
     score = 0   
     print("Quiz 1: What is the full meaning of OOP?")
     
     answer = input("Type your answer: ")
     if answer.lower() == "oop":
        print("True!")
        score += 1
        check_score(score)
     else:
         print("False!")
         score -= 1
         check_score(score)
     #quiz 2
     print("Quiz 2: What is the full meaning of JVM?")
     answer = input("Type your answer: ")
     if answer.lower() == "java":
        print("True!")
        score += 1
        check_score(score)
     else:
         print("False!")
         score -= 1
         check_score(score)

if playing.lower() == "yes":
       startgame()

else:
    quit()



