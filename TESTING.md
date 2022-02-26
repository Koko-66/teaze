# TESTING
The program was tested at each step of the development within the development environment as well as on Heroku after deployment. The testing processes included:
1. [User Stories testing](#user-stories-testing)
2. [Validator testing](#validator-testing)
2. [Programmatic testing](#programmatic-testing)
3. [Performance testing](#performance-testing)
4. [Development testing](#bugs-and-fixes)

## <a name="user-stories-testing"></a>User Story testing
Functionality was tested at each stage of development and as each of the stories in the Git Project was completed. Refer [here](https://github.com/Koko-66/teaze/projects/1) for details of the stories.
The testing entailed going through each feature of the app and ensuring that the application runs as expected and yields expected results, without causing any errors.

## <a name="validator-testing"></a>Validator testing 
Each view file has been checked with [Pep 8 online check](http://pep8online.com/) validator. The development took place also in an environment  with enabled linters: pylint, flake8 and cornflakes-linter (VS Code extensions).
Some errors raised by Pep 8 refer to the length of links to code refernced in comments and have not been resolved.
HTML and CSS were checked in their relevant W3C validators and results with some notes on remaining errors and warnings are available [here](https://github.com/Koko-66/teaze/blob/main/static/data/CSS%20and%20HTML%20validation.pdf).
The deployed application was also checked with __Lighthouse__ and some reports can be accessed [here](https://github.com/Koko-66/teaze/tree/main/static/data/lighthouse_reports).

## <a name="programmatic-testing"></a>Programmatic testing 
In addition to testing the code during the development using various print statments, the code was also tested programmatically using Unittest.
Each application has its own `tests` with test files divided according to the part they are testing - `models`, `views` and `forms`. 
The testing is done in an SQlite database separate from the production one, which uses its own `test_settings.py` file.
The decisions on which part of code needed testing were based on reports generated with the use of __Coverage__ plugin and at the most current report stands at 92%.

## <a name="performance-testing"></a>Performance and responsiveness testing
Performance testing was done by running the application on various devices and browsers, including:
- Browsers: Firefox 9, Chrome, Safari, Samsung (mobile)
- Devices: Laptop 13', Samsung Note 8 and Samsung Note 10, iPad Pro 10 inch
In addition, the responsiveness of design was tested extensively in Firefox DevTools

## <a name="bugs-and-fixes"></a>Development Testing
Each feature was tested while being developed to ensure correct and error-free functionality. Each of the bugs encountered was resolved by using a combination of error message analysis, print statements, and research for possible causes and solutions.
Some more pertinent bugs encountered during the development and their fixes are listed below.

1. Removing `position` from the __Option__ model removed the `required` property from question options radio buttons which were in position 1 when listed in the `take_quiz` view. This resulted in a situation where not all questions had to be answered, which in turn meant that the submitted assessment data was incomplete and only contained data for the answered questions.  
__FIXED__: To each listed question added a hidden and pre-checked input field which remains checked if an answer to the question is not provided, thus still providing the response data to push to backend.

2. Adding `assessment` variable to the _index.html_ page caused an UnboundLocalError (local variable 'assessment' referenced before assignment) when reaching the page if no assessments exist for the logged-in user.
__FIXED__: declared `assessment` with value `None` that is overwritten if assessment exists.

3. When viewing the results of the already taken test, the assessment score goes back to 0. 
__FIXED__: Changed view post function to use the `update` method rather than `create` to update the assessment score after the loop going over all questions finishes. 

4. Issues with redirections when trying to create/edit/delete questions/options. 
Since the questions and options can be managed both from _Quiz details_ page as well as from the _Manage questions_ using the same _Question detail_ page to follow DRY principles, the application needed a way to manage redirects depending on where _Manage questions_ page was accessed from.
__FIXED__: Based `quiz` class views relating to the question and options management on classes from `questions`, so that they inherit all their functionality, but added `get_success_url` functions specifying different redirect paths, `if` functions to the templates to check for the presence of `quiz.slug` in the `kwargs` arguments passed in the urls, as well as using different url paths.
 
6. When trying to serve static files to Heroku (chagning DISABLE_COLLECTSTATIC to 0) Heroku throws an error pointing to an issue in cloudinary settings.  
`File "/app/.heroku/python/lib/python3.9/site-packages/cloudinary_storage/storage.py", line 241, in _exists_with_etag
  etag = response.headers["ETAG"].split('"')[1]
File "/app/.heroku/python/lib/python3.9/site-packages/requests/structures.py", line 54, in __getitem__
  return self._store[key.lower()][1]
KeyError: 'etag'`
Since the error message from the deployment log pointed clearly to Cloudinary storage as the failing point, removed: `STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'` and `DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'` from the `settings.py` file for testing, which seemed to resoved the problem and did not cause any issues with uploading images to the application, thus removed from the settings file. This solution worked fine when in DEBUG mode, however meant that in production no static files were served. 
__FIXED__: Used __Whitenoise__ for serving the static files and Cloudinary for handling media uploads only. Needed to remove'cloudinary_storage' from installed aps to avoid conflict. 

### Issues pending fixing
1. Saving an option whose text matches exactly one that already exists results in the second option to be added, however, if the already existing option is selected as correct, the duplicate is not created and the operation fails silently in the background without an error. 
This needs to be investigated further.

2. When editing a category in a question, the form does not allow saving if no option is selected, thus preventing `category` from being set to None. This seems to be caused by form validation settings and would also need further investigation.
