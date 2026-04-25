export default function appendToEachArrayValue(array, appendString) {
  let idx = 0;
  const updatedArray = [];
  for (const value of array) {
    updatedArray[idx] = appendString + value;
    idx += 1;
  }

  return updatedArray;
}
