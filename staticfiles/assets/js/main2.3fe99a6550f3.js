var call = function(token) {
    console.log("reCAPTCHA validated for 'data-widget-uuid=\"XXX\"'")
    grecaptcha.render();

};

$(document).on('submit', '#contactForm, #Notification', function(event) {
    event.preventDefault();
    console.log('Button Submit Clicked', event.target.id);
    //grecaptcha.execute();

    if (event.target.id == 'Notification') {
        button = document.querySelector(".button-Notify");
        button.innerHTML = "<div class='loader'></div>";

        var clickedObj = $(".button-Notify");
    
        const csrf = document.getElementsByName("csrfmiddlewaretoken")
        var tag = "Notification";
        var name = $('.notification-form #nameNote').val();
        var email = $('.notification-form #emailNote').val();
        let captcha = $('[name=g-recaptcha-response]');
    
        var dataPost = new FormData();
        dataPost.append("csrfmiddlewaretoken", csrf[0].value);
        dataPost.append("tag", tag);
        dataPost.append("name", name);
        dataPost.append("email", email);
        //dataPost.append("g-recaptcha-response", $('#g-recaptcha-response').val());
        //console.log(grecaptcha.getResponse());
    
        $.ajax({
            method: 'POST',
            url: '',
            data: dataPost,
            processData: false,
            contentType: false,
            dataType: 'json',
    
            success: function(response) {
                var msg = response['msg'];
                console.log(msg);
                if (msg == 'valid') {
                    grecaptcha.execute();
                    $( '#Notification' ).each(function(){
                        this.reset();
                    });
                    button.innerHTML = "<div class='valid-form'><h5>Thank You!</h5></div>";
                    setTimeout(function(){
                        button.innerHTML = "Get notified!";
                    }, 4000);
                } else {
                    button.innerHTML = "<div class='invalid-form'><h5>Error! Please Check Your Details..<h5></div>";
                    setTimeout(function(){
                        button.innerHTML = "Get notified!";
                    }, 4000);             
                }
            },
            error: function(error) {
                button.innerHTML = "<div class='invalid-form'><h5>Error! Please try again later..<h5></div>";
                setTimeout(function(){
                    button.innerHTML = "Get notified!";
                }, 4000);               
            }
        })
    }
    else if (event.target.id == 'contactForm') {
        button = document.querySelector(".button-Contact");
        button.innerHTML = "<div class='loader2'></div>";
 
        var clickedObj = $(".button-Contact");
    
        const csrf = document.getElementsByName("csrfmiddlewaretoken")
        var tag = "contactForm";
        var name = $('.contact-form #name').val();
        var email = $('.contact-form #email').val();
        var subject = $('.contact-form #subject').val();
        var message = $('.contact-form #message').val();
    
        var dataPost = new FormData();
        dataPost.append("csrfmiddlewaretoken", csrf[0].value);
        dataPost.append("tag", tag);
        dataPost.append("name", name);
        dataPost.append("email", email);
        dataPost.append("subject", subject);
        dataPost.append("message", message);
    
        $.ajax({
            method: 'POST',
            url: '',
            data: dataPost,
            processData: false,
            contentType: false,
            dataType: 'json',
    
            success: function(response) {
                var msg = response['msg'];
                if (msg == 'valid') {
                    $( '#contactForm' ).each(function(){
                        this.reset();
                    });
                    button.innerHTML = "Message Sent"
                    setTimeout(function(){
                        button.innerHTML = "Send Message";
                    }, 4000);
                } else {
                    button.innerHTML = "<div class='invalid-form'><h5>Error! Please Check Your Details..<h5></div>";
                    setTimeout(function(){
                        button.innerHTML = "Send Message";
                    }, 4000);             
                }
            },
            error: function(error) {
                button.innerHTML = "<div class='invalid-form'><h5>Error! Please try again later..<h5></div>";
                setTimeout(function(){
                    button.innerHTML = "Send Message";
                }, 4000);               
            }
        })
    }
});