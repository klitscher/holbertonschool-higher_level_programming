const lang = navigator.language;
const url = 'https://fourtonfish.com/hellosalut/?lang=' + lang;
$.get(url, function (data) {
  $('DIV#hello').text(data.hello);
});
