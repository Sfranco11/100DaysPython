print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

combinedNames = name1.lower() + name2.lower()

true_count = sum(combinedNames.count(char) for char in "true" ) 
love_count = sum(combinedNames.count(char) for char in "love")

love_score = int(str(true_count) + str(love_count))

if (love_score <10 or love_score>90):
    print(f"Your score is {love_score} you go together like coke and mentos.")
elif(love_score >40 and  love_score < 50):
    print(f"Your score is {love_score} you are alright together.")
else:
    print(f"Your score is {love_score}")