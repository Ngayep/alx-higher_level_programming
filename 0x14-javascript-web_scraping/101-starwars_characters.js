#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the URL to fetch the movie details
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a request to the Star Wars API to get the movie details
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  // Parse the response body
  const film = JSON.parse(body);
  const characters = film.characters;

  // For each character URL, make a request to get the character details
  characters.forEach(characterUrl => {
    request(characterUrl, (err, res, body) => {
      if (err) {
        console.error(err);
        return;
      }

      // Parse the character details and print the character's name
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
