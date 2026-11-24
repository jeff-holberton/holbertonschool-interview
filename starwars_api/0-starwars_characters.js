#!/usr/bin/env node

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./script.js filmNumber');
  process.exit(1);
}

const filmNumber = process.argv[2];
if (!/^[1-6]$/.test(filmNumber)) {
  console.log("The film doesn't exist");
  process.exit(1);
}

function get (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) return reject(error);
      if (response.statusCode !== 200) {
        return reject(new Error(`${url} returned ${response.statusCode}`));
      }
      try {
        resolve(JSON.parse(body));
      } catch (parseError) {
        reject(parseError);
      }
    });
  });
}

async function main () {
  const film = await get(`https://swapi-api.hbtn.io/api/films/${filmNumber}/`);
  const characters = await Promise.all(film.characters.map(get));
  characters.forEach((character) => console.log(character.name));
}

main().catch(console.error);
