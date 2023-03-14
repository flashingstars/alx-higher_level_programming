#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(search => {
    if (search === searchElement) {
      count++;
    }
  });
  return (count);
};
