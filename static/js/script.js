$( document ).ready(function () {
    // QUIZZES - MODALS //

    // Delete quiz button - formURL is retrieved from the data of the element
    $(".delete-quiz").each(function () {
        $(this).modalForm({formURL: $(this).data("form-url"), isDeleteForm: true});
    });

    // // Edit quiz button - formURL is retrieved from the data of the element
    // $(".edit-quiz").each(function () {
    //     $(this).modalForm({formURL: $(this).data("form-url")});
    // });

    // QUESTIONS - MODALS //
  
    // Delete question button - formURL is retrieved from the data of the element
    $(".delete-question").each(function () {
        $(this).modalForm({formURL: $(this).data("form-url"), isDeleteForm: true});
    });

    $(".delete-option").each(function () {
        $(this).modalForm({formURL: $(this).data("form-url"), isDeleteForm: true});
    });

    // Edit question button - formURL is retrieved from the data of the element
    $(".edit-option").each(function () {
        $(this).modalForm({
            formURL: $(this).data("form-url")});
    });

      // Question details buttons
    $(".question-details").each(function () {
        $(this).modalForm({formURL: $(this).data("form-url")});
    });

    // CATEGORIES - MODALS //

    // Add category link opens form in modal with id="add-category-modal"
    $(".add-category").each(function () {
        $(this).modalForm({
            formURL: $(this).data("form-url"),
            modalID: $(this).data("modal-id"),
        });
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
