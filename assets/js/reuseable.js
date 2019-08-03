$(document).ready(function() {
    //$("#header-wrapper").on("load", "../pages/partials/header.html #header");
    loadReuseable();
    //chooseHeaderPic();
    $(document).ajaxStop(function() {

        $("#sidebar-open").click(function() {
            $("#sidebar").toggleClass('opened');

        });
    });


});

var chooseHeaderPic = function() {
    var header_pic_arr = ["(\'../img/header-pic.png\')", "(\'../img/header-pic1.gif\')", "(\'../img/header-pic2.jpg\')", "(\'../img/header-pic3.jpg\')"];
    var random_pic = header_pic_arr[Math.floor(Math.random() * header_pic_arr.length)];
    $(document).ajaxStop(function() {
        $("#header-pic").css("background-image", "url" + random_pic);
        //window.open($("#header-pic").css("background-image"));
        //alert($("#header-pic").css("background-image"));
    });

}

var loadReuseable = function() {
    //$("#header-wrapper").load("partials/header.html");
    //$("#footer-wrapper").load("partials/footer.html");
};
