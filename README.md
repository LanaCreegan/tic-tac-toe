# Tic Tac Toe
## Introduction
Created with Python, Tic tac toe is a two player game where each player takes turns using X or an O. These can go horizontally, diagonally or vertically and are displayed on a grid. The first player to get 3 in a row wins

## User Experience
### User story
As a user, I want to:
- Understand how to play the game
- Have a clear idea of where to put an X or an O
- Be able to play the game again or quit

## Features
### Welcome message
A welcome message is displayed, welcoming the user to the game along with a brief explaination of the rules. The user will then be asked if the understand the rules

### Player Names
After the welcome message the user will be asked to enter a name to play with 'X' and again with 'O'

### Game Play
Once names have been entered for Player X and Player O the game begins. The game is displayed on a 3 x 3 grid. A map will be displayed so the user can see what number correlates to which position on the game board. The user must enter a number between 1-9. If the user tries to enter a number that has already been used they will get an error message.

### End Game
When the game has finished a message saying would you like to play again will display. The user can enter 'y' which will restart the game or 'n' which will exit the game

### Future Features
- Give the option if the user wants to go first or second 
- Scoreboard 

## Technologies Used
- Python


## Testing 
### User Stories
As a user, I want to know where to put my symbol:
- This can be done by viewing the map provided 

As a user, I want to be able to see if a spot has already been taken:
- If a spot has already been taken, the user will be shown a message saying that the move is invalid. This will also be displayed if the user enters anyhting other than a number

As a user, I want to be able to play the game again at the end of the game:
- When the user reaches the end of the game they will be shown a message asking them if they want to play again, which the user can input 'y' to play again or 'n' to exit the game

## Fixed Bugs


## Deployment 
To deploy on Heroku:
- Navigate to the Heroku dashboard, select 'New' and then click on 'Create new app'
- Write a name for your app and then select your region
- Then click 'Create app'
- Navigate to the settings tab
- Go down to the config vars section and select 'Reveal Config Vars'
- Add in any relevant config vars, in this case 'PORT' was entered in the key field and '8000' in the value field
- Then go to buildpacks and add Python and click save changes
- Then select node.js and click save changes
- Navigate to the deploy tab
- Underneath the deployment method section select GitHub
- Click on 'Connect to GitHub'
- Search for the repository 

## Clone
The repository can be cloned by following these steps:

- Log into GitHub and go to the GitHub Repository
- Click on the code button on the right above the files list
- Then select HTTPS and copy the URL
- Open Git Bash
- Change the current working to the location you   want the cloned directory to be
- Type git clone and paste the URL from earlier
- Press enter to create the local clone