#!/usr/bin/env node

const fs = require("fs");

const args = process.argv.slice(2);

const dir = args[0] || ".";

const entries = fs.readdirSync(dir);

for (const entry of entries) {
  console.log(entry);
}
