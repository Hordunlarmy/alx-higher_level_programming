#!/usr/bin/node
// a script that concats 2 files.

const fs = require('fs');

const { argv } = process;
const [fileA, fileB, fileC] = [argv[2], argv[3], argv[4]];

if (
  fs.existsSync(fileA) &&
fs.statSync(fileA).isFile &&
fs.existsSync(fileB) &&
fs.statSync(fileB).isFile &&
fileC !== undefined
) {
  const fileAContent = fs.readFileSync(fileA);
  const fileBContent = fs.readFileSync(fileB);
  const stream = fs.createWriteStream(fileC);

  stream.write(fileAContent);
  stream.write(fileBContent);
  stream.end();
}
