#!/usr/bin/node
const request = require('request');
const fd = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
request(url, function (error, response, body) {
  if (error) {}
  fd.writeFile(filePath, body, 'utf8', (err) => { if (err) {} });
});
