$(document).ready(function() {
	
	// append toTop div to the bottom of the body tag.
    $('body').append('<div id="toTop" class="btn btn-info"><i class="fas fa-arrow-up"></i></div>');
	
	// function to show the button based on page position.
	$(window).scroll(function () {
		// if not at the top of the page
		if ($(this).scrollTop() != 0) {
			// fade the button in.
			$('#toTop').fadeIn();
		} else {
			// fade the button out.
			$('#toTop').fadeOut();
		}
	}); 
    
    // click function for toTop button.
    $('#toTop').click(function(){
        // smoothly scroll to the top of the page.
        $("html, body").animate({ scrollTop: 0 }, 600);
        return false;
    });
});