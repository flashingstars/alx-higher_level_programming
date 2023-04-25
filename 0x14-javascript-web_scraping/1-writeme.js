#!/usr/bin/node
// A script to write to a file

const fs = require('fs');
const filepath = process.argv[2];
const content = process.argv[3];
fs.writeFile(filepath, content, err => {
  if (err) {
    console.error(err);
  }
});
