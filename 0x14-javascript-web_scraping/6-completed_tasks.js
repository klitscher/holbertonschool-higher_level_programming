#!/usr/bin/node
const request = require('request');
const idList = [];
let idSet;
const newObj = {};
request(process.argv[2], function (error, response, body) {
  if (error) {}
  const list = JSON.parse(body);
  for (let i = 0; i < list.length; i++) {
    if (!(list[i].userId in idList)) {
      idList.push(list[i].userId);
    }
  }
  idSet = [...new Set(idList)];
  for (let i = 0; i < idSet.length; i++) {
    newObj[idSet[i]] = (function (list, id) {
      let count = 0;
      for (let j = 0; j < list.length; j++) {
        if (id === list[j].userId && list[j].completed === true) {
          count++;
        }
      }
      return count;
    })(list, idSet[i]);
  }
  console.log(newObj);
});
