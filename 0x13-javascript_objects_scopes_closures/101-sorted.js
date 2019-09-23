#!/usr/bin/node

const dict = require('./101-data').dict;

const values = [...new Set(Object.keys(dict).map(function (key) { return dict[key]; }))];
const keys = Object.keys(dict);
const newDict = {};

for (let i = 0; i < values.length; i++) {
  newDict[values[i]] = keys.map(function (x) { if (dict[x] === values[i]) { return (x); } }).filter(Boolean);
}

console.log(newDict);
