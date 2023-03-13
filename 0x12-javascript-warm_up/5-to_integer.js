#!/usr/bin/node

if (isNaN(Math.trunc(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Math.trunc(process.argv[2]));
}
