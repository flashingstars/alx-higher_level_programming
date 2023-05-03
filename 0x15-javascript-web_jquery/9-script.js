$(document).ready(()=>{
    const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
    let response = null;

    $.ajax({
        url: url,
        method: 'GET',
        async: false,
        success: (data) => {
            response = data.hello;
        },
        error: ()=>{
            response = 'Error fetching data';
        }
    });
    if (response){
        $('#hello').text(response);
    }
});