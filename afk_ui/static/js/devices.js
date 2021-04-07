function create_device_objects(device_info) {
    d_info_data = device_info["data"];
    d = document.querySelector('mel-grid-sizer');
    for (var i = 0; i < d_info_data.length; i++){

    }

}



//function get_device_info() {
//    fetch('http://localhost:8888/api/v1/device_info')
//    .then(response=>response.json())
//    .then(device_info=>{
//        console.log(device_info);
//        create_device_objects(device_info);
//    })
//}

function get_device_info() {
    fetch('http://localhost:8888/api/v1/device_info')
    .then(res=>{
        d_info = res;
        console.log(d_info);
        return res.text();
//        create_device_objects(device_info);
    })
    .then(devices_cards => {
//    data = data ;
//    console.log(data);
    // Convert the HTML string into a document object
	  var parser = new DOMParser();
	  var devices_cards_dom = parser.parseFromString(devices_cards, 'text/html');
//	  debugger;
	  console.log(devices_cards_dom.body)
      //document.querySelector('.mel-grid-sizer').appendChild(devices_cards_dom);
//      document.querySelector('.mel-grid-sizer').appendChild(devices_cards_dom.body);
    /*  mel_grid = document.querySelector('.mel-grid') */

      $grid.innerHTML = devices_cards;
      $grid.append('<div class="mel-grid-sizer"></div>');

//    $('#container').html(data);
});
}

//var step1_continue = document.querySelector("first_step");
var filter_button = document.querySelector(".mel-filter");
//step1_continue.addEventListener('click', get_device_info)
filter_button.addEventListener('click', get_device_info)