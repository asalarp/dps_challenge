
const axios = require('axios');
var hotpOtpGenerator = require('hotp-totp-generator');

const totpToken = hotpOtpGenerator.totp({
        key: '', 
        T0: 0,
        X: 120,
        algorithm: 'sha512',
        digits: 10});
        
axios.defaults.headers.common['Authorization'] = 'Basic ' + totpToken;
axios.defaults.headers.post['Content-Type'] = 'application/json';

axios.post('', {
  "github":"",
  "email":"",
  "url":"", 
  "notes":""
  })
  .then((response) => {
    console.log(response);
  }, (error) => {
    console.log(error);
  });