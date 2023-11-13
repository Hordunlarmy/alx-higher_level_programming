#!/usr/bin/node

const { argv } = process;

if (!isNaN(Number(argv[2]))) {
  let size = Number(argv[2]);

  while (size > 0) {
    console.log('X'.repeat(argv[2]));
    size--;
  }
} else {
  console.log('Missing size');
}
