# Number Guessing

(Developer: Robin Bosch)

![Mockup Number Guessing](docs/mockup/mockup.png)

[View live site]("https://ci-pp3-number-guessing.herokuapp.com/")

## Table of Contents

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [User Stories](#user-stories)
    4. [User Manual](#user-manual)
3. [Technical Design](#technical-design)
    1. [Flowchart](#flowchart)
    2. [Data Models](#data-models)
4. [Features](#features)
5. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks](#frameworks)
    3. [Tools](#tools)
6. [Validation and Testing](#validation-and-testing)
    1. [Python Validation](#python-validation)
    2. [Testing user stories](#testing-user-stories)
7. [Bugs](#bugs)
8. [Deployment](#deployment)
9. [Credits](#credits)
    1. [Media](#media)
    2. [Code](#code)
    3. [Acknowledgements](#acknowledgements)
10. [License](#license)

## Project Goals

### User Goals

- Play a fun little game
- Be able to change the difficulty
- Being able to login or register
- Winning

### Site Owner Goals

- Offer a fun game
- Make sure that the user understands the rules
- Give the user the possibility to customise their game

## User Experience

### Target Audience

- Everyone who wants to play a little game
- People who want a simple game

### User Requirements and Expectations

### User Stories

As a user I want to:

1. Start a game
2. Know the rules
3. Play as guesser
4. Let the computer guess
5. Know if I won
6. Register myself
7. Login
8. Change my username
9. Set the difficulty
10. Create my own difficulty

### User Manual

## Technical Design

### Flowchart

### Data Models

## Features

## Technologies Used

### Languages

- Python

### Libraries

- [gspread](https://docs.gspread.org/en/latest/) - To manage the spreadsheet
- [google oauth](https://google-auth.readthedocs.io/en/master/) - To connect to the google drive

### Tools

- Git
- GitHub
- Heroku - to deploy the app
- Pycodestyle - for validation
- Diagrams.net - for the flowchart

## Validation and Testing

### Python Validation

### Testing user stories

## Bugs

## Deployment

Heroku:

1. Create an account at Heroku and login.
2. Click the "Create new app" button on your dashboard, add app name and region.
3. Click on the "Create app" button.
4. Click on the "Settings" tab.
5. Under "Config Vars" click "Reveal Config Vars" add your credentials as value with "CREDS" as key.
6. Under "Buildpacks" click "Add buildpack" and then choose "Python" first and click "Save changes"
7. Add a second buildpack "nodejs" and click "Save changes"
8. Go to the "Deploy" tab and choose GitHub as your deployment method
9. Connect your GitHub account
10. Enter your repository name, search for it and click connect when it appears below.
11. In the manual deploy section click "Deploy branch"
12. Optional: You can enable automatic deploys if you want the app to automatically update

You can fork the repository by following these steps:

1. Go to the repository on GitHub  
2. Click on the "Fork" button in the upper right hand corner

You can clone the repository by following these steps:

1. Go to the repository on GitHub
2. Locate the "Code" button above the list of files and click it  
3. Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the "copy" button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone <https://github.com/YOUR-USERNAME/YOUR-REPOSITORY>)  
7. Press Enter to create your local clone.

## Credits

### Media

### Code

### Acknowledgements

## License
