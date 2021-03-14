
# import the pyttsx module inside program
import pyttsx3

# initializing the module
engine = pyttsx3.init()

# .say() function is used to speak the text you have written 
# inside the function
#whatever we write here computer will speak
engine.say("hello Aniket Singh")

# this is used to process and run the program commands
engine.runAndWait()
