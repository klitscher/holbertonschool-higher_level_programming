window.onload = function () {
  $('DIV#add_item').click(function () {
    const item = '<li>Item</li>';
    $('UL.my_list').append(item);
  });
  $('DIV#remove_item').click(function () {
    $('UL.my_list > li').last().remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list > li').remove();
  });
};
