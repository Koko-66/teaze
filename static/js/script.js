// console.log('Hello world')

$( document ).ready(function () {
    // Delete category buttons - formURL is retrieved from the data of the element
    $(".delete-category").each(function () {
        $(this).modalForm({formURL: $(this).data("form-url"), isDeleteForm: true});
    });

    // Add category button opens form in modal with id="add-category-modal"
    $("#add-category").modalForm({
        formURL: "/categories/add_category/",
        modalID: "#add-category-modal"
    });
});