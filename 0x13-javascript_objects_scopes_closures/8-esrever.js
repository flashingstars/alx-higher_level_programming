#!/usr/bin/node

exports.esrever = function (list) {
  const array = [];
  for (let i = 0; i < list.length; i++) {
    array.unshift(list[i]);
  }
  return (array);
};
