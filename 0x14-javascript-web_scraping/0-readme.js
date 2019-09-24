#!/usr/bin/node

const fs = require('fs');

try {
  const content = fs.readFileSync(process.argv[2], 'utf8', function (err, result) { if (err) console.log(err); });
  console.log(content);
} catch (err) {
  console.log(err);
}
