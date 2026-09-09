/*
TASK E: 

Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
MASALAN: getReverse("hello") return qilsin "olleh"

*/

function getReverse(string) {
  let result = "";

  for (let i = string.length - 1; i >= 0; i--) {
    result += string[i];
  }

  return result;
}

console.log(getReverse("salom"));
