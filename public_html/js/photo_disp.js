$(document).ready(function() {
    var displaying = false;

    $(".smallphoto").click(function(evt) {
        var img_url = $(evt.target).attr("src").replace("shrunk", "full");
        $("#photo-overlay").empty();
        $("#photo-overlay").append("<p class=\"overlay-text\">Click anywhere to close.</p><img src=\"" + img_url + "\">");
        $("#photo-overlay").css("display", "block");
        displaying = true;
    });

    $("#photo-overlay").click(function(evt) {
        $("#photo-overlay").css("display", "none");
        $("#photo-overlay").empty();
        displaying = false;
    });

    $(window).keyup(function(evt) {
        if(displaying) {
            $("#photo-overlay").css("display", "none");
            $("#photo-overlay").empty();
            evt.preventDefault();
        }
        displaying = false;
    });

    $(window).keypress(function(evt) {
        if(displaying) {
            $("#photo-overlay").css("display", "none");
            $("#photo-overlay").empty();
            evt.preventDefault();
        }
        displaying = false;
    });
});
