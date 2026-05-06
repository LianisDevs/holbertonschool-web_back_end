let input = '';

console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('data', (data) => {
  input += data.toString();

  if (process.stdin.isTTY) {
    const name = input.trim();
    if (name.length > 0) {
      process.stdout.write(`Your name is: ${name}\r`);
    }
  }
});

process.stdin.on('end', () => {
  const name = input.trim();
  if (name.length > 0) {
    process.stdout.write(`Your name is: ${name}\n`);
  }
  process.stdout.write('This important software is now closing\n');
});

process.on('SIGINT', () => {
  process.stdout.write('This important software is now closing\n');
  process.exit(0);
});
