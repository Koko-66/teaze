// console.log('Hello world')

$( document ).ready(function () {
    // QUIZZES - MODALS //
    // Add quiz link opens form in modal with id="add-question-modal"
    $("#add-quiz").modalForm({
        formURL: "/quiz/add_quiz/",
        modalID: "#add-quiz-modal"
    });

    // Delete quiz button - formURL is retrieved from the data of the element
    $(".delete-quiz").each(function () {
        $(this).modalForm({formURL: $(this).data("form-url"), isDeleteForm: true});
    });

    // Edit quiz button - formURL is retrieved from the data of the element
    $(".edit-quiz").each(function () {
        $(this).modalForm({formURL: $(this).data("form-url")});
    });

    // QUESTIONS - MODALS //
    // Add question link opens form in modal with id="add-question-modal"
    $("#add-question").modalForm({
        formURL: "/questions/add_question/",
        modalID: "#add-question-modal"
    });

    // Delete question button - formURL is retrieved from the data of the element
    $(".delete-question").each(function () {
        $(this).modalForm({formURL: $(this).data("form-url"), isDeleteForm: true});
    });

    // Edit question button - formURL is retrieved from the data of the element
    $(".edit-question").each(function () {
        $(this).modalForm({formURL: $(this).data("form-url")});
    });

    // CATEGORIES - MODALS //
    // Add category link opens form in modal with id="add-category-modal"
    $("#add-category").modalForm({
        formURL: "/categories/add_category/",
        modalID: "#add-category-modal"
    });

    // Delete category buttons - formURL is retrieved from the data of the element
    $(".delete-category").each(function () {
        $(this).modalForm({formURL: $(this).data("form-url"), isDeleteForm: true});
    });

    // Edit category button - formURL is retrieved from the data of the element
    $(".edit-category").each(function () {
        $(this).modalForm({formURL: $(this).data("form-url")});
    });

});