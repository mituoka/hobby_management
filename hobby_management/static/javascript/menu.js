
function Change_category(category_name){
    console.log(category_name);

    // csrfToken
	const csrfToken = getCookie('csrftoken');
    // Call Python function
	$.ajax({
	    headers: {'X-CSRFToken': csrfToken},
        url: 'search_category',
		method: 'POST',
		data: {
			'category_name'       : category_name,   
        },
		success: function(data) {
            // Success callback
			$('#image_list_area').replaceWith(data.html);
		},
		error: function(err) {
			// Fail callback
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

function delete_image(image_id){
    console.log(543534);
    console.log(image_id);

    // csrfToken
	const csrfToken = getCookie('csrftoken');
    // Call Python function
	$.ajax({
	    headers: {'X-CSRFToken': csrfToken},
        url: 'delete_image',
		method: 'POST',
		data: {
			'image_id'       : image_id,   
        },
		success: function(data) {
            // Success callback
            // $('#image_list_area').replaceWith(data.html);
            window.location.reload();
            alert('データを削除しました')
		},
		error: function(err) {
			// Fail callback
		}
	});

}
