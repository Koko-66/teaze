<!-- ![](my logo?)  -->
# TABLE OF CONTENTS
1. [Introduction](#intro)
2. [UX](#ux)<br>
  2.1 [User Stories](#user-story)
3. [Features and design](#features-design)<br>
  3.1. [Existing features](#existing-features)
  3.2. [Features left to implement](#left-to-implement)<br>
4. [Management via Django admin](#django-admin)
5. [Technologies](#technologies)<br>
  5.1. [Languages used](#languages)<br>
  5.2. [Frameworks, libraries and programs used](#libraries-and-programs)
6. [Testing](#errors-testing)
7. [Deployment](#deployment)
8. [Credits](#credits)


# <a name="intro"></a>Teaze

![Responsive Mockup]()

Teaze is a web-based application build for use as an internal self-testing tool in aid of training as well as for use in more fun team building activities. In the future, it's use might be extended to external users as a marketing tool aiming at increasing the engagement of the existing and potential customers and encouraging them up for the company's newsletter.

At present, the application is at Stage 1 of development and the focus of the development efforts has been placed on achieving a functioning Minimum Viable Product (MVP) which allows the users to take and create quizzes. Further improvements to the application UI and functionality will be ventured after main stakeholders' input and testing.

Link to the deployed app: https://teaze.herokuapp.com/accounts/login/


# <a name="ux"></a>UX

The initial user interface design idea was captured in the wireframes available [here](https://github.com/Koko-66/teaze/blob/main/data/teaze_wireframes.pdf), while the flow of the application logic in a diagram available for viewing [here](https://github.com/Koko-66/teaze/blob/main/static/data/Teaze_algorithm.pdf).
The design is driven by the user's needs and ease of use. It aims to replicate the process the user would usually go through when creating a quiz, but also offer flexibility by providing access to various features from different places in the application and at different stages of creating or managing a quiz (e.g. editing questions or adding and removing their options).
With user experience in mind, the design of the application is kept simple with primary focus placed on functionality. 


## <a name="user-story"></a>User Stories 

The application was developed using Agile methodology, with User Stories managed within a Github Project. All completed and outstanding User Stories can be viewed [here](https://github.com/Koko-66/teaze/projects/1).


# <a name="features-design"></a>Features and Design

## Models and functional design

The application uses Postgres relationship database to store its data and the data model is comprised of `Quiz`, `Question`, `Option`, `Category`, `Assessment` and `Answer`. The components of each model and the relationships between them are represented in a graphic model representation available [here](https://github.com/Koko-66/teaze/blob/main/static/data/teaze_data_model.pdf).

The decision to keep `Quiz`, `Question` and `Options` as separate models was driven by flexibility. This kind of approach allows maximum flexibility when creating quizzes and questions, as the user is not restricted to a pre-set structure, number of questions per quiz, options per question etc. It also allows for the questions to be reused even if the quiz has been deleted, as they are not inherently a part of the quiz either.

This approach, however, calls for careful consideration of the relationships between various models and what should happen if instances of these are deleted while related to an instance of another model. These considerations are still pending in Teaze app, and need to be addressed.

At present, the relationship between quiz and question is One-to-Many, though it would, arguably, be more beneficial to the user to be able to use the same question in more than one quiz. The deletion of questions, options and categories also poses a problem due to their links with other models for which cascading deletion is not an option. In the future, the `Delete` will be replaced with the __Active/Disabled__ approach instead.

## <a name="existing-features"></a>Existing Features

### Sign up and Log in

When first accessing the application, the user is directed to a _Log in_ page. The page includes a link to a _Sign up_ form, should the visitor not yet have an account. _Sign up_ and _Log in_ forms are delivered by __Allauth__ Django app. The forms are fully validated for correct data input, and the _Sign up_ form asks to confirm the inserted password and an option to provide an e-mail address.

Log in form 
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/Sign_in_unauth_user_landing_p.png" width="500">

Sign up form
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/Sign_up_page.png" width="500">

All users are managed via backend Django admin site, where __superadmin__ user can assign users to the __Admin__ group with advanced rights. 
At the moment, the application is not linked to any e-mail address and the passwords can only be reset via contact with the application admin. This will be fixed in the future, however, considering the internal nature of the application this is not affecting the app usability hugely at this stage.

### Landing page

After logging in, a standard User is redirected to their homepage, where they can see a list of quizzes that have been published (i.e. set to `Approved`. If the quiz has been completed it is marked as such, and the button for taking the quiz is replaced with __Results__ that take the user to a page showing their results for that particular quiz.

Standard user's home page
<img src='https://github.com/Koko-66/teaze/blob/main/static/data/Standard_user_home_page.png' width="500">

Admin users, on the other hand, are redirected to a dashboard with an overview of quizzes, questions and categories existing in the application. From here, via an extended menu, they can manage (create, edit and delete) all of these elements.

Admin user's home page
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/Admin_user_home_page.png" width="500">

### Navigation

The navigation menu is placed at the top of the page and changes depending on whether the user is authenticated or not, and also depending on the type of user. 

Non-authenticated user's menu
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/non-authenticated_user_menu.png" width="200">

Standard user's menu
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/standard_user_menu.png" width="200">

Admin user's menu
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/admin_user_menu.png" width="500">

The menu is also responsive and collapses into a button on smaller devices.

### Taking the quiz

On their homepage, a standard User can see a list of all published quizzes available for them to take as well as those they have already taken. 
Upon clicking the _Take quiz_ button, the user is taken to a page with a list of all questions.
Take quiz view
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/take_quiz.png" width="500">

The quiz allows only one answer per question, however, not all questions have to be answered to submit the quiz. On submission, the User is redirected to a page showing their results - total score for the quiz and feedback for each of the questions. These quiz results are available for the User to view at any time via the links on each quiz card on their homepage.

Quiz results view
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/quiz_results.png" width="500">

Each response is saved as an individual answer assigned to an assessment which is saved against the user and, at present, the user cannot take the same quiz more than once. This again is something to be discussed and agreed on with the stakeholders.

### Quiz creation

To create a new quiz, the user needs to be assigned relevant permissions by the superuser, e.g. by adding them to the __Admin__ group. Adding a quiz is a simple process and can be done either directly from the Dashboard or the _Manage quizzes_ page accessible from the __Menu__ at the top of the page.

Adding quiz from Dashboad
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/add_quiz_from_dashboard.png" width="500">

Adding quiz from Manage quizzes
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/add_quiz_from_manage_quizzes.png" width="500">

Clicking the __Add__ button initiates the _Add quiz_ form, where the user can fill in the quiz Title (required), Category (required), Description (optional), and Image (optional). The form is validated for required fields and checks if a quiz with the same title already exists.

Add quiz form 
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/add_quiz_form.png" width="500">

A quiz can only be assigned one category, and if the required category does not yet exist, it can be added from the _Add quiz_ view as well.

Add category while creating new quiz
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/add_category_while_in_quiz.png" width="500">

If the user decides not to save the changes, they can cancel the process at any point by clicking either the __Cancel__ button or the __X__ sign in the top right corner of the form.

Clicking __Save__, redirects the user to a view with quiz details.

### Quiz details view

After creating a quiz, the Admin user is redirected to a _Quiz detail_ page, where they can see information about the quiz: title, status, category, description, image and quiz questions, if any already exist.
If there are any questions in the database that are assigned the same category as the quiz and are not assigned to any other quiz, they are listed below the main quiz details and can be added to the quiz by clicking the small __+__ icon showing to the right. Similarly, questions can be as easily removed from the quiz by clicking the __x__ icon in the quiz questions list.
Note that this action merely removes the question from the quiz and does not delete it.

List of questions availble for adding to the quiz
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/available_questions_to_add.png" width="500">

The __Edit quiz__ button redirects the user to the _Edit quiz_ page, where the user can make tweaks to the quiz details. The form mirrors the _Add quiz_ form but is populated with existing quiz data.

<img src ="https://github.com/Koko-66/teaze/blob/main/static/data/edit_quiz.png" width="500">

#### Setting quiz status

A quiz can be set as either `Draft` or `Approved`. Until the status is set to `Draft`, quiz will not be visible to a standard user to prevent them from completing quizzes which are not completed and verified.
At the time of creating, a new quiz is set to `Draft` as detault and can be toggled to `Approved` in the Quiz detail view, once admin user is finished setting it up. 

On setting the quiz to `Approved` a pop-up alert informs the user that the status has been changed and the quiz is now available for all test-takers.

#### Quiz featured image 

The user can upload a feature image to the quiz which is uploaded directly to Cloudinary. The images are then appearing as background on the quiz cards and can be showing as a background to the quiz in the Take Quiz and Resulsts views in the future. Images can be previewed in the Quiz details view, can be removed and updated as needed. There are certain considerations for using images in the application (in relation to size, colouring,  ratios, etc.) which will be addressed in the admin user training and contorlled programmatically in the future.

![Quiz details with image thumbnail](https://github.com/Koko-66/teaze/blob/main/static/data/quiz_details_with_img_thumbnail.png)

#### Quiz preview

Once created, admin user has an option to check the quiz as it would appear to a standard user by using __Preview__ button on the quiz card in the Manage quizzes page. The Preview mimics the actual quiz-taking experience of a standard user. Admin user's quizzes get saved into the database to ensure everything is working correctly, but they can take the quiz more than once.

### Managing questions

Questions are a building block of the application and as such, have their own model and can be managed as individual items. The question management page can be accessed from the link in the card on the _Home_ page or link in the menu at the top of the page.

In the Qustion management page the admin user sees a list of questions with their basic details and is able to filter them by category and quiz, and search by keywords typed in. The filter is collapsed by default to make the page cleaner. When a filter is applied a button for clearing it appears. 
![Manage question page with filter not collapsed](https://github.com/Koko-66/teaze/blob/main/static/data/manage_question_filters.png)

![Manage qestion page with Clear filter button](https://github.com/Koko-66/teaze/blob/main/static/data/question_filters_when_selected.png)

#### Adding questions

A new question can be added from _Quiz detail_ page , in which case the Quiz property of the question is being automatically set to that of the quiz viewed, or from _Manage questions_ page, where the question can be created without selecting a quiz and added to a quiz when needed.

![Adding question from Quiz details page](https://github.com/Koko-66/teaze/blob/main/static/data/create_question_in_quiz.png)

![Adding question from Manage questions page](https://github.com/Koko-66/teaze/blob/main/static/data/add_question_from_question_manag.png)

A question can be assigned more than one category by holding down `Ctrl` button (or `Cmd` on a Mac) and making a selection. The user is informed about this on the form.

Once the user is happy with the the information they put in and click `Save`, they are redirected to a question detail page, which is also an editing view.

#### Featured images in questions

As in quiz, the images can have their own images with a view that some questions might require images for illustration purposes or which can be part of the question. 

#### Editing questions and managing options

The question details view follows the same layout as quiz view, including image preview.
The user can edit question elements individually by clicking on the edit icon. Each edit form opens in a separate modal showing over the page, which helps the user stay focused on the task. 

![Question details page with modal open](https://github.com/Koko-66/teaze/blob/main/static/data/edit_question_modal_view.png)

On this page the user also gets an opprotunity to manage options - they can add and delete them as required. Because options are not part of a question model but have model of their own, the number of options per qustions is not determined by design and can be set individually per question. 

#### Option uniqueness checks

At present, the application design allows for only one option to be set as correct. To prevent the user from setting more than one answer as correct, and once one option is set as such, the tick box for is_correct is replaced with information that one correct option already exists.
![Adding option when correct answer already exists](https://github.com/Koko-66/teaze/blob/main/static/data/add_option_when_correct_exists.png)

#### Question status

As quizzes, questions have two statuses _Draft_ and _Approved_. At present this feature is simply for to the admin user to keep track of questions that still needs to be reviewed, but they can still be used in the quiz, if the user wishes to use them. 
Draft qustions are clearly indicated in the _Quiz detail_ page and can be reviewed and approved before adding to the quiz and publishing the latter.

![Draft questions indicated in the Quiz detail page](https://github.com/Koko-66/teaze/blob/main/static/data/draft_qustions_in_quiz_details.png)

#### Deleting questions and options
Question can be deleted from the _Manage questions_ or _Question details_ pages however the option is only available if it is not used in any quiz. Before the question is deleted, the application will also performa an  additional check to see if it appears any saved assessments. If yes, the user will be provided with appropriate feedback, and deletion would not be possible.
Options can be deleted from _Question details_ page as well, and are also checked for appearance in saved answers to prefent Protected error. 

!()
Considering the data model and the fact that assessments and answers need to be stored beyoed the life-cycle of any quiz, question or option, the deletions need further consideation and will be replaced with 'active/disabled' approach instead.

### Managing Categories

Categories are the smalles model and are the simplest to manage. They can be added while creating a new quiz or from their own _Manage categories_ page. 
An attempt to delete a Category triggers a check for its use in a Quiz or a Question and prevents the deletion if the Category is used in any of these.

### Accessibility and alerts

To increase users' engagement with the application each button that does not contain text has a `title` tag which on hover provides information about the button's function. Each action is also confirmed by an alert, which is dismissed automatically after 3 seconds if the uer does not dissmiss it.

## <a name="left-to-implement">Features Left to Implement</a>

### User managment of their own account

In the future, the user will have access to a page allowing them to manage their account, change their password, add an avatar etc.

### Display quiz questions one per page

Display one question per page would be especially helpful for questions using an image as part of their content. 

### Assessment management for Admin user

At present, management of the assessments is only available to the admin user via Django admin page after they have been set as Staff members by a superuser. In the future this functionality would be available for admin users from front-end.


# <a name="django-admin">Management via Django admin site</a>


# <a name="technologies">Technologies used</a>
## <a name="languages">Languages</a>

Programming languages used in the project: 

- HTML and CSS3
- Python
- JavaScript

## <a name="libraries-and-programs"></a>Frameworks, Libraries, Plugins and other services used
- __Django__: main application framework
- __Bootstrap__: CSS styling
- __GitPod__: primary code editor
- __Git__:  for version control
- __[Git Hub](https://github.com/)__: to store project files
- __[Python Tutor](https://pythontutor.com/)__: used to help with debugging
- __darw.io__: to create the data model and program logic flow chart
- __Balsamiq__: for wireframes
- __Cloudinary__: to store image files uploaded by the user
- __PostgreSQL Database__: serving as main database
- __Coverage__: create reporting on level of tests
- __[AllAuth](https://django-allauth.readthedocs.io/en/latest/)__: user management
- __[django-bootstrap-modal-forms](https://pypi.org/project/django-bootstrap-modal-forms/)__: to display forms in modals
- __[django-filter](https://django-filter.readthedocs.io/en/stable/)__: used on the Manage questions page to filter the content
- __[Heroku](https://www.heroku.com/)__: used to deploy the live version of the project
- __[whitenoise](http://whitenoise.evans.io/en/stable/django.html)__: to serve static files correctly in production
- __Beautify__: VSCode extenstion to format code
- __[Am I Responsive?](http://ami.responsivedesign.is/#)__ site to generate the responsive mockup

# <a name="errors-testing">Error handling and testing</a>

The error handling is currently mostly hadnled by the inbuilt functionality of class based views as well as some if-statment based checks within these. Going forward, the application willbe be using a more robust approach using a set of custom error classes.

Information about the application testing is available in a separate file [here]().

# <a name="deployment">Deployment</a>
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
8. Towards the end of development, enabled static files by chaning the value of DISABLE_COLLECTSTATIC to 0. Resolved issues caused by settings for cloudinary in the static files setup in the settings.py file (see Testing file for more details).
9. Installed whitenoise to ensure static files are served in production mode.
 
# Requirements
All requirements are contained in the requirements.txt file.

# <a name="credits">Credits</a>
A great thank you to: 
- My mentor, Caleb Mbakwe, for invaluable advice on the best approach to the project, organisation of code, and support throughout the whole project. 
- Stackoverflow: for pointing in the right direction on arranging question and option models
- https://stackoverflow.com/questions/54048741/nonetype-object-has-no-attribute-is-ajax: for solving issue of pulling author from logged user rather than having to set it in the form.
<!-- - Izen Oku: for his [blog post](https://medium.com/swlh/overview-building-a-full-stack-quiz-app-with-django-and-react-57fd07449e2f) on creating a Quiz app:  -->
- https://www.youtube.com/watch?v=vXXfXRf2S4M
- Creators of [Heroku documentation](https://devcenter.heroku.com/).

