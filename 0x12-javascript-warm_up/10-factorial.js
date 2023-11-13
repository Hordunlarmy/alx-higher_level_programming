#!/usr/bin/node

function fact (num) {
  if (num === 0 || isNaN(num)) {
    return 1;
  }

  return (num * fact(num - 1));
}

const { argv } = process;
console.log(fact(Number(argv[2]), Number(argv[3])));
