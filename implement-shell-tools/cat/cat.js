#!/usr/bin/env node

const fs = require("fs");

let args = process.argv.slice(2);

let numberAll = false;
let numberNonEmpty = false;

// Parse flags
if (args[0] === "-n") {
  numberAll = true;
  args.shift();
} else if (args[0] === "-b") {
  numberNonEmpty = true;
  args.shift();
}

const files = args;

let lineNumber = 1;

for (const file of files) {
  const content = fs.readFileSync(file, "utf8");

  if (!numberAll && !numberNonEmpty) {
    process.stdout.write(content);
  } else {
    const lines = content.split("\n");

    for (const line of lines) {
      if (numberAll) {
        process.stdout.write(`${String(lineNumber).padStart(6)}  ${line}\n`);
        lineNumber++;
      } else if (numberNonEmpty) {
        if (line.trim() !== "") {
          process.stdout.write(`${String(lineNumber).padStart(6)}  ${line}\n`);
          lineNumber++;
        } else {
          process.stdout.write("\n");
        }
      }
    }
  }
}
