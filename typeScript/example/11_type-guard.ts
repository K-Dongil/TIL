interface Developer{
  name: string;
  skill: string;
}

interface Person {
  name: string;
  age: number;
}

function introduce(): Developer | Person{
  return { name: 'Dongil', age: 27, skill: 'King'}
}

const dongil = introduce();
// console.log(dongil.skill) // error

// 타입의 범위를 줄여나간다, 타입을 구체화시키는 것
if ((dongil as Developer).skill){
  const skill = (dongil as Developer).skill;
  console.log(skill);
}else if ((dongil as Person).age) {
  const age = (dongil as Person).age;
  console.log(age);
}

const dongil1 = introduce() as Developer;
console.log(dongil1.skill)

const dongil2 = introduce() as Person;
console.log(dongil2.age)

// 타입가드
function isDeveloper(target: Developer | Person): target is Developer{
  return (target as Developer).skill !== undefined;
}

if (isDeveloper(dongil)) {
  console.log(dongil.skill)
}else{
  console.log(dongil.age)
}