#!/usr/bin/env node

const fs = require("fs");

const args = process.argv.slice(2);

let dir = ".";
let onePerLine = false;

// parse arguments
for (const arg of args) {
  if (arg === "-1") {
    onePerLine = true;
  } else {
    dir = arg;
  }
}

const entries = fs.readdirSync(dir);

for (const entry of entries) {
  if (onePerLine) {
    console.log(entry);
  } else {
    process.stdout.write(entry + "  ");
  }
}
