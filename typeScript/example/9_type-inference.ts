// 타입 추론 기본 1
const a = 'a';

function logA(b = 'a') {
  const c = 10;
  return b + c;
}

// 타입 추론 기본 2
interface Dropdown<T> {
  value: T
  title: string;
}
const items: Dropdown<number> = {
  value: 10,
  title: 'a'
}

interface DetailedDropdown<K> extends Dropdown<K> {
  description: string;
  tag: K;
}
const detailItems: DetailedDropdown<number> = {
  value: 5,
  title: 'a',
  description: 'b',
  tag: 5
}

// Best Common Type
const arr = [0, 1, true]; // arr의 타입은 (number | boolean)[]이 된다