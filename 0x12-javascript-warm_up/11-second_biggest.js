#!/usr/bin/node

const { argv } = process;

if (argv.length <= 3) {
  console.log(0);
} else {
  const argLen = argv.length;
  let biggest = 0;
  let secondBiggest = 0;

  for (let i = 0; i < argLen; i++) {
    while (biggest < argv[i]) {
      secondBiggest = biggest;
      biggest = argv[i];
    }
  }
  console.log(secondBiggest);
}
