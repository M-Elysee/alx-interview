#!/usr/bin/node
// a script that fetch and prints all characters of a Star Wars movie

const request = require('request');

if (process.argv.length > 2) {
  const id = process.argv[2];
  request({
    method: 'GET',
    uri: `https://swapi-api.alx-tools.com/api/films/${id}`
  },
  function (error, response, body) {
    if (error) {
      console.error(error);
    } else if (response && response.statusCode === 200) {
      const characters = JSON.parse(body).characters;
      // console.log(characters);
      fetchCharacters(characters);
    }
  });

  function fetchCharacters (characters) {
    for (const character of characters) {
      request({
        method: 'GET',
        uri: `${character}`
      },
      function (error, response, body) {
        if (error) {
          console.error(error);
        } else if (response && response.statusCode === 200) {
          const name = JSON.parse(body).name;
          console.log(name);
        }
      });
    }
  }
}
