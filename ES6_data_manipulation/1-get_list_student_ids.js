export default function getListStudentIds(studentsArray) {
  if (Array.isArray(studentsArray) !== true) return [];
  return studentsArray.map((student) => student.id);
}
