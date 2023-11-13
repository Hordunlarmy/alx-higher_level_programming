#!/usr/bin/node

const { argv } = process;

if (argv[2] && typeof argv[2] !== 'number') {
  if (!isNaN(argv[2])) {
    console.log('My number: ' + Math.floor(argv[2]));
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
