#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id + '/';

function getCharacterName (charUrl) {
  return new Promise(function (resolve, reject) {
    request(charUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
}

async function printCharacters () {
  const resp = await new Promise(function (resolve, reject) {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });

  const film = JSON.parse(resp);
  const characters = film.characters;

  for (let i = 0; i < characters.length; i++) {
    const charUrl = characters[i];
    try {
      const name = await getCharacterName(charUrl);
      console.log(name);
    } catch (error) {
      console.log(error);
    }
  }
}

printCharacters();
