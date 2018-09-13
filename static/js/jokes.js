"use strict";

function replaceJoke(joke) {
    $('#joke').html(joke);
}

function newJoke(evt) {
  evt.preventDefault();
    $.get('/generate-joke.json', replaceJoke);
}

$('#new-joke').on('click', newJoke)