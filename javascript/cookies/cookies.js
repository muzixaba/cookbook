// Cookies are small text files store on client's computer. Used to remember info about the user in order to personalize the web page.
// Cookies are stored in the browser's memory and are sent with every HTTP request to the server.

// Check is cookies are enabled
console.log(navigator.cookieEnabled);

// Create a cookie
document.cookie = "name=Muzi; expires=Thu, 18 Dec 2024 12:00:00 UTC; path=/";
document.cookie = "surname1=Xaba; expires=Thu, 18 Dec 2024 12:00:00 UTC; path=/";

// Delete a cookie (use past date)
document.cookie = "surname1=Xaba; expires=Thu, 18 Dec 2014 12:00:00 UTC; path=/";

// Create a cookie with a function
setCookie("email", "muzi@email.com", 15);

// Get a cookie with a function
var firstname = getCookie("name");
if (firstname != null) {
  console.log(firstname);
}


// view all cookies
console.log(document.cookie);


// function to create a cookie
function setCookie(name, value, daysToExpire) {
  var date = new Date();
  date.setTime(date.getTime() + (daysToExpire * 24 * 60 * 60 * 1000));
  var expires = "expires=" + date.toUTCString();
  document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

// function to get a cookie
function getCookie(name) {
  var cookieName = name + "=";
  var cookies = document.cookie.split(';');
  for(var i = 0; i < cookies.length; i++) {
    var cookie = cookies[i].trim();
    if (cookie.indexOf(cookieName) == 0) {
      return cookie.substring(cookieName.length, cookie.length);
    }
  }
  return null;
}


// get and set cookies in html
const username = document.querySelector('#username');
const surname = document.querySelector('#surname');
const submitBtn = document.querySelector('#submitBtn');
const getCookiesBtn = document.querySelector('#showBtn');

// when user clicks the Submit button, set the cookies
submitBtn.addEventListener('click', () => {
  setCookie('username', username.value, 15);
  setCookie('surname', surname.value, 15);
});

// when user clicks the Show Cookies button, get the cookies
getCookiesBtn.addEventListener('click', () => {
  username.value = getCookie('username');
  surname.value = getCookie('surname');
});