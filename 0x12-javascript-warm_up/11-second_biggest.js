#!/usr/bin/node

const { argv } = process;

if (argv.length <= 3) {
  console.log(0);
} else {
  const argLen = argv.length;
  let biggest = 0;
  let secondBiggest = 0;

  for (let i = 2; i < argLen; i++) {
    const num = Number(argv[i]);

    if (!isNaN(num)) {
      if (num > biggest) {
        secondBiggest = biggest;
        biggest = num;
      } else if (num > secondBiggest && num !== biggest) {
        secondBiggest = num;
      }
    }
  }
  console.log(secondBiggest);
}
