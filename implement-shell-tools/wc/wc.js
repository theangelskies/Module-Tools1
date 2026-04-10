#!/usr/bin/env node

const fs = require("fs");

const args = process.argv.slice(2);

let showLines = false;
let showWords = false;
let showBytes = false;

const files = [];

for (const arg of args) {
  if (arg === "-l") {
    showLines = true;
  } else if (arg === "-w") {
    showWords = true;
  } else if (arg === "-c") {
    showBytes = true;
  } else {
    files.push(arg);
  }
}

if (!showLines && !showWords && !showBytes) {
  showLines = showWords = showBytes = true;
}

for (const file of files) {
  const content = fs.readFileSync(file, "utf8");

  const lines = content.split("\n").length;
  const words = content.trim().split(/\s+/).filter(Boolean).length;
  const bytes = Buffer.byteLength(content, "utf8");

  let output = [];

  if (showLines) output.push(lines);
  if (showWords) output.push(words);
  if (showBytes) output.push(bytes);

  output.push(file);

  console.log(output.join(" "));
}
