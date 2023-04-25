#!/usr/bin/node
// A script to show the status code of a GET request

const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) console.error(err);
  console.log('code:', res.statusCode);
});
