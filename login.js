function signin(){
    var username = $('#user').val();
    var password = $('#pwd').val();    
    if (!username){
       alert ('please fill user input');
       return
    }
    if (!password){
       alert ('please fill password input');
       return  
    }
    
    var patt = /[^A-Za-z0-9]/g;
    var result = username.match(patt);
    if (result){
        alert("fill according to requirement\nAtleast 8 Character with including lowercase,uppercase,number");
        return
    }
    console.log(username);
    console.log(password);

    $.ajax({
        url: '../../../cgi-bin/vipul/login.py',
        type: 'POST',
        data: {'user': username, 'pwd': password, 'login': 'signin'},
        success: function(result){
                    alert(result);
        },
        error: function(error){
                   alert(error.statusText);
                },        
     });
  }

function create_signup(){
    add_element = '<li><p id="login_label"><label for="email">Email</label></p></li><li class="login_input"><input type="email" id="email" class="login_input1" placeholder="Email"></li>';
    $(".ul_login li:eq(1)").after(add_element);

    $("p#ul_header").hide();   
    $("#login_button")[0].innerHTML = "Sign up";
    $("#login_button")[0].setAttribute("onclick","signup()")

}

function signup(){
    var email = $('#email').val();     
    var username = $('#user').val();  
    var password = $('#pwd').val();    
    if (!username){
       alert ('please fill user input');
       return
    }
    if (!password){
       alert ('please fill password input');
       return  
    }
    if (!email){
       alert ('please fill email input');
       return
    }

    
    var patt = /[^A-Za-z0-9]/g;
    var result = username.match(patt);
    if (result){
        alert("fill according to requirement.\nAtleast 8 Character with including lowercase,uppercase,number")
        return
    }
    console.log(username);
    console.log(password);

    $.ajax({
        url: '../../../cgi-bin/vipul/login.py',
        type: 'POST',
        data: {'user': username, 'pwd': password,'login':'signup','email':email},
        success: function(result){
                    asdd = result
                    alert(asdd);
                    window.location.reload();
                    

        },
        error: function(error){
                   alert(error.statusText);
              },        
    });
}
function myFunction() {
  var txt;
  var person =prompt("Please enter your username:");
  if (person == null || person == "") {
    txt = "User cancelled the prompt.";
  }
  else {
    txt = "Hello " + person + "! How are you today?";
  }
}
