#!/usr/bin/env node
/**
 * Security reminder wrapper for run-with-flags compatibility.
 *
 * The original hook logic lives in security-reminder.py. This wrapper keeps
 * the hook on the approved Node-based execution path while preserving the
 * existing Python implementation.
 */

'use strict';

const path = require('path');
const { spawnSync } = require('child_process');

const MAX_STDIN = 1024 * 1024;

let raw = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', chunk => {
  if (raw.length < MAX_STDIN) {
    raw += chunk.substring(0, MAX_STDIN - raw.length);
  }
});

process.stdin.on('end', () => {
  const scriptPath = path.join(__dirname, 'security-reminder.py');
  const pythonCandidates = ['python3', 'python'];
  let result;

  for (const pythonBin of pythonCandidates) {
    result = spawnSync(pythonBin, [scriptPath], {
      input: raw,
      encoding: 'utf8',
      env: process.env,
      cwd: process.cwd(),
      timeout: 5000,
    });

    if (result.error && result.error.code === 'ENOENT') {
      continue;
    }
    break;
  }

  if (!result || (result.error && result.error.code === 'ENOENT')) {
    process.stderr.write('[SecurityReminder] python3/python not found. Skipping security reminder hook.\n');
    process.stdout.write(raw);
    process.exit(0);
  }

  if (result.error) {
    process.stderr.write(`[SecurityReminder] Hook failed to run: ${result.error.message}\n`);
    process.stdout.write(raw);
    process.exit(0);
  }

  if (result.stdout) process.stdout.write(result.stdout);
  if (result.stderr) process.stderr.write(result.stderr);

  process.exit(Number.isInteger(result.status) ? result.status : 0);
});
