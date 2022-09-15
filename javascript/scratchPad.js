const userRegex = /^[\w]{6,8}$/i;
console.log(userRegex.test("Muzi1234"));
console.log(userRegex.test("Muzi12444444434"));
// console.log(userRegex.search("Muzi1234"));

emailPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/

console.log(emailPattern.test("muzi123@Gmail.com"));
console.log(emailPattern.test("muzi.xaba@Gmail.co.za"));

