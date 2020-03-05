// //getting all textboxes
// var username = document.getElementById("username");
// var password = document.getElementById("password");
// var cpassword = document.getElementById("cpassword");
//
// //getting all error display objects
// var reqname = document.getElementById("reqname");
// var reqemail = document.getElementById("reqemail");
// var reqmessage = document.getElementById("reqmessage");
//
// //setting all event listeners
// username.addEventListener("blur", nameVerify, true);
// email.addEventListener("blur", emailVerify, true);
// message.addEventListener("blur", messageVerify, true);
//
// //validation function
// function validation(){
//   //getting all input text objects
//   var forname = document.getElementById("name").value;
//   var foremail = document.getElementById("email").value;
//   var formessage = document.getElementById("message").value;
//
//   if(forname == null || forname == "")
//      {
//        //name validation
//        reqname.textContent = "please type a valid name";
//        username.focus();
//        return false;
//      }
//   if (foremail == null || foremail == "" || foremail.indexOf('@')<=0 || foremail.charAt(foremail.length-4) != '.')
//      {
//        //email validation
//        reqemail.textContent = "please type a valid email";
//        email.focus();
//        return false;
//      }
//   if (formessage == null || formessage == "")
//      {
//        //message validation
//        reqmessage.textContent = "please type a message";
//        message.focus();
//        return false;
//      }
// }
//
// //event handler funtions
// function nameVerify(){
//   if(username.value != ""){
//     reqname.textContent = "";
//     return true;
//   }
// }
// function emailVerify(){
//   if(email.value != ""){
//     reqemail.textContent = "";
//     return true;
//   }
// }
// function messageVerify(){
//   if(message.value != ""){
//     reqmessage.textContent = "";
//     return true;
//   }
// }
