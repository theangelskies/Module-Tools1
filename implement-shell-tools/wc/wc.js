#!/usr/bin/env node

const fs = require("fs");

const files = process.argv.slice(2);

if (files.length === 0) {
  console.error("Usage: wc <file...>");
  process.exit(1);
}

let totalLines = 0;
let totalWords = 0;
let totalBytes = 0;

for (const file of files) {
  const content = fs.readFileSync(file, "utf8");

  const lines = content.split("\n").length;
  const words = content.trim().split(/\s+/).filter(Boolean).length;
  const bytes = Buffer.byteLength(content, "utf8");

  console.log(lines, words, bytes, file);

  totalLines += lines;
  totalWords += words;
  totalBytes += bytes;
}

if (files.length > 1) {
  console.log(totalLines, totalWords, totalBytes, "total");
}
