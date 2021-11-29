<!-- ![](my logo?)  -->
# TABLE OF CONTENTS
1. [Introduction](#intro)
2. [UX](#ux)<br>
  2.1 [User Story](#user-story)
3. [Features and design](#features-design)<br>
  3.1. [Existing features](#existing-features)<br>
  3.2. [Features left to implement](#left-to-implement)
4. [Technologies](#technologies)<br>
  4.1. [Languages used](#languages)<br>
  4.2. [Frameworks, libraries and programs used](#libraries-and-programs)
5. [Testing](https://github.com/Koko-66/Translate_it/blob/main/TESTING.md)
6. [Deployment](#deployment)
7. [Credits](#credits)

## <a name="intro"></a>Translate it!

![Responsive Mockup]()

Link to the deployed app: 

## <a name="ux"></a>UX


### Functionality design


### <a name="user-story"></a>User Story


## <a name="features-design"></a>Features and Design


### <a name="existing-features"></a>Existing Features


### <a name="left-to-implement"></a>Features Left to Implement



## <a name="technologies"></a>Technologies used
### <a name="languages"></a>Languages
- HTML and CSS (provided in Code Institute's template)
- Python
- 


### <a name="libraries-and-programs"></a>Frameworks, Libraries and Programs used
- __GitPod__: used as a backup code editor
- __Git__: used for version control
- __[Git Hub](https://github.com/)__: used to store project files
- __[Python Tutor](https://pythontutor.com/)__: used to help with debugging
- __darw.io__: to create the data models
- __Balsamiq__: for wireframes
- __Cloudinary__: to store image files
- __PostgreSQL Database__: serving as main database
- __Python Libraries__: 
  - Coverage
- __[Heroku](https://www.heroku.com/)__: used to deploy the live version of the project
- __[Am I Responsive?](http://ami.responsivedesign.is/#)__ site to generate the responsive mockup

## <a name="testing"></a>Testing 
Information about testing is available in a separate file [here]().

## <a name="deployment">Deployment
The program was deployed to Heroku and is accessible here: 


The steps taken to deploy the app: 

1. Updated the contents of the requirements file using the `pip3 freeze > requirements.txt` command in VS Code.
2. Checked the project structure and run the program to ensure everything is working as expected.
3. Created the Translate it! project on Heroku, giving it the name 'translate-it7'     (translate-it was not available).
4. In the Config Vars section of the Settings tab, added the environment variables to set up: 
  - credentials to access the Google Sheet with the database; 
  - port;
  - credentials to access the e-mail account for sending e-mails.
5. Added the python and nodejs buildpacks (in that order).
6. In the Deployment tab:
 - selected GitHub as deployment method,
 - selected Connect,
 - authorised Heroku to access the GitHub account,
 - searched for Translate_it repository and confirmed the connection.
7. First time deployed the app using the manual Deploy Branch button, then enabled automatic deploys.
8. Once the first build finished, tested the app's functionality and resolved encountered issues.
 
## Requirements
The program requires Python 3 or higher. 

## <a name="credits">Credits 
A great thank you to: 
- My mentor, Caleb Mbakwe, for invaluable advice on the best approach to the project, organisation of code, and support throughout the whole project. 
- Stackoverflow, its users and their previous posts for helping me find solutions to problems encountered during development. Specifically Ned Batchelder for his suggestion on how to sort linguists listings according to a specific attribute available [here](https://stackoverflow.com/questions/4010322/sort-a-list-of-class-instances-python#comment4297852_4010333).
- [Python Examples](https://pythonexamples.org/python-split-string-by-regex/) for tips on how to use regex for splitting the content.
- Creators of [W3 schools](https://www.w3schools.com) and [Python official documentation](https://docs.python.org/3/) for tips on the usage of various in-built functions and methods.
- [Geeks for Geeks](https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/) for code for e-mail validation using Regex.
- [Programiz](https://www.programiz.com/python-programming/docstrings) for notes on how to write docstrings for modules and classes.
- Creators of [Heroku documentation](https://devcenter.heroku.com/).

