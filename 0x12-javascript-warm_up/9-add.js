#!/usr/bin/node

function add (a, b) {
  return (Number(a) + Number(b));
}

const { argv } = process;
console.log(add(argv[2], argv[3]));
