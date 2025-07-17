// Select the "Add item" div
const addItemDiv = document.getElementById('add_item');

// Select the <ul> with class "my_list"
const myList = document.querySelector('ul.my_list');

// Add click event listener to the "Add item" div
addItemDiv.addEventListener('click', () => {
  // Create a new <li> element
  const newItem = document.createElement('li');
  // Set its text content to "Item"
  newItem.textContent = 'Item';
  // Append the new <li> to the list
  myList.appendChild(newItem);
});

