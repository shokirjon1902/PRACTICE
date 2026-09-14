/* 
TASK G:

Yagona parametrga ega function tuzing.
Va bu function parametr orqalik integer ma'lumot turlariga ega bo'lgan bir arrayni qabul qilsin.
Ushbu function bizga arrayning tarkibidagi birinchi eng katta qiymatning indeksini qaytarsin.

MASALAN: getHighestIndex([5, 21, 12, 21 ,8]); return qiladi 1 sonini
Yuqoridagi misolda, birinchi indeksda 21 joylashgan.
Va bu 21 soni arrayning tarkibidagi birinchi eng katta son hisobladi va bizga uning indeksi 1 qaytadi.

*/

function getHighestIndex(Yagona) {
  let highest = Yagona[0];
  let index = 0;
  for (let i = 1; i < Yagona.length; i++) {
    if (Yagona[i] > highest) {
      highest = Yagona[i];
      index = i;
    }
  }
  return index;
}

console.log(getHighestIndex([5, 21, 12, 26, 8]));

/*
TASK F:

Yagona string argumentga ega findDoublers nomli function tuzing
Agar stringda bittadan ortiq bir xil harflar ishtirok etgan bo'lsa
true yokida false natija qaytarsin.

MASALAN: findDoublers("hello"); natija true qaytadi. Sababi ikki marotaba takrorlangan 'll' harfi mavjud!

* */

// function findDoublers(a) {
//   for (let i = 0; i < a.length; i++) {
//     for (let j = 0; j < a.length; i++) {
//       if (a[i] === a[j]) {
//         return true;
//       }
//     }
//   }
//   return false;
// }

// result = findDoublers("hello");
// console.log("result", result);
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
