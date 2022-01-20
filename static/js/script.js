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
        $(this).modalForm({
            formURL: $(this).data("form-url")});
    });

    $('#save-question').click(function(){
        $('#add-option').addClass('d-inline');
    });

      // Read book buttons
    $(".question-details").each(function () {
        $(this).modalForm({formURL: $(this).data("form-url")});
    });

    // CATEGORIES - MODALS //
    // Add category link opens form in modal with id="add-category-modal"
    // $("#add-category").modalForm({
    //     formURL: "/categories/add_category/",
    //     modalID: "#add-category-modal"
    // });

    $(".add-category").each(function () {
        $(this).modalForm({
            formURL: $(this).data("form-url"),
            // formURL: "/categories/add_category/",
            modalID: $(this).data("modal-id"),
            // modalID: "#add-category-modal"
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

    // Toggle button function (not posting to object)
    // $( document.body ).click(function() {
    //     $( ".toggle-btn" ).each(function(i) {
    //         console.log("event attached")
    //         if ( this.value != 0 ) {
    //             this.value = 0;
    //             this.innerHTML="Draft"
    //         } else {
    //             this.value = 1;
    //             this.innerHTML="Published"
    //         }    
    //     sendData();   
    // });

});

        
// const url = window.location.href;
// const csrf = document.getElementsByName('csrfmiddlewaretoken');
// // console.log(csrf)

// const sendData = () => {
//     const question = document.querySelector("#status");
//     // question.dataset.id = 1
//     // question.dataset.user = "xyz"

//     console.log(question.dataset.id);

//     let data = {}
//     let status = [...document.getElementsByName('status')];
//     data['csrfmiddlewaretoken'] = csrf[0].value
//     status.forEach(el => {
//         data[el.name] = el.value
//     })
//     data['id'] = question.dataset.id

//     $.ajax({
//         type: 'POST',
//         url: `${url}toggle/`,
//         data: data,
//         success: function(response) {
//             console.log(response)
//             },
//         error: function(error) {
//             console.log(error)
//         }
//     })
// }
// })