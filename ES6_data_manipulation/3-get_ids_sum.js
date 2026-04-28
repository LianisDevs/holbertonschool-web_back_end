export default function getStudentIdsSum(studentsArray) {
  if (Array.isArray(studentsArray) !== true) return 0;

  const result = studentsArray.reduce(
    (accumulator, currentItem) => accumulator + currentItem.id, 0,
  );
  return result;
}
