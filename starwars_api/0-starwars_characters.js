#!/usr/bin/env node

const request = require('request');



if (process.argv.length !== 3) {
  console.log('Usage: filmNumber');
} else {
  const filmn = process.argv[2];
  if (!/^[1-6]$/.test(filmn)) {
    console.log("The film doesn't exist");
  } else {
    request('https://swapi-api.hbtn.io/api/films/' + filmn, function (error, response, body) {
      if (error) {
        console.error('error:', error);
		return;
      }
      const film = JSON.parse(body);

      film.characters.forEach((url) => {
        request(url, (err, res, body) => {
          if (err) return console.error(err);
          console.log(JSON.parse(body).name);
        });
      });
    });
  }
}
