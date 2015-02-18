$(document).ready(function(){
// using jQuery
function getCookie(name) {
var cookieValue = null;
if (document.cookie && document.cookie != '') {
var cookies = document.cookie.split(';');
for (var i = 0; i < cookies.length; i++) {
var cookie = jQuery.trim(cookies[i]);
// Does this cookie string begin with the name we want?
if (cookie.substring(0, name.length + 1) == (name + '=')) {
cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
break;
}
}
}
return cookieValue;
}
var csrftoken = getCookie('csrftoken');	
$("#go").click(function () {
var tweet = $('#tweet').val();
var rt = $('#rt').val();
var fav = $('#fav').val();
$.ajax({
type:'POST',
url:'http://127.0.0.1:8000/gonder/',
data:{tweet: tweet, rt: rt, fav: fav},
success:function(cevap){
$("#sonuc").html(cevap);
},
});
});


});