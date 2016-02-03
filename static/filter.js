/**
 * Created by chris on 01/02/2016.
 */
/** this is the legacy version of the filter, still currently in use at /main and /open
 *
 * It is being deprecated in favour of the Datatables.net functionality
 */


var $rows = $('.Row');
$('#search').keyup(function() {
    var val = $.trim($(this).val()).replace(/ +/g, ' ').toLowerCase();

    $rows.show().filter(function() {
        var text = $(this).text().replace(/\s+/g, ' ').toLowerCase();
        return !~text.indexOf(val);
    }).hide();
});