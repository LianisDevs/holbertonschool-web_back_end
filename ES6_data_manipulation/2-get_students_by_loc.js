export default function getStudentsByLocation(studentsArray, city) {
  if (Array.isArray(studentsArray) !== true) return [];

  const result = studentsArray.filter((student) => student.location === city);
  return result;
}
