var g_filter= [];
var g_page = 1;

function get_server_url(){
    return window.location.href.split('/')[2]
}

function get_device_info(filter, page=1) {
    var page_filter = "";
    var filter = filter.length ? `filter=${JSON.stringify(filter)}` : "";
    if (filter){page_filter = "&";}
    page_filter = page > 1 ? page_filter + `page[number]=${page}` : "";
    fetch(`http://${get_server_url()}/api/v1/device_info?${filter}${page_filter}`)
    .then(res=>{
        return res.text();
    })
    .then(devices_cards => {
      $grid.html(devices_cards);
      $grid.append('<div class="mel-grid-sizer"></div>');

});
}

function remove_filter(key, value=null){
    for (i=0; i < g_filter.length;i++){
        if (g_filter[i].hasOwnProperty(key)){
           if (value == null){
                g_filter.splice(i, 1);
           }
           else if ((value != null) &&  (g_filter[i][key] == value)){
                g_filter.splice(i, 1);
           }

         }
     }
}


$('.all-filter').click(function() {
    g_filter=[];
    get_device_info(filter=g_filter)
})

$('.local-filter').click(function() {
    g_filter=[{"name":"connectedHost","op":"eq","val":"IP"}];
    get_device_info(filter=g_filter)
})



$( ".dropdown-menu" ).css('margin-top',0);
$( ".dropdown" )
  .mouseover(function() {
    $( this ).addClass('show').attr('aria-expanded',"true");
    $( this ).find('.dropdown-menu').addClass('show');
//    $( this ).find('.dropdown-toggle').addClass('show');
  })
  .mouseout(function() {
    $( this ).removeClass('show').attr('aria-expanded',"false");
    $( this ).find('.dropdown-menu').removeClass('show');
//    $( this ).find('.dropdown-toggle').removeClass('show');
  });


$('.dropdown-menu a').click(function () {
   $( this ).parent().parent().find( 'a.active' ).removeClass('active');
   $( this ).addClass('active');

   var pac = null;
   if ($(this).text()  == "True"){
       pac = true;
   } else if ($(this).text()  == "False"){
       pac = false;
   }
   remove_filter(key="name", value="isPac");
   if (pac != null){
       g_filter.push({"name":"isPac","op":"eq","val": pac });
   }
   get_device_info(filter=g_filter);
   });

$('#hw-list').on('change', function() {
    var selected_devices = [];
    $('option:selected').each(function(){
        selected_devices.push($(this).val())
    });
    remove_filter(key="name", value="deviceType");
    (selected_devices.length > 0) && g_filter.push({"name":"deviceType","op":"in_","val": selected_devices});
    get_device_info(filter=g_filter);
})

$('.pointer-label low').on('change', function() {
    a = $(this).val();
    b = 1;
})

$('.pointer-label high').on('change', function() {
    a = $(this).val();
    b = 1
})

$('.page-link').click( function() {
    var page = $(this).text();
    get_device_info(filter=[], page)
})