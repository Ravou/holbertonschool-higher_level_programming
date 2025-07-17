// Select the header element
const header = document.querySelector('header');

// Select the element with id 'update_header'
const updateHeaderDiv = document.getElementById('update_header');

// Add click event listener on the update_header element
updateHeaderDiv.addEventListener('click', () => {
  // Change the text content of the header
  header.textContent = 'New Header!!!';
});

