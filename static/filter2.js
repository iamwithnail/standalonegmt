/**
 * Created by chris on 01/02/2016.
 */
$(document).ready(function(){
 //add index column with all content.
 $(".filterable tr:has(td)").each(function(){
   var t = $(this).text().toLowerCase(); //all row text
   $("<td class='indexColumn'></td>")
    .hide().text(t).appendTo(this);
 });//each tr
 $("#search").keyup(function(){
   var s = $(this).val().toLowerCase().split(" ");
   //show all rows.
   $(".filterable tr:hidden").show();
   $.each(s, function(){
       $(".filterable tr:visible .indexColumn:not(:contains('"
          + this + "'))").parent().hide();
   });//each
 });//key up.
});//document.ready