#!/usr/bin/env node

const fs = require("fs");

let args = process.argv.slice(2);

let numberLines = false;

if (args[0] === "-n") {
  numberLines = true;
  args.shift();
}

const files = args;

let lineNumber = 1;

for (const file of files) {
  const content = fs.readFileSync(file, "utf8");

  if (!numberLines) {
    process.stdout.write(content);
  } else {
    const lines = content.split("\n");

    for (const line of lines) {
      process.stdout.write(`${String(lineNumber).padStart(6)}  ${line}\n`);
      lineNumber++;
    }
  }
}
