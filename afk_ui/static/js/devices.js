var filter= [];

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

$('.all-filter').click(function() {
    filter=[];
    get_device_info(filter=filter)
//    get_device_info(filter=false)
})

$('.local-filter').click(function() {
    filter=[{"name":"connectedHost","op":"eq","val":"IP"}];
    get_device_info(filter=filter)
//    get_device_info(filter="[{\"name\":\"connectedHost\",\"op\":\"eq\",\"val\":\"IP\"}]")
})

$('.pac-filter').click( function() {
    filter.push({"name":"isPac","op":"eq","val":true})
    get_device_info(filter=filter)
//    get_device_info(filter="[{\"name\":\"isPac\",\"op\":\"eq\",\"val\":true}]")
})

$('#example-getting-started').on('change', function() {
    var selected_devices = [];
    $('option:selected').each(function(){
        selected_devices.push($(this).val())
    });
    (selected_devices.length > 0) && filter.push({"name":"deviceType","op":"in_","val": selected_devices});
    get_device_info(filter=filter);

//    (selected_devices.length > 0) ? get_device_info(filter=`[{\"name\":\"deviceType\",\"op\":\"in_\",\"val\":${JSON.stringify(selected_devices)}}]`) : get_device_info(filter=false);
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