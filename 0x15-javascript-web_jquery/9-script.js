const lang = $('html').attr('lang');
$.get('https://fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
  $('DIV#hello').text(data.hello);
});
