"use strict";

function replaceJoke(joke) {
    joke = joke.replace('â', "'")
    $('#joke').html(joke);
}

function newJoke(evt) {
  evt.preventDefault();
    $.get('/generate-joke.json', replaceJoke);
}

$('#new-joke').on('click', newJoke)