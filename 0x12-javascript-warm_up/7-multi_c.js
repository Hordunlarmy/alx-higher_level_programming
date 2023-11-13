#!/usr/bin/node

const { argv } = process;

if (argv[2]) {
  while (argv[2] > 0) {
    console.log('C is fun');
    argv[2]--;
  }
} else { console.log('Missing number of occurrences'); }
