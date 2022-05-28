const emails: {value: string, selected: boolean}[] = [
  { value: 'naver.com', selected: true },
  { value: 'gmail.com', selected: false },
  { value: 'hanmail.net', selected: false },
];

const numberOfProducts: {value: number, selected: boolean}[] = [
  { value: 1, selected: true },
  { value: 2, selected: false },
  { value: 3, selected: false },
];

function createDropdownItem(item: {value: string, selected: boolean}) {
  const option = document.createElement('option');
  option.value = item.value.toString();
  option.innerText = item.value.toString();
  option.selected = item.selected;
  return option;
}

// NOTE: 이메일 드롭 다운 아이템 추가
emails.forEach(function (email) {
  const item = createDropdownItem(email);
  const selectTag = document.querySelector('#email-dropdown');
  selectTag.appendChild(item);
});


// interface 사용
interface Email {
  value: string;
  selected: boolean;
}

interface ProductNumber {
  value: number;
  selected: boolean;
}

const emails_interface: Email[] = [
  { value: 'naver.com', selected: true },
  { value: 'gmail.com', selected: false },
  { value: 'hanmail.net', selected: false },
];

const numberOfProducts_interface: ProductNumber[] = [
  { value: 1, selected: true },
  { value: 2, selected: false },
  { value: 3, selected: false },
];

function createDropdownItem_interface(item: Email | ProductNumber) {
  const option = document.createElement('option');
  option.value = item.value.toString();
  option.innerText = item.value.toString();
  option.selected = item.selected;
  return option;
}

// NOTE: 드롭 다운 아이템 추가
emails_interface.forEach(function (email) {
  const item = createDropdownItem_interface(email);
  const selectTag = document.querySelector('#email-dropdown');
  selectTag.appendChild(item);
});

numberOfProducts_interface.forEach(function (product) {
  const item = createDropdownItem_generic<number>(product);
  const selectTag = document.querySelector('#product-dropdown');
  selectTag.appendChild(item);
});

// generic 사용
interface Dropdown<T> {
  value: T;
  selected: boolean;
}

const emails_generic: Dropdown<string>[] = [
  { value: 'naver.com', selected: true },
  { value: 'gmail.com', selected: false },
  { value: 'hanmail.net', selected: false },
];

const numberOfProducts_generic: Dropdown<number>[] = [
  { value: 1, selected: true },
  { value: 2, selected: false },
  { value: 3, selected: false },
];

function createDropdownItem_generic<T>(item: Dropdown<T>) {
  const option = document.createElement('option');
  option.value = item.value.toString();
  option.innerText = item.value.toString();
  option.selected = item.selected;
  return option;
}

// NOTE: 드롭 다운 아이템 추가
emails_generic.forEach(function (email) {
  const item = createDropdownItem_generic<string>(email);
  const selectTag = document.querySelector('#email-dropdown');
  selectTag.appendChild(item);
});

numberOfProducts_generic.forEach(function (product) {
  const item = createDropdownItem_generic<number>(product);
  const selectTag = document.querySelector('#product-dropdown');
  selectTag.appendChild(item);
});