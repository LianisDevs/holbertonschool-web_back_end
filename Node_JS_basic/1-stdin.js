let input = '';

console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('data', (data) => {
  if (process.stdin.isTTY) {
    const name = data.toString().trim();
    if (name.length > 0) {
      process.stdout.write(`Your name is: ${name}\r`);
    }
  } else {
    input += data.toString();
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
  process.stdout.write('This important software is now closing\n');
  process.exit(0);
});
