# LED Lightshow: Morse Code Animation

This code is a very simple light assignment on CircuitPython.

In this assignment, I created an interactive light show. It takes a morse code inputed by the user and translates it into light. 
The user is given a link to a Morse code translator page. In that page they can turn their phrase into morse. They copy the output into the code. And the lightshow begins!

I achieved a very simple interaction between the CircuitPython and the user that I think is fun and easy to use. What I particularly like about my assignment is that it immerses the user into it, that way they are not lost in understanding the code output or trying to understand the story behind the show. The show is simply whatever they want to tell. <3

I chose the colour pink for the LED blinking, simply because I love pink! And, I wanted a colour different than the usual Red, Green, Blue. I refrained from alternating colours, because I believe it beats the purpose of morse by becoming too confusing. 

## My Fav Part:

  ``` 
  #FUNCTION DEFINITION

  #SHORT MORSE IS JUST A DOT, IT LOOKS LIKE THIS "."
  def shortMorse():
      led[0] = (255, 53, 184)
      time.sleep(0.2)
      led[0] = (0, 0, 0)
      time.sleep(0.1)

  #LONG MORSE IS A DASH, AND IT LOOKS LIKE THIS "-"
  def longMorse():
      led[0] = (255, 53, 184)
      time.sleep(0.7)
      led[0] = (0, 0, 0)
      time.sleep(0.1)

  #JUMP MORSE IS A FORWARD FACING SLASH, AND IT LOOKS LIKE THIS "/"
  def jumpMorse():
      led[0] = (0, 0, 0)
      time.sleep(0.7)

  #SPACE MORSE IS SIMPLY A SPACE BETWEEN EACH MORSE SET, AND IT LOOKS LIKE THIS " "
  def spaceMorse():
      led[0] = (0, 0, 0)
      time.sleep(0.3) 
  ```
This part of the code was my favourite because it allowed for all the interactions in the show. Because of defining my functions, I am able to take in user input, allow for flexibility with the phrases inputed, and make the code less time consuming. This little piece of function definition is very time efficient and smart. 

## Difficulties: 

1. I do not know how to turn the Morse code translator page into an active link, the user can click on directly. 
2. I started out the code without defining any functions. It would have been very time consuming and would not be able to take user input. 
3. I had a difficult time finding a way to end the code. After enumerating through the characters. So I appended every character from the string after it was read, then once the string was empty, I prompted the user for a new input. 

## Next Steps:

To take this code further, I think adding sound to match the blinks would make it a lot more understandable and easier to follow. And a better way to avoid links is to create a whole Morse code translator built into the code. That way the user types in their phrase normally. Another thing that would be fun to add is for the user to choose their own desired colour. That way the user gets a lot of personalisation out of the code to truly reflect their intended message.
