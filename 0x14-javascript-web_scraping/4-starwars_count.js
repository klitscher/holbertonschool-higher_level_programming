#!/usr/bin/node
const request = require('request');
let url = process.argv[2];
url = 'http://swapi.co/api/people/18';
request(url, function (error, response, body) {
  if (error) { return; }
  console.log(JSON.parse(body).films.length);
});
