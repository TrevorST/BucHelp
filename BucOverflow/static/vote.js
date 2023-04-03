function like_function(post_id) {
    var like_button = document.getElementById('like-'+post_id);
    var dislike_button = document.getElementById('dislike-'+post_id);
    var counter_element = document.getElementById('counter-'+post_id);
    let current_counter = parseInt(counter_element.innerText);

    //check if dislike is on(true) or off(false)
    let dislike_state = false
    if (dislike_button.className == "vote_down_on") {
        dislike_state = true
    }
    else {
        dislike_state = false
    }
    //if dislike is checked
    if (dislike_state) {
        current_counter += 2;
        dislike_button.className = 'vote_down_off'
        counter_element.innerText = current_counter
        like_button.className = 'vote_up_on'
    }
    // if dislike is not checked
    else {
        if (like_button.className == 'vote_up_off') {
            like_button.className = "vote_up_on"
            current_counter +=  1;
            counter_element.innerText = current_counter
        }
        else {
            like_button.className = "vote_up_off"
            current_counter +=  -1;
            counter_element.innerText = current_counter
        }
    }
}



function dislike_function(post_id) {
    var like_button = document.getElementById('like-'+post_id);
    var dislike_button = document.getElementById('dislike-'+post_id);
    var counter_element = document.getElementById('counter-'+post_id);
    let current_counter = parseInt(counter_element.innerText);

    //check if like is on(true) or off(false)
    let like_state = false
    if (like_button.className == "vote_up_on") {
        like_state = true
    }
    else {
        like_state = false
    }
    //if like is checked
    if (like_state) {
        current_counter +=  -2;
        like_button.className = 'vote_up_off'
        counter_element.innerText = current_counter
        dislike_button.className = "vote_down_on"
    }
    //if like is not checked
    else {
        if (dislike_button.className == 'vote_down_off') {
            dislike_button.className = "vote_down_on"
            current_counter +=  -1;
            counter_element.innerText = current_counter
        }
        else {
            dislike_button.className = "vote_down_off"
            current_counter +=  1;
            counter_element.innerText = current_counter
        }
    }
}