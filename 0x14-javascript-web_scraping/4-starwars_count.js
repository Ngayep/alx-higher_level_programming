#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const wedgeId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const data = JSON.parse(body);
    const films = data.results; // The results contain the list of movies
    let count = 0;

    films.forEach(film => {
      if (film.characters.some(character => character.endsWith(wedgeId))) {
        count++;
      }
    });

    console.log(count);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
