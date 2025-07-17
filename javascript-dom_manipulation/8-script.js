// Wait until the DOM content is fully loaded
document.addEventListener('DOMContentLoaded', () => {
  // Fetch the hello translation in French
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      // Select the element with id 'hello'
      const helloDiv = document.getElementById('hello');
      // Set its text content to the 'hello' value from the response
      helloDiv.textContent = data.hello;
    })
    .catch(error => console.error('Error fetching hello:', error));
});

