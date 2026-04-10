#!/usr/bin/env node

const fs = require("fs");

const args = process.argv.slice(2);

let dir = ".";
let onePerLine = false;
let showAll = false;

for (const arg of args) {
  if (arg === "-1") {
    onePerLine = true;
  } else if (arg === "-a") {
    showAll = true;
  } else {
    dir = arg;
  }
}

let entries = fs.readdirSync(dir);
if (!showAll) {
  entries = entries.filter((name) => !name.startsWith("."));
}

for (const entry of entries) {
  if (onePerLine) {
    console.log(entry);
  } else {
    process.stdout.write(entry + "  ");
  }
}

if (!onePerLine) {
  console.log();
}
