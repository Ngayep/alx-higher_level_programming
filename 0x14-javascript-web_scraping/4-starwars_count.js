#!/usr/bin/node

const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];
const characterId = 18; // Wedge Antilles character ID

// Fetch data from the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const films = JSON.parse(body).results;
    let count = 0;

    // Iterate through each film
    films.forEach(film => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        count++;
      }
    });

    console.log(count);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
