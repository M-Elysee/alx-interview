#!/usr/bin/node
// a script that fetch and prints all characters of a Star Wars movie

const request = require('request');
let id = process.argv[2];

if (!id) {
  console.log('Usage: node 0-starwars_characters.js <id>');
  process.exit(1);
}

try {
  id = parseInt(id);
  if (!Number.isInteger(id)) {
    throw new Error();
  }
} catch (error) {
  console.log('Please provide an interger id');
  process.exit(1);
}

request({
  method: 'GET',
  uri: `https://swapi-api.alx-tools.com/api/films/${id}`
},
function (error, response, body) {
  if (error) {
    return console.error('oh no', error);
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
        console.error('hello', error);
      } else if (response && response.statusCode === 200) {
        const name = JSON.parse(body).name;
        console.log(name);
      }
    });
  }
}
