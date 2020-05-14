$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (key in data.results) {
    $('#list_movies').append('<li>' + data.results[key].title + '</li>');
  }
});
