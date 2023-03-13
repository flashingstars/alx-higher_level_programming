#!/usr/bin/node

const arg1 = process.argv[2];
if (parseInt(arg1)) {
  console.log('My number: <first argument converted in integer>');
} else {
  console.log('Not a number');
}
