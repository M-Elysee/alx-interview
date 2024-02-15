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
      fetchCharacters(characters);
    }
  });

  async function fetchCharacters (characters) {
    for (const character of characters) {
      try {
        const name = await getCharacterName(character);
        console.log(name);
      } catch (error) {
        console.errot(error);
      }
    }
  }

  function getCharacterName (character) {
    return new Promise((resolve, reject) => {
      request({
        method: 'GET',
        uri: character
      }, (error, response, body) => {
        if (error) {
          reject(error);
        } else if (response && response.statusCode === 200) {
          const name = JSON.parse(body).name;
          resolve(name);
        }
      });
    });
  }
}
