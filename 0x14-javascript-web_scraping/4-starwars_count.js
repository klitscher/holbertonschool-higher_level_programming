#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) { return; }
  let count = 0;
  const results = JSON.parse(body).results;
  for (const film of results) {
    for (const chara of film.characters) {
      if (chara.includes('/18') || chara.includes('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
