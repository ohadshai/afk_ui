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

//var all_filter = document.querySelector('.all-filter');
//var pac_filter = document.querySelector('.pac-filter');

//filter_button.addEventListener('click', get_device_info)