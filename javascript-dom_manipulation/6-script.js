// Select the element with id 'character'
const characterDiv = document.getElementById('character');

// Fetch data from the API
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json()) // Parse the JSON from the response
  .then(data => {
    // Update the div content with the character name
    characterDiv.textContent = data.name;
  })
  .catch(error => {
    // Handle any errors
    characterDiv.textContent = 'Error loading character';
    console.error('Error fetching data:', error);
  });

