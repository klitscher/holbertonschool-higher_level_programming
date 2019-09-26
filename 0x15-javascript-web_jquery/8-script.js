$.get('https://swapi.co/api/films/?format=json', function (data) {
  const results = data.results;
  for (const film of results) {
    const item = $('<li></li>').text(film.title);
    $('UL#list_movies').append(item);
  }
});
