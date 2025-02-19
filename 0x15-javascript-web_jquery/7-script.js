// script that fetches the character name from this URL:i
// https://swapi-api.hbtn.io/api/people/5/?format=json
const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('DIV#character').append(data.name);
});
