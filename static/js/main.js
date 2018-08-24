
$(function() {
  // datepicker para fechas de nacimiento
    $( ".datepicker-range" ).datepicker({
    dateFormat: "yy-mm-dd",
    changeMonth: true,
    changeYear: true,
    minDate: "-100Y",
    maxDate: "-14Y",
    yearRange: "-100:-14",}).val();
    // datepicker standar
  $( ".datepicker" ).datepicker({
    dateFormat: "yy-mm-dd",
    changeMonth: true,
    changeYear: true,}).val();
  // blockea fechas mayores a la actual
  $( ".datepicker-max" ).datepicker({
    dateFormat: "yy-mm-dd",
    changeMonth: true,
    changeYear: true,
    maxDate: new Date}).val();
  // blockea fechas menores a la actual
  $( ".datepicker-min" ).datepicker({
    dateFormat: "yy-mm-dd",
    changeMonth: true,
    changeYear: true,
    minDate: new Date}).val();
  // muestra tiempo como horas
  $('.timepicker').timepicker({ 'timeFormat': 'H:i:s' });

});


 $(document).ready(function() {
    var table = $('#dataTable').DataTable({
        "language": {
                url: "/static/localizacion/es_ES.json"
        }});
     
    $('#dataTable tbody').on('click', 'tr', function () {

        var data = table.row( this ).data();
        //alert( 'You clicked on '+data[0]+'\'s row' );
        
        
    } );
 } );

function getDate() {
    var d = new Date();
    var day = addZero(d.getDate());
    var month = addZero(d.getMonth()+1);
    var year = addZero(d.getFullYear());
    var h = addZero(d.getHours());
    var m = addZero(d.getMinutes());
    var s = addZero(d.getSeconds());
    return day + "-" + month + "-" + year + " " + h + ":" + m;
}

// AJAX
function sendAjax(url, params, myCallback, args) {
    if (typeof args === "undefined") {
        load_elem = "#load";
    } else {
        load_elem = args.load_elem;
    }
    /*$(load_elem).show().html('<img src="/static/img/load16.gif" />');*/
    $(load_elem).show().html('Cargando...');
    if (typeof args === "undefined" || args.met === "get") {
        $.get(url, params).done(function(data) {
            myCallback(data);
            $(load_elem).fadeOut();
        }).fail(function(error) {
            console.log(error);
        });
    } else if (args.met === "post") {
        $.post(url, params).done(function(data) {
            myCallback(data);
            $(load_elem).fadeOut();
        }).fail(function(error) {
            console.log(error);
        });
    }
}


function abrir_modal(url)
{
    $('#popup').load(url, function()
    {
        $(this).modal('show');
    });
    return false;
}


function cerrar_modal()
{
        $('#popup').modal('hide');
        return false;
}


function delete_actividad(url) {
    $.getJSON(url, function (data) {
        console.log(data)
        location.reload();
        alert("Se ha eliminado correctamente");
    });   
}


$(document).ready(function()
{
    var table = $('#dataTables').dataTable({
        "language": {
                url: "/static/es_ES.json"
        }}  );
});