function reload() {
    window.location.reload()
};

$('.my-selectpicker').selectpicker('val');

$(function() {
    $('[data-toggle="tooltip"]').tooltip()
})

//---------------------------------------------------------------------


$.fn.select2.defaults.set("theme", "bootstrap");
$(document).ready(function() {
    $('.basic-multiple').select2();
    $('.basic-single').select2();
});

//---------------------------------------------------------------------


$(document).ready(function() {
    createTable('user_publication_table',null,'sortable');
} );
