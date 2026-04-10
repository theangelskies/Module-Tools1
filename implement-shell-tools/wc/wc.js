#!/usr/bin/env node

const fs = require("fs");

const args = process.argv.slice(2);

if (args.length !== 1) {
  console.error("Usage: wc <file>");
  process.exit(1);
}

const file = args[0];

const content = fs.readFileSync(file, "utf8");

const lines = content.split("\n").length;
const words = content.trim().split(/\s+/).filter(Boolean).length;
const bytes = Buffer.byteLength(content, "utf8");

console.log(lines, words, bytes);
