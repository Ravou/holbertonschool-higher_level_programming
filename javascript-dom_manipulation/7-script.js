// Select the <ul> element with id 'list_movies'
const listMovies = document.getElementById('list_movies');

// Fetch the list of films from the API
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())          // Parse JSON response
  .then(data => {
    // For each movie in the results array
    data.results.forEach(movie => {
      // Create a new <li> element
      const li = document.createElement('li');
      // Set the text to the movie title
      li.textContent = movie.title;
      // Append the <li> to the list
      listMovies.appendChild(li);
    });
  })
  .catch(error => console.error('Error:', error));

