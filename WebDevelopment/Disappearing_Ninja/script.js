
$('img').click(function () {
    $(this).hide('slow');
    console.log("Successfully Image is Hidden");
});


$('button').click(function(){
    console.log("Entered Inside Button")

    $('img[style]').show();

})
