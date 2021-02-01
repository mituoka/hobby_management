
function Change_category(category_name){
    console.log(category_name);

    // csrfToken
	const csrfToken = getCookie('csrftoken');
    // Call Python function
	$.ajax({
	    headers: {'X-CSRFToken': csrfToken},
        url: 'test_ajax_app',
		method: 'POST',
		data: {
			'category_name'       : category_name,
            
        },
		success: function(data) {
            console.log(data.hoge);
            // Success callback
            console.log('==============');
			console.log('成功');
            
			$('#image_list_area').replaceWith(data.html);
		},
		error: function(err) {
            console.log(hoge.hoge);
			// Fail callback
			console.log('失敗');
		}
	});
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
