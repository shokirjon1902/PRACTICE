/*
TASK F:

Yagona string argumentga ega findDoublers nomli function tuzing
Agar stringda bittadan ortiq bir xil harflar ishtirok etgan bo'lsa
true yokida false natija qaytarsin.

MASALAN: findDoublers("hello"); natija true qaytadi. Sababi ikki marotaba takrorlangan 'll' harfi mavjud!

* */

function findDoublers(a) {
  for (let i = 0; i < a.length; i++) {
    for (let j = 0; j < a.length; i++) {
      if (a[i] === a[j]) {
        return true;
      }
    }
  }
  return false;
}

result = findDoublers("hello");
console.log("result", result);
/*
TASK E: 

Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
MASALAN: getReverse("hello") return qilsin "olleh"

*/

// function getReverse(string) {
//   let result = "";

//   for (let i = string.length - 1; i >= 0; i--) {
//     result += string[i];
//   }

//   return result;
// }

// console.log(getReverse("salom"));
