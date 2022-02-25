
<!-- ![](my logo?)  -->
# TABLE OF CONTENTS
1. [Introduction](#intro)
2. [UX](#ux)<br>
  2.1 [User Stories](#user-story)
3. [Features and design](#features-design)<br>
  3.1. [Existing features](#existing-features)<br>
    3.1.1. [Sign up and Login](#sign-up)<br>
    3.1.2. [Landing page](#landing-page)<br>
    3.1.3. [Navigation](#navigation)<br>
    3.1.4. [Taking the quiz](#take-quiz)<br>
    3.1.5. [Managing quizzes](#managing-quizzes)<br>
    3.1.6. [Managing questions](#managing-questions)<br>
    3.1.6. [Managing categories](#managing-categories)<br>
    3.1.6. [User feedback and alerts](#user-feedback)<br>
  3.2. [Features left to implement](#left-to-implement)<br>
4. [Management via Django admin](#django-admin)
5. [Technologies](#technologies)<br>
  5.1. [Languages used](#languages)<br>
  5.2. [Frameworks, libraries and programs used](#libraries-and-programs)
6. [Testing](#errors-testing)
7. [Deployment](#deployment)
8. [Credits](#credits)


# <a name="intro"></a>Teaze


Teaze is a web-based application built for use as an internal self-testing tool in aid of training as well as for use in more fun team building activities. In the future, its use might be extended to external users as a marketing tool aiming at increasing the engagement of the existing and potential customers and encouraging them up for the company's newsletter.

At present, the application is at Stage 1 of development and the focus of the development efforts has been placed on achieving a functioning Minimum Viable Product (MVP) that allows the users to take and create quizzes. Further improvements to the application UI and functionality will be ventured after the main stakeholders' input and testing.

Link to the deployed app: https://teaze.herokuapp.com/accounts/login/


# <a name="ux"></a>UX

The initial user interface design idea was captured in the wireframes available [here](https://github.com/Koko-66/teaze/blob/main/data/teaze_wireframes.pdf), while the flow of the application logic in a diagram available for viewing [here](https://github.com/Koko-66/teaze/blob/main/static/data/Teaze_algorithm.pdf).
The design is driven by the user's needs and ease of use. It aims to replicate the process the user would usually go through when creating a quiz, but also offer flexibility by providing access to various features from different places in the application and at different stages of creating or managing a quiz (e.g. editing questions or adding and removing their options).
With user experience in mind, the design of the application is kept simple with a primary focus placed on functionality. 


## <a name="user-story"></a>User Stories 

The application was developed using Agile methodology, with User Stories managed within a Github Project. All completed and outstanding User Stories can be viewed [here](https://github.com/Koko-66/teaze/projects/1).


# <a name="features-design"></a>Features and Design

## Models and functional design

The application uses the Postgres relationship database to store its data and the data model is comprised of `Quiz`, `Question`, `Option`, `Category`, `Assessment` and `Answer`. The components of each model and the relationships between them are represented in a graphic model representation available [here](https://github.com/Koko-66/teaze/blob/main/static/data/teaze_data_model.pdf).

The decision to keep `Quiz`, `Question` and `Options` as separate models was driven by flexibility. This kind of approach allows maximum flexibility when creating quizzes and questions, as the user is not restricted to a pre-set structure, number of questions per quiz, options per question etc. It also allows for the questions to be reused even if the quiz has been deleted, as they are not inherently a part of the quiz either.

This approach, however, calls for careful consideration of the relationships between various models and what should happen if instances of these are deleted while related to an instance of another model. These considerations are still pending in Teaze app, and need to be addressed.

At present, the relationship between quiz and question is One-to-Many, though it would, arguably, be more beneficial to the user to be able to use the same question in more than one quiz. The deletion of questions, options and categories also poses a problem due to their links with other models for which cascading deletion is not an option. In the future, the `Delete` will be replaced with the __Active/Disabled__ approach instead.

## <a name="existing-features"></a>Existing Features

### <a name="#sign-up"></a>__Sign up and Log in__

When first accessing the application, the user is directed to a _Log in_ page. The page includes a link to a _Sign up_ form, should the visitor not yet have an account. _Sign up_ and _Log in_ forms are delivered by __Allauth__ Django app. The forms are fully validated for correct data input, and the _Sign up_ form asks to confirm the inserted password and an option to provide an e-mail address.

Log in form<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/Sign_in_unauth_user_landing_p.png" width="500">

Sign up form<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/Sign_up_page.png" width="500">

All users are managed via backend Django admin site, where __superadmin__ user can assign users to the __Admin__ group with advanced rights. 
At the moment, the application is not linked to any e-mail address and the passwords can only be reset via contact with the application admin. This will be fixed in the future, however, considering the internal nature of the application this is not affecting the app usability hugely at this stage.

### <a name="#landing-page"></a>__Landing page__

After logging in, a standard User is redirected to their homepage, where they can see a list of quizzes that have been published (i.e. set to `Approved`. If the quiz has been completed it is marked as such, and the button for taking the quiz is replaced with __Results__ that take the user to a page showing their results for that particular quiz.

Standard user's home page<br>
<img src='https://github.com/Koko-66/teaze/blob/main/static/data/Standard_user_home_page.png' width="500">

Admin users, on the other hand, are redirected to a dashboard with an overview of quizzes, questions and categories existing in the application. From here, via an extended menu, they can manage (create, edit and delete) all of these elements.

Admin user's home page<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/Admin_user_home_page.png" width="500">

### <a name="#navigation"></a>__Navigation__

The navigation menu is placed at the top of the page and changes depending on whether the user is authenticated or not, and also depending on the type of user. 

Non-authenticated user's menu<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/non-authenticated_user_menu.png" width="200">

Standard user's menu<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/standard_user_menu.png" width="200">

Admin user's menu<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/admin_user_menu.png" width="500">

The menu is also responsive and collapses into a button on smaller devices.

### <a name="#take-quiz"></a>__Taking the quiz__

On their homepage, a standard User can see a list of all published quizzes available for them to take as well as those they have already taken. 
Upon clicking the _Take quiz_ button, the user is taken to a page with a list of all questions.

Take quiz view<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/take_quiz.png" width="500">

The quiz allows only one answer per question, however, not all questions have to be answered to submit the quiz. On submission, the User is redirected to a page showing their results - total score for the quiz and feedback for each of the questions. These quiz results are available for the User to view at any time via the links on each quiz card on their homepage.

Quiz results view<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/quiz_results.png" width="500">

Each response is saved as an individual answer assigned to an assessment which is saved against the user and, at present, the user cannot take the same quiz more than once. This again is something to be discussed and agreed on with the stakeholders.


### <a name="#managing-quizzes"></a>__Managing quizzes__

The _Manage quizzes_ page can be accessed from the link in the card on the _Home_ page or via the Menu at the top of the page. Each quiz has its own card with some basic information and links to delete or edit a quiz, as well as add a new one.

<img scr="https://github.com/Koko-66/teaze/blob/main/static/data/manage_quizzes.png" width="500">

#### __*Creating a quiz*__

To create a new quiz, the user needs to be assigned relevant permissions by the superuser, e.g. by adding them to the __Admin__ group. Adding a quiz is a simple process and can be done either directly from the Dashboard or the _Manage quizzes_ page accessible from the __Menu__ at the top of the page.

Adding quiz from Dashboad<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/add_quiz_from_dashboard.png" width="500">

Adding quiz from Manage quizzes<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/add_quiz_from_manage_quizzes.png" width="500">

Clicking the __Add__ button initiates the _Add quiz_ form, where the user can fill in the quiz Title (required), Category (required), Description (optional), and Image (optional). The form is validated for required fields and checks if a quiz with the same title already exists.

Add quiz form<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/add_quiz_form.png" width="500">

A quiz can only be assigned one category, and if the required category does not yet exist, it can be added from the _Add quiz_ view as well.

Add category while creating new quiz<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/add_category_while_in_quiz.png" width="500">

If the user decides not to save the changes, they can cancel the process at any point by clicking either the __Cancel__ button or the __X__ sign in the top right corner of the form.

Clicking __Save__, redirects the user to a view with quiz details.

#### __*Quiz details view*__

After creating a quiz, the Admin user is redirected to a _Quiz detail_ page, where they can see information about the quiz: title, status, category, description, image and quiz questions, if any already exist.
If there are any questions in the database that are assigned the same category as the quiz and are not assigned to any other quiz, they are listed below the main quiz details and can be added to the quiz by clicking the small __+__ icon showing to the right. Similarly, questions can be as easily removed from the quiz by clicking the __x__ icon in the quiz questions list.
Note that this action merely removes the question from the quiz and does not delete it.

List of questions availble for adding to the quiz<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/available_questions_to_add.png" width="500">

The __Edit quiz__ button redirects the user to the _Edit quiz_ page, where the user can make tweaks to the quiz details. The form mirrors the _Add quiz_ form but is populated with existing quiz data.

<img src ="https://github.com/Koko-66/teaze/blob/main/static/data/edit_quiz.png" width="500">

#### __*Setting quiz status*__

A quiz can be set as either `Draft` or `Approved`. By default when created a quiz is given a status of `Draft`. Until the status is set to `Draft`, a quiz will not be visible to a standard User to prevent them from completing quizzes that have not been finished and verified.
The quiz can be toggled to `Approved` in the _Quiz detail_ page at any time, once an Admin user is finished setting it up. 

On setting the quiz to `Approved` a pop-up alert informs the user that the status has been changed and the quiz is now available for all test-takers.

#### __*Quiz featured image*__

The user can upload an image to act as a feature image for the quiz which is uploaded directly from the form to Cloudinary. The uploaded images are then appearing as background on the quiz cards and can be set as showing as a background to the quiz in the _Take Quiz_ and _Resulsts_ pages in the future. Images appear on the _Quiz details_ page as thumbnails and can be removed and updated as needed. There are certain considerations for using images in the application (in relation to size, colouring,  ratios, etc.) that will be addressed in the Admin user training and controlled programmatically in the future.

Quiz details with image thumbnail<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/quiz_details_with_img_thumbnail.png" width="500">

#### __*Quiz preview*__

Once created, an Admin user has an option to check the quiz as it would appear to a standard User by using the __Preview__ button on the quiz card in the _Manage quizzes_ page. The __Preview__ mimics the actual quiz-taking experience of a standard user. Admin users' quizzes get saved into the database to ensure everything is working correctly, but they can take the quiz more than once.

### <a name="#managing-questions"></a>__Managing questions__

The _Manage questions_ page can be accessed from the link in the card on the _Home_ page or via the Menu at the top of the page.

In the _Manage questions_ page the admin user sees a list of questions with their basic details and can filter them by category and quiz, and search by text that might show in the question text. Filtering options are collapsed by default to make the page cleaner but are easily accessible at the top of the page.

Filter optons<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/manage_question_filters.png" width="500">

When a filter is applied a button __Clear filters__  appears that clears all filters and shows all questions in the database.

Manage qestion page with __Clear filter__ button<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/question_filters_when_selected.png" width="500">

#### __*Adding questions*__

A new question can be added from the _Quiz detail_ page, in which case the `quiz` and `category` properties of the question are set based on those of the quiz, or from the _Manage questions_ page, where the question can be created without selecting a quiz or category and added to a quiz when needed.

Adding question from Quiz details page<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/create_question_in_quiz.png" width="500">

Adding question from Manage questions page<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/add_question_from_question_manag.png" width="500">

A question can be assigned more than one category by holding down the `Ctrl` button (or `Cmd` on a Mac) and making a selection. The user is informed about this option on the form.

Once the user is happy with the information they provided and click `Save`, they are redirected to the _Question detail_ page, which is also an editing view.

#### __*Featured images in questions*__

As in a #### Featured images in questions

As in a quiz, a question can have a featured image with a view that some questions might require images for illustration purposes or which can be part of the question. This is also handled by Cloudinary and works in the same way as in the case of quizzes.quiz, a question can have a featured image with a view that some questions might require images for illustration purposes or which can be part of the question. This is also handled by Cloudinary and works in the same way as in the case of quizzes.

#### __*Editing questions and managing options*__

The _Question details_ follows the same layout as the _Quiz details_ page, including the image preview as a thumbnail.
For convenience, the user can edit question elements individually by clicking on the __Edit__ icon. The edit form for each of the elements opens in a separate modal showing over the page, which helps the user stay focused on the task. 

Question details page with modal open<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/edit_question_modal_view.png" width="500">

On this page the user also gets an opportunity to manage options - they can create and delete them as required. Because options are not part of a question model but have a model of their own, the number of options per question is not determined by design and can be set individually per question. Creating and editing forms for options are also opened in modals for convenience.

#### __*Option uniqueness checks*__

At present, the quiz design allows only one option to be set as correct. To prevent the Admin user from setting more than one answer as correct, the tick box for `is_correczt is replaced with information that one correct option already exists if this is the case.

Adding option when correct answer already exists<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/add_option_when_correct_exists.png" width="500">

#### __*Question status*__

As quizzes, questions have two statuses _Draft_ and _Approved_. At present this feature is simply for the Admin user to keep track of questions that still need to be reviewed, but they can still be used in the quiz if the Admin wishes so. 
Draft questions are clearly indicated in the _Quiz detail_ page and can be reviewed and approved before adding to the quiz and publishing the latter.

Draft questions indicated in the Quiz detail page<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/draft_qustions_in_quiz_details.png" width="500">

#### __*Deleting questions and options*__
A question can be deleted from the _Manage questions_ or _Question details_ pages, however, the option to delete it is only available if it is not used in any of the existing quizzes. Before the question is deleted, the application will also perform an additional check to see if it appears in any of the saved assessments. If yes, the user will be provided with appropriate feedback, and the deletion would not be possible.
Options can be deleted from the _Question details_ page as well, and are also checked for appearance in saved answers to prevent ProtectedError. 

!()
As explained above, considering the data model and the fact that assessments and answers need to be stored beyond the life-cycle of any quiz, question or option, the deletions need further consideration and will be replaced with an `Active/Disabled` approach instead.
 
### <a name="#managing-categories"></a>__Managing Categories__

Categories are the smallest model and are the simplest to manage. They can be added while creating a new quiz or from their own _Manage categories_ page. 
An attempt to delete a Category triggers a check for its use in a Quiz or a Question and prevents the deletion if the Category is used in any of these.

### <a name="#user-feedback"></a>__User feedback and alerts__

To increase users' engagement with the application the user is offered feedback on various operations via alerts as well as the use of `title` tags.

## <a name="left-to-implement"></a>Features Left to Implement

### User management of their account

In the future, the user will have access to a page allowing them to manage their account: change their password, add an avatar etc.

### Display quiz questions one per page

Displaying one question per page would be especially helpful for questions using an image as part of their content. 

### Assessment management for Admin user

At present, management of the assessments is only available to the admin user via the Django admin page after they have been set as Staff members by a user with superuser rights. In the future, this functionality would be available for Admin users from the front-end as well.

### Other

There are a lot of additional features that can be added to the application to improve the user experience and add functionality. These will be discussed with the stakeholders, changed into new User Stories and prioritised as appropriate.

# <a name="django-admin"></a>Management via Django admin site

As with any Django application, all models and functionality of the application can be managed via Django's administration site, provided the user is set as a __Staff__ user. 

Superuser has access to all content while Admin user has only certain specific permissions available to them.

Admin user Django admin access
<img src="" width="500">

To make the management easier in the Django admin site, the models have been set up to be viewed as sets of data (e.g. questions can be added within quiz and options within questions). The views also include filters and display information on the main page deemed most important. Again, this can be easily adjusted depending on the stakeholders and admin preferences.

__Quiz details__<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/djangp_admin_gr_quiz_details.png" width="500">

__Question list__<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/django_admin_gr_question_list.png" width="500">

__Question details__<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/django_admin_gr_questions.png" width="500">

__Assessment list__<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/django_admin_gr_assessment_list.png" width="500">

__Assessment_details__<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/django_admin_gr_assessment_details.png" width="500">

__Answers__<br>
<img src="https://github.com/Koko-66/teaze/blob/main/static/data/django_admin_gr_answer_list.png" width="500">


# <a name="technologies"></a>Technologies used
## <a name="languages"></a>Languages

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


# <a name="errors-testing"></a>Error handling and testing

The error handling is currently mostly handled by the inbuilt functionality of class-based views as well as some if-statement based checks within these. Going forward, the application will be using a more robust approach using a set of custom error classes.

Information about the application testing is available in a separate file [here](https://github.com/Koko-66/teaze/blob/main/TESTING.md).


# <a name="deployment"></a>Deployment
The program was deployed to Heroku at the start of the project to ensure its correct functioning and is accessible here: 

The steps taken to deploy the app: 

1. Updated the contents of the requirements file using the `pip3 freeze > requirements.txt` command in VS Code.
2. Checked the project structure and run the program to ensure everything is working as expected.
3. Created the Tease project on Heroku, giving it the name 'teaze'.
4. Added a new Postgres database:
  - In the Resources tab, searched for Heroku Postgres add-in and selected the free Hobby Dev option.
5. In the Config Vars section of the Settings tab, added the environment variables to set up: 
  - Link to Postgres database 
  - Link to Cloudinary
  - Disabled static files for the time of development
  - App secret key
5. In the Deployment tab:
 - selected GitHub as deployment method,
 - selected Connect,
 - authorised Heroku to access the GitHub account,
 - searched for 'teaze' repository and confirmed the connection.
6. First time deployed the app using the manual Deploy Branch button, then enabled automatic deploys.
7. Once the first build was complete, changed the settings to deploy automatically. 
8. Towards the end of development, enabled static files by changing the value of DISABLE_COLLECTSTATIC to 0. Resolved issues caused by settings for Cloudinary in the static files setup in the settings.py file (see Testing file for more details).
9. Installed Whitenoise to ensure static files are served in production mode.
 
 
# Requirements
All requirements are contained in the requirements.txt file.

# <a name="credits"></a>Credits
A great thank you to: 
- My mentor, Caleb Mbakwe, for invaluable advice on the best approach to the project, organisation of code, and support throughout.
- Stackoverflow community: for pointing in the right direction on so many issues it's not efficient to list them here, though specific mention should be given to Bishwa Karki for solving the issue of [pulling author from the logged user rather than having to set it in the form](https://stackoverflow.com/questions/54048741/nonetype-object-has-no-attribute-is-ajax).
- TO Izen Oku: for his [blog post](https://medium.com/swlh/overview-building-a-full-stack-quiz-app-with-django-and-react-57fd07449e2f) on creating a Quiz app and pointers on how to organise my database models.
- [To PyPlane](https://www.youtube.com/channel/UCQtHyVB4O4Nwy1ff5qQnyRw) and [Lara Code](https://www.youtube.com/channel/UClXcbBNNhFU9ATAcXB6U7eQ) for their tutorials on creating a quiz in Django.
- Creators of Django and Heroku documentation as well as authors of all the plugins and libraries used in this application.

