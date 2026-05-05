process.stdout.write('Welcome to Holberton School, what is your name?\n');

let data = '';

process.stdin.setEncoding('utf8');

process.stdin.on('data', (chunk) => {
  data += chunk;
});

process.stdin.on('end', () => {
  const name = data.trim();
  process.stdout.write(`Your name is: ${name}\n`);
  process.stdout.write('This important software is now closing\n');
});
