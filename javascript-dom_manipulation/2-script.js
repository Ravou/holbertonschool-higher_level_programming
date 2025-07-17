// Select the header element
const header = document.querySelector('header');
// Select the element with id 'red_header'
const redHeaderDiv = document.getElementById('red_header');

// add a click event listener on the 'red_header' element
redHeaderDiv.addEventListener('click', () => {
	// When clicked, add the 'red' class to the <header> element
	header.classList.add('red');
});

