#!/usr/bin/node
// A script that sends GET request and stores in a file

const request = require('request');
const fs = require('fs');
const filepath = process.argv[3];
const url = process.argv[2];

require(url, (err, res, body) => {
  if (err) console.error(err);
  fs.writeFile(filepath, body, err => {
    if (err) console.error(err);
  });
});
