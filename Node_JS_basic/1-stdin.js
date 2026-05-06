let input = '';

console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('data', (data) => {
  input += data.toString();

  if (process.stdin.isTTY) {
    const name = input.trim();
    process.stdout.write(`Your name is: ${name}\n`);
    input = '';
  }
});

process.stdin.on('end', () => {
  if (!process.stdin.isTTY) {
    const name = input.trim();
    console.log(`Your name is: ${name}`);
  }
  console.log('This important software is now closing');
});

process.on('SIGINT', () => {
  process.stdout.write('\n');
  process.stdout.write('This important software is now closing\n');
  process.exit(0);
});
