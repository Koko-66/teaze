# TESTING
The program was tested at each step of the development within the development environment as well as on Heroku after deployment. The testing process included:
1. [User Stories testing](#user-stories-testing)
2. [Validator testing](#validator-testing)
2. [Programmatic testing](#programmatic-testing)
3. [Performance testing](#performance-testing)
4. [Development testing](#bugs-and-fixes)
5. [Deployment testing](#deployement-testing)

## <a name="user-stories-testing"></a>User Story testing
Functionality testing was completed as each of the stories in the Git Project were completed. Refer [here]() for details of the stories.
This entailed going through each feature of the app and ensuring that the application runs as expected and yields expected resutls, without causing any errors.

## <a name="validator-testing"></a>Validator testing 
Each module has been checked with [Pep 8 online check](http://pep8online.com/) validator and developed in an environment with enabled linters: pylint, flake8 and cornflakes-linter (VS Code extensions).
HTML and CSS were checked in their relevant W3C validators. Results are available [here]().

## <a name="programmatic-testing"></a>Programmatic testing 
In addition to testing the code during the development using various print statments, the code was also tested programmatically using Unittest.
The tests are placed in their folder in each application and are split according to the part they are testing - models, views and forms. The decisions on which part of code need to be tested or are missing tests were based on reports generated with the use of Coverage plugin.
The test coverage is checked using Coverage and the latest report is availble for view [here]().

## <a name="performance-testing"></a>Performance and responsiveness testing
Performance testing was done by running the application on various devices and browsers, including:
- Browsers: Firefox 9, Chrome, Safari, Samsung (mobile)
- Devices: Laptop 13', Samsung Note 8 and Samsung Note 10, iPad Pro 10 inch
In addition, responsiveness of design was tested extensively in Firefox DevTools


## <a name="bugs-and-fixes"></a>Development Testing
Each feature was tested while being developed to ensure correct and error-free functionality.
Bugs encountered during the development and their fixes are listed below.

Taking the quiz:

1. Adding pagination caused issues with the from submission as a whole, with only the last question submitting; 
___FIXED__: moved navigation to the next page to form action element to allow for adding "submit" to the OK and Next button.
    - issue with the answers now saving if hitting previous


    - issue with index out of range if question not answered

2. Removing position from the Option model removed the `required` property from questions when listing them in the `take_quiz` view. This allows for not all the questions to be answered, which in turn means that if not all questions are answered, the assessment will be incomplete and only contain the data for the answered questions. 
Added a hidden pre-checked radio-button to convey those cases.
__FIXED__: Added a hidden and pre-checked input field to the list of options to each questions that remaines checked if an answer to the question is not provided.

3. Adding `assessment` variable to the index.html page causes an UnboundLocalError (local variable 'assessment' referenced before assignment) when reaching the page if no assessments are present for the user.
__FIXED__: declared `assessment` with value `None` that is overwritten if assessment exists.

4. When viewing the results of the already taken test, the assessment score goes back to 0. 
__FIXED__: Changed view post function to use the `update` method to update the assessment score after the loop going over all questions finishes. 

5. Issues with redirections when trying to manage questions/options. 
__FIXED__: in quiz app added class views that are based off classes in qustions with different success urls and paths including slug to use in if statements in tempaltes to check which function to use.

6. Sometimes a question gets duplicated in the view

7. Saving option when one with the same name and selected as correct and if same text, but not correct - doesn't save the first time, but does the second. 

8. When trying to serve static files to Heroku (chagning DISABLE_COLLECTSTATIC to 0) Heroku throws an error pointing to an issue in cloudinary settings.  `File "/app/.heroku/python/lib/python3.9/site-packages/cloudinary_storage/storage.py", line 241, in _exists_with_etag
           etag = response.headers["ETAG"].split('"')[1]
         File "/app/.heroku/python/lib/python3.9/site-packages/requests/structures.py", line 54, in __getitem__
           return self._store[key.lower()][1]
       KeyError: 'etag'`
Removed entires for   from the settings file for testing, which seemed to resoved the problem.