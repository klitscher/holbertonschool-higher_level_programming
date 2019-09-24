#!/usr/bin/node
const req = require('request');
req(process.argv[2], function (error, response) {
  if (error) {}
  console.log('code:', response.statusCode);
});
