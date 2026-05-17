const fs = require('node:fs');

module.exports = function countStudents(filePath) {
  try {
    const data = fs.readFileSync(filePath, 'utf8');

    const lines = data.split('\n').map((row) => row.split(','));

    const students = lines.slice(1);

    const csList = [];
    const sweList = [];

    for (const innerArray of students) {
      const last = innerArray[innerArray.length - 1];

      if (last === 'CS') {
        csList.push(innerArray[0]);
      }
      if (last === 'SWE') {
        sweList.push(innerArray[0]);
      }
    }

    console.log('Number of students:', students.length);
    console.log(`Number of students in CS: ${csList.length}. List: ${csList.join(', ')}`);
    console.log(`Number of students in SWE: ${sweList.length}. List: ${sweList.join(', ')}`);
  } catch (err) {
    console.log('Cannot load the database');
  }
};
