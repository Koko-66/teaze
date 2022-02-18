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

## <a name="intro">Teaze</a>

![Responsive Mockup]()

Teaze is a web-based application for use as a quiz and self-testing tool for fun and in aid of training. There are two levels of users,Admin user can manage and create quizzes and questions, and in the future would be also able to view and manage user assessments. To gain Admin access the user needs to request it from the site manger. A standard user has access to published quizzes, can take the quiz and view his or her results.

Link to the deployed app: 

## <a name="ux"></a>UX

### <a name="user-story"></a>User Stories 
The application was developed using Agile methodology. User stories are logged in the Git Project and are available to view [here](https://github.com/Koko-66/teaze/projects/1).

## <a name="features-design"></a>Features and Design

The app is designed following the UX design principles, with the user's convenience and intuitive navigation in mind. Visual design is kept simple and clean, prioritising usability and speed. Application features are described in more detail below.

### Models and functional design

The application is composed of quiz, question, option, category, assessment and answer models. The relationships bewtween these are represented in the model available [here]().   
<!-- Add about models and design -->

### <a name="existing-features"></a>Existing Features

#### Sign up and Log in

When first accessing the page, the user is directed to a log in page. If they do not yet have an account, they can follow a link to the Sign up page or can log in, if they already have an account. Sign up and Log in forms are delivered by Allauth django app and are fully validated for correct format, asking for providing the password twice and allowing an option to provide an e-mail address.
<!-- Add information that in order to reset password you need to provide email - if that functionality will be added -->

![screentots of forms and admin site]()

Users are managed via backend django admin, where superadmin can assign users to Admin group with advanced rights. 

![screentots of forms and admin site]()

#### Landing page

After logging in, standard user is redirected to their homepage, where they can see a list of published quizzes available for them to complete. If the quiz has been completed it is marked as such, and the button for taking the quiz is replaced with one taking to the user to a page showing their quiz results.

Admin users are redirected to a dashboard with an overview of quizzes, qustions and categories existing in the application. From here, via an extended menu, they can manage (create, edit and delete) quizzes, questions and categories.

![screenshot]()

#### Navigation

Navigation adjusts depending on whether the user is authenticated and if yes, the type of user. 
Menu for non-authenticated user:
![screenshot]()

Menu for authenticated standard user:
![screenshot]()

Menu for authenticated admin user:
![screenshot]()

#### Taking the quiz / Preview

Standard user can take the quiz from their dashboard. Upon clicking on _Take quiz_ button, the user is redirected to a page with the quiz, featuring the quiz title and the questions.
![screenshot]()

The quiz allows only one answer per question, but not all questions have to be answered to submit answers. On submission of answers, the user is redirected to a page showing their results - total score for the quiz and feedback for each of the questions. These quiz results are available to access later via the links on the homepage. Quiz results are saved as assessment against the user and the user cannot take the same quiz more than once.
![screenshot]()

Admin user has an option to preview how quiz will look like on the standard user's page and can preview and complete the assessment as many times as they wish.
![screenshot]()

#### Quiz creation

In order to create a new quiz, the user needs to be assigned to Admin group. This can be requested from app managers (superusers). Adding quiz is a simple process and can be done either directly from Dashboard or from the Manage quizzes page accessible from the Menu at the top of the page.
![screenshot]()

Clicking the _Add_ button initiates Add quiz form, where the user needs to fill in information for the quiz. The form is validated for required fields and duplicated quiz name. Quiz can only be assigned one category.
![screenshot]()

If the user decides not to save the changes, they can cancel the process at any point by clicking either _Cancel_ button or the X sign in the top right corner of the form.

Clicking Save, redirects the user to a view with quiz details.

##### Uploading images - Cloudinary

The user can upload a feature image to the quiz directly to Cloudinary storage. <!-- later used as background in the take quiz view --> 
<!-- At the time of upload, the images are converted to preset sizes. -->

#### Quiz details view

After creating a quiz, the admin user is redirected to a quiz detail view, where they can see information about the quiz: name, status, category, description, image and quiz questions, if any already exist.
If any questions in the same category as the quiz exist and are not used in another quiz <!-- Change questions models to be many-to-many --> they are listed below the main quiz details and can be added to the quiz by clicking the small __+__ icon. Questions can be as easily removed from the quiz by clicking the __x__ icon in the quiz qustions list. 
Note that this action merely remvoves question from the quiz and does not delete it.

![screenshot]()

The _Edit quiz_ button redirects to editing form, where the user can make tweaks to the quiz details.

![screenshot]()

##### Setting quiz status

A quiz can have two statuses - _Draft_ and _Published_. Until the status is set to _Draft_, quiz will not be visible to the standard user to prevent them from completing quizzes which have not been properly prepared and vetted.
At the time of creating, quiz is set to _Draft_ as detault and can be toggled to _Published_ in the Quiz detail view, once admin user is finished setting up the quiz. 

#### Managing questions

Questions are a building block of the application and as such, have their own model and can be managed as individual items. The question management page can be accessed from the link in the card on the __Home__ page or link in the menu at the top of the page.

In the Qustion management page the admin user sees a list of questions with their basic details <!-- and is able to filter them by category and search by keyword typed in. -->.
![screenshot]()

##### Adding questions

A new question can be added from quiz detail view, in which case the quiz is being automatically set to that of the quiz viewed, or from manage questions view, where the question can be created without selecting a quiz and added to a quiz when needed.

Adding question from quiz ![screenshot]
Adding question from ![screenshot]

A question can be assigned more than one category <!--and can be used in more than one question. --> by holding down `Ctrl` button (or `Cmd` on a Mac) and making a selection.

Once the user is happy with the details for the qustion and click `Save`, they are redirected to a question detail page, which is also an editing view.

##### Editing questions and managing options

The user can edit qustion elements individually, which open in modals, and can add and delete options as required.
![Screenshot]
Because options are not part of a question model, but have model of their own, the number of options per qustions is not pre-set and can be set individually per question. 
<!-- The applicatoin prompts the user if they are trying to add an answer option with the same text that already exists.  -->

##### Option uniqueness checks
At prsent, the application design allows for only one option to be set as correct and once one option is set as correct, the tick box for setting an option as correct is not available.
![Screenshot]

##### Accessibility and alerts

Each button that does not contain text has a `title` tag which on hover provides information about the button's function. Each action is also confirmed by an alert, which is dismissed automatically after 3 seconds if the uer does not dissmiss it.

### <a name="left-to-implement"></a>Features Left to Implement

#### User managment of their own account

In the future, the user will have access to a page allowing them to manage their account and 

#### Display quiz qustions one per page

#### Assessment management for Admin user

#### Filtering and searching in questions

## <a name="technologies"></a>Technologies used
### <a name="languages"></a>Languages

Programming languages used in the project: 

- HTML and CSS3
- Python
- JavaScript

### <a name="libraries-and-programs"></a>Frameworks, Libraries, Plugins and other services used
- __Django__: main application framework
- __Bootstrap__
- __GitPod__: primary code editor
- __Git__:  for version control
- __[Git Hub](https://github.com/)__: to store project files
- __[Python Tutor](https://pythontutor.com/)__: used to help with debugging
- __darw.io__: to create the data models
- __Balsamiq__: for wireframes
- __Cloudinary__: to store image files uploaded by the user
- __PostgreSQL Database__: serving as main database
- __Coverage__: create reporting on level of tests
- __AllAuth__: user management
- __django-bootstrap-modal-forms__: to display forms in modals

- __[Heroku](https://www.heroku.com/)__: used to deploy the live version of the project
- __[Am I Responsive?](http://ami.responsivedesign.is/#)__ site to generate the responsive mockup

## <a name="testing"></a>Testing 
Information about testing is available in a separate file [here]().

## <a name="deployment">Deployment</a>
The program was deployed to Heroku at the start of the project to ensure it's correct functioning and is accessible here: 

The steps taken to deploy the app: 

1. Updated the contents of the requirements file using the `pip3 freeze > requirements.txt` command in VS Code.
2. Checked the project structure and run the program to ensure everything is working as expected.
3. Created the Tease project on Heroku, giving it the name 'teaze'.
4. Added a new Postgres database:
  - In the Resources tab, searched for Heroku Postgres add-in and selected free Hobby Dev option.
5. In the Config Vars section of the Settings tab, added the environment variables to set up: 
  - Link to Postgres database 
  - Link to Cloudinary
  - Disabled static files for the time of development
  - App sectret key
5. In the Deployment tab:
 - selected GitHub as deployment method,
 - selected Connect,
 - authorised Heroku to access the GitHub account,
 - searched for 'teaze' repository and confirmed the connection.
6. First time deployed the app using the manual Deploy Branch button, then enabled automatic deploys.
7. Once the first build finished, changed the setting to deploy automatically. 
8. When finished development, enabled static files.
 
## Requirements
All requirements are contained in the requirements.txt file.

## <a name="credits">Credits</a>
A great thank you to: 
- My mentor, Caleb Mbakwe, for invaluable advice on the best approach to the project, organisation of code, and support throughout the whole project. 
- Stackoverflow: for pointing in the right direction on arranging question and option models
- https://stackoverflow.com/questions/54048741/nonetype-object-has-no-attribute-is-ajax: for solving issue of pulling author from logged user rather than having to set it in the form.
<!-- - Izen Oku: for his [blog post](https://medium.com/swlh/overview-building-a-full-stack-quiz-app-with-django-and-react-57fd07449e2f) on creating a Quiz app:  -->
- https://www.youtube.com/watch?v=vXXfXRf2S4M
- Creators of [Heroku documentation](https://devcenter.heroku.com/).

