$.get('https://swapi.co/api/people/5/?format=json', function (data) {
  const character = data.name;
  $('DIV#character').text(character);
});
