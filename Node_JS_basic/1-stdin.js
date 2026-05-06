console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('data', (data) => {
  const name = data.toString().trim();
  process.stdout.write(`Your name is: ${name}\r`);
});

process.on('SIGINT', () => {
  process.stdout.write('This important software is now closing\n');
  process.exit(0);
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
