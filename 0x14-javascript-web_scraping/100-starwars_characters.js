#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) { return; }
  const charList = JSON.parse(body).characters;
  for (let i = 0; i < charList.length; i++) {
    request(charList[i], function (error, response, body) {
      if (error) { return; }
      console.log(JSON.parse(body).name);
    });
  }
});
