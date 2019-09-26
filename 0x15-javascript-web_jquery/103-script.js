window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + lang;
    $.get(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
  $('INPUT#language_code').on('keypress', function (enter) {
    if (enter.which === 13) {
      const lang = $('INPUT#language_code').val();
      const url = 'https://fourtonfish.com/hellosalut/?lang=' + lang;
      $.get(url, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });
};
