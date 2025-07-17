// Select the element
const header = document.querySelector('header');

// Select the element with id "toggle_header"
const toggle = document.getElementById('toggle_header');

// add a click event listener to the toggle_header element
toggle.addEventListener('click' () => {
  // Check the current class of the header
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    // if it's green or anything else, swith to red
    header.classList.remove('green');
    header.classList.add('red');
  }
	
});
