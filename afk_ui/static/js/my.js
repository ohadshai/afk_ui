function create_device_objects(device_info) {
    d_info_data = device_info["data"];
    d = document.querySelector('mel-grid-sizer');
    for (var i = 0; i < d_info_data.length; i++){

    }

}



function get_device_info() {
    fetch('http://localhost:8888/api/v1/device_info')
    .then(response=>response.json())
    .then(device_info=>{
        d_info = device_info;
        console.log(device_info);
        create_device_objects(device_info);
    })
}

var step1_continue = document.getElementById("first_step");
step1_continue.addEventListener('click', get_device_info)