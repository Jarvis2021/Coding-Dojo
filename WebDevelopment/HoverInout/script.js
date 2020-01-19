
var originalimg = '';
$('img').hover(function () {
    originalimg = $(this).attr("src");
    $(this).attr("src", "https://media-prd.coachella.com/content/coachella/homepage_img2.jpg");
}, function () {
    $(this).attr("src", originalimg);
});