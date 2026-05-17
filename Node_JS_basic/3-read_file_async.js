const fs = require('node:fs/promises');

module.exports = async function countStudents(filePath) {
  try {
    const csList = [];
    const sweList = [];

    const data = await fs.readFile(filePath, { encoding: 'utf8' });

    const lines = data.split('\n').map((row) => row.split(','));

    const students = lines.slice(1);

    for (const innerArray of students) {
      const last = innerArray[innerArray.length - 1];

      if (last === 'CS') {
        csList.push(innerArray[0]);
      }
      if (last === 'SWE') {
        sweList.push(innerArray[0]);
      }
    }

    console.log('Number of students:', csList.length + sweList.length);
    console.log(`Number of students in CS: ${csList.length}. List: ${csList.join(', ')}`);
    console.log(`Number of students in SWE: ${sweList.length}. List: ${sweList.join(', ')}`);
  } catch (err) {
    throw new Error('Cannot load the database');
  }
};
