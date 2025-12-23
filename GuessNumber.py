import  pyttsx3
from random import randint
random_num=randint(1, 100) 
guesses = 0
guess_num = -1
def speak(text):
    engine = pyttsx3.init()   
    engine.setProperty('rate',150 )
    engine.setProperty('volume', 10.0)
    engine.say(text)
    engine.runAndWait()
    
speak("Hey budy now you can start your game. I'll make you sure that it will be fun for you")
        
speak("Enter your guesses ")

while guess_num != random_num:
    guess_num = int(input( "Enter your guess :"))    
    guesses += 1
    speak(str(guess_num))
    if guess_num > random_num:
        text = "Lower number please \n" 
        print(text)
   
        speak(text)
    elif guess_num < random_num:
        text = "Higher number please \n" 
        print(text)
                             
        speak(text)
                                
print(f"You have guessed the right number {guess_num} in {guesses} guesses ")
speak(f"You have guessed the right number {guess_num} in {guesses} guesses ")
