// //console.log(document.getElementById("lime").innerText);
 console.log($("#lime").css("color", "green").css("display", "inline"));



$("button").click(function(){
    $("img").slideToggle(2000, function () {
    
         $("img").attr("src", "sophie.jpeg");
        // $("img").fadeIn(5000);
    });
});
