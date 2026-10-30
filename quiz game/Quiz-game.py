# Project= Quiz Game
# Author= Princy Sharma
# updated on= 24 August 2026 

Questions =[
     "What is 2+2?",
     "Who is known as the God of Cricket?",
     "Name the highest grossing movie in the World?",
     "Which Nation has won the most fifa world cup?",
     "Which programming language are we learning?"
]

Answers =[
    "4",
    "Sachin Tendulkar",
    "Avatar",
    "Brazil",
    "Python"
]
while True:
  i=0
  n=len(Questions)
  score=0

  while(i<n):
    print(Questions[i])
    user_answer = input("Enter your Answer:", )
    if(user_answer==Answers[i]):
        print("Answer is correct")
        score+=1
    else:
        print("Answer is wrong")
    i+=1


  print("Your score is: ",score)
  if(score==5):
    print("Excellent")
  elif(5>score>=3):
    print("Great Job")
  else:
    print("keep trying")

  print("Do You Wanna Play Again")
  user_choice=input("YES/NO",  )
  if(user_choice=="NO"):
   break