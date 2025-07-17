// Select the header element
cont header = document.querySelector('header');

// Select the element with id 'red_header'
const div = document.querySelector('red_header');

// Add a click event listener to the 'red_header' element
redHeader.addEventListener('click', () => {
	header.style.color = '#FF0000'
});
