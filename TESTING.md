## Testing
The local terminal in Gitpod and the Code Institute, Heroku terminal, was used to test the program and code. 
Throughout the testing of each function, I checked the error messages, tried different approaches how to rewriting or fixing the code. 
To see if the math equations' calculation was correct or not, I had a calculator at hand. 

### Code Validation
The code passed through [PEP8 linter](http://pep8online.com/checkresult). The result confirmed there are no problems with the code.

![PEP8](documentation/testing/pep8.png)

### Browser Compatibility
* Google Chrome
  * The program runs without any issues in the Google Chrome browser

  ![Chrome](documentation/testing/play-game.png)

* Mozilla Firefox
  * The program runs without any issues in the Mozilla Firefox browser

  ![Firefox](documentation/testing/create-firefox.png)

* Microsoft Edge
  * The program runs without any issues in the Microsoft Edge browser

  ![Edge](documentation/testing/about-game2.png)

* Safari
  * The program runs without any issues in the Safari browser

  ![Safari](documentation/testing/safari.png)

### Tested User Stories
#### Menu
To navigate through the menu, the user can choose between the numbers 0 to 3. If the user enters a value that is not the number between 0 to 3, the print statement displays on the screen and asks the user to enter a valid value. 

 ![Input Test1](documentation/testing/menu-input-test.png)

#### Section About the Game
When selected, the first part of an informational text about the game appears in the terminal for the user to read. The user can not go forward with the text if not pressing "Enter". If the user tries another key, it will only show next to the instruction until "Enter" is clicked.
At the bottom of the terminal, the menu appears again for the user to navigate to another section of the program.

![Input Test](documentation/testing/about-game-test1.png)

![Bottom of about](documentation/testing/about-game2.png)

#### Game
The game runs in the flow of the set game rules and the order described in the Existing Features. 
At the first input, choose a number between 1 to 10; if the player tries to enter a value that is not valid, an error message will be printed in the terminal, asking the user to enter a correct input.

* Beginning of the Game

![Number input test1](documentation/testing/number-test5.png)

* During the game

![Number input test2](documentation/testing/number-test1.png)

![Number input test3](documentation/testing/number-test2.png)

![Number input test4](documentation/testing/number-test3.png)

![Number input test5](documentation/testing/number-test4.png)


Depending on the user entering an odd or even number, the terminal will print four colors for the player to choose. 

* Result odd number

![Odd number](documentation/testing/choose-color2.png)

* Result even number

![Even number](documentation/testing/choose-color1.png)


The second input for the player is to choose one of the four colors printed in the terminal. Suppose the player tries to enter a color written differently than presented or enter any other character, number, or special sign. In that case, an error message will be printed in the terminal telling the player to enter a valid input.

![Color test 1](documentation/testing/color-test1.png)

![Color test 2](documentation/testing/color-test2.png)

![Color test 3](documentation/testing/color-test3.png)


Depending on which color the player chooses, a math equation will display in the terminal to answer. The color will always have the same equation, but the numbers in the equation will be different for each new round. A the moment, the numbers will be between 1 to 20, and there will never be a negative result or decimals in the answer.

* Addition

 ![Red1](documentation/testing/red1.png)

 ![Red2](documentation/testing/red2.png)

 ![Blue1](documentation/testing/blue1.png)

 ![Blue2](documentation/testing/blue2.png)

* Subtraction

 ![Green1](documentation/testing/green1.png)

 ![Green2](documentation/testing/green2.png)

 ![Yellow1](documentation/testing/yellow1.png)

 ![Yellow2](documentation/testing/yellow2.png)

* Multiplication

 ![Orange1](documentation/testing/orange1.png)

 ![Orange2](documentation/testing/orange2.png)

 ![Purple1](documentation/testing/purple1.png)

 ![Purple2](documentation/testing/purple2.png)

* Division

 ![Pink1](documentation/testing/pink1.png)

 ![Pink2](documentation/testing/pink2.png)

 ![Brown1](documentation/testing/brown1.png)

 ![Brown2](documentation/testing/brown2.png)


If the player tries to answer the question with a character that is not a number, an error message will display in the terminal, asking the user to insert a valid answer.

![Answer input test](documentation/testing/answer-test1.png)


When the player has answered the question, depending on if the answer is correct or incorrect, a message will display in the terminal, letting the player know if they are correct 

![Correct](documentation/testing/correct-print.png)

or incorrect:

![Incorrect](documentation/testing/wrong-print.png)


If the player answers a question wrong, they will lose on "life" of the 3 given at the start of the game. If they answer the question correctly, the game will go on back to choose a number again. The number of lives will only change if the player answers the question wrong. 
The player will be able to keep track of their lives through a printed message in the terminal.

* Correct answer:

![Correct test 1](documentation/testing/correct-lives1.png)

![Correct test 2](documentation/testing/correct-lives2.png)

![Correct test 3](documentation/testing/correct-lives3.png)

* Incorrect answer:

![Life test 1](documentation/testing/wrong-test1.png)

![Life test 2](documentation/testing/wrong-test2.png)

![Life test 3](documentation/testing/wrong-test3.png)

When the player has answered the questions wrong 3 times, a message will display in the terminal letting the player know that they lost all of their lives and ask the player if they want to play the game again or not. 

![Play again](documentation/testing/play-again.png)

If the player wants to play again or not, they can only go forward with their decision if the input value is "y" for yes or "n" for no. Suppose the player tries to put in another than the valid value, an error message will display in the terminal, telling the player to enter a valid value.

![Input test 1](documentation/testing/again-test1.png)

![Input test 2](documentation/testing/again-test2.png)

If the player decides to play again, the game will be reset and start again with 3 new lives. 

![Back to game](documentation/testing/play-again-game.png)

If the player decides not to play another game, a message will display in the terminal, thanking the player for playing the game and taking them back to the start menu.

![Back to menu](documentation/testing/menu.png)

* Instructions on how the user can create their own paper Loppa
When selected, the flow of the text is going as it should. The user can only move forward if they press Enter. If the user presses another key, then nothing will happen. The user needs to press Enter the whole way to get back to the menu.

![Create own test 1](documentation/testing/create-test.png)

### Unfixed Bugs
* The clear() function does not clear the terminal to the top. Depending on how much the user goes through the program, some of the previous visit sections are still showing.

* When a user put in an invalid value to the input field in the menu, the error message would not show what kind of value the user had supplied. To fix this, I made it only to show that an invalid value had has been used. 
