#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
const nameObj = {};
request(url, function (error, response, body) {
  if (error) { return; }
  let count = 0;
  const charList = JSON.parse(body).characters;
  for (let i = 0; i < charList.length; i++) {
    request(charList[i], function (error, response, body) {
      if (error) { return; }
      const chars = JSON.parse(body);
      nameObj[chars.url] = chars.name;
      count++;
      if (count === charList.length) {
        for (const character of charList) {
          console.log(nameObj[character]);
        }
      }
    });
  }
});
