// $(function() {
//     $('.submit').click(function(){
//         console.log('Button Submit Clicked');
//         const btn = document.querySelector(".button");
//         btn.classList.toggle("button--loading");
//     });
// });


$(document).on('submit', '#contactForm', function(event) {
    event.preventDefault();
    //console.log('Button Submit Clicked');

    var clickedObj = $(".button");
    clickedObj.addClass("active");
    console.log('active');


    const csrf = document.getElementsByName("csrfmiddlewaretoken")
    var name = $('.contact-form #name').val();
	var email = $('.contact-form #email').val();
    var subject = $('.contact-form #subject').val();
	var message = $('.contact-form #message').val();

    var dataPost = new FormData();
	dataPost.append("csrfmiddlewaretoken", csrf[0].value);
	dataPost.append("name", name);
	dataPost.append("email", email);
    dataPost.append("subject", subject);
	dataPost.append("message", message);
    //console.log(dataPost);

    $.ajax({
        method: 'POST',
        url: '',
        data: dataPost,
        processData: false,
        contentType: false,
        //context: btn,
        dataType: 'json',

        success: function(response) {
            var msg = response['msg'];
            console.log(msg);
            if (msg == 'valid') {
                console.log(response)
                //alert("Form valid");
                clickedObj.removeClass("active");
                clickedObj.addClass("success");
                setTimeout(function(){
                    clickedObj.removeClass("success");
                }, 3000);
            } else {
                console.log(response)
                //alert("Form invalid");
                clickedObj.removeClass("active");
                clickedObj.addClass("error-form");
                setTimeout(function(){
                    clickedObj.removeClass("error-form");
                }, 3000);             
            }
        },
        error: function(error) {
            console.log(error)
            //alert("Error: Message not delievered!");
            clickedObj.removeClass("active");
            clickedObj.addClass("error-break");
            setTimeout(function(){
                clickedObj.removeClass("error-break");
            }, 3000);               
        }
    })
});