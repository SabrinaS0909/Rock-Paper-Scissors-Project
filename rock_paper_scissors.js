
// Eventually see if there is a more condensed way to do the same thing, like maybe if statements so if someone clicks the bee button, they get the bee specific one, and an f statement to make it more general
document.getElementById('beeButton').addEventListener('click', function() {
    console.log('You clicked the bee!');
    fetch('/button_click', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => console.log(data.message));

});
document.getElementById('bunButton').addEventListener('click', function() {
    console.log('You clicked the bun!');
    fetch('/button_click', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => console.log(data.message));

});
document.getElementById('corvidButton').addEventListener('click', function() {
    console.log('You clicked the corvid!');
    fetch('/button_click', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => console.log(data.message));

});
document.getElementById('catButton').addEventListener('click', function() {
    console.log('You clicked the cat!');
    fetch('/button_click', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => console.log(data.message));

});
document.getElementById('wolfButton').addEventListener('click', function() {
    console.log('You clicked the wolf!');
    fetch('/button_click', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => console.log(data.message));

});
document.getElementById('humanButton').addEventListener('click', function() {
    console.log('You clicked the human!');
    fetch('/button_click', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => console.log(data.message));

});

//The above works! But I think there's an issue with it translating over to Python.
//Ask Gemini about the error messages you're getting 