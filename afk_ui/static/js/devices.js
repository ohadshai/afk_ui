function get_server_url(){
    return window.location.href.split('/')[2]
}

function get_device_info(filter) {
    filter = filter ? `filter=${filter}` : "";
    fetch(`http://${get_server_url()}/api/v1/device_info?${filter}`)
    .then(res=>{
        return res.text();
//        create_device_objects(device_info);
    })
    .then(devices_cards => {
      $grid.html(devices_cards);
      $grid.append('<div class="mel-grid-sizer"></div>');

});
}

$('.all-filter').click(function() {
    get_device_info(filter=false)
})

$('.pac-filter').click( function() {
    get_device_info(filter="[{\"name\":\"isPac\",\"op\":\"eq\",\"val\":true}]")
})

$('#example-getting-started').on('change', function() {
    var selected_devices = [];
    $('option:selected').each(function(){
        selected_devices.push($(this).val())
    });

    (selected_devices.length > 0) ? get_device_info(filter=`[{\"name\":\"deviceType\",\"op\":\"in_\",\"val\":${JSON.stringify(selected_devices)}}]`) : get_device_info(filter=false);
})

$('.pointer-label low').on('change', function() {
    a = $(this).val();
    b = 1;
})

$('.pointer-label high').on('change', function() {
    a = $(this).val();
    b = 1
})