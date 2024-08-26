function eml()
{
var cemail=/^[a-z0-9.-]+@[a-z0-9.-]+\.[a-z]{2,7}$/;
var email=document.getElementById("cemail").value;
// alert(email);
if(!cemail.test(email))
{
alert("Wrong email");
document.getElementById("sp5").innerHTML="Wrong Email";
document.getElementById("sp5").style.color="red";
document.getElementById("pemail").style.border="2px solid red";
}
else
{
alert("Right email");
document.getElementById("sp5").innerHTML="Right Email";
document.getElementById("sp5").style.color="green";
document.getElementById("pemail").style.border="2px solid green";
}
}