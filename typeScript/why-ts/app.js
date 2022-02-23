// api url
var url = 'https://jsonplaceholder.typicode.com/users/1';

// dom
var username = document.querySelector('#username');
var email = document.querySelector('#email');
var address = document.querySelector('#address');

// user data
var user = {};


/**
 * @typedef {object} Address
 * @property {string} street
 * @property {string} city
 */

/**
 * @typedef {object} user
 * @property {string} name
 * @property {string} email
 * @property {Address} address
 */


/**
 * @returns {Promise<user>}
 */
function fetchUser(){
  return axios.get(url);
}

fetchUser().then(function(response){
  response.address.city
})

function startApp() {
  // axios
  //   .get(url)
  fetchUser()
    .then(function (response) {
      user = response.data;
      console.log(user)
      
      // TODO: 이름, 이메일, 주소 표시하기
      username.innerText = user.name;
      email.innerText = user.email;
      address.innerText = user.address.street;
    })
    .catch(function (error) {
      console.log(error);
    });
}

startApp();
