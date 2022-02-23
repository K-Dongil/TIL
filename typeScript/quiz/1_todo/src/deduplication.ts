// 스펙 : 구체적인 타입
// 타입에 이름을 부여 : 타입별칭
type Todo1 = {
  id: number;
  title: string;
  done: boolean;
}

// interface
interface Todo {
  id: number;
  title: string;
  done: boolean
}

let todoItems1: Todo[];

// api
function fetchTodoItems(): Todo[] {
  const todos: Todo[] = [
    { id: 1, title: '안녕', done: false },
    { id: 2, title: '타입', done: false },
    { id: 3, title: '스크립트', done: false },
  ];
  return todos;
}

// crud methods
function fetchTodos(): object[] {
  const todos: object[] = fetchTodoItems();
  return todos;
}

function addTodo(todo: Todo): void {
  todoItems1.push(todo);
}

function deleteTodo(index: number): void {
  todoItems1.splice(index, 1);
}

function completeTodo(index: number, todo: Todo): void {
  todo.done = true;
  todoItems1.splice(index, 1, todo);
}

// business logic
function logFirstTodo(): object {
  return todoItems1[0];
}

function showCompleted(): object[] {
  return todoItems1.filter(item => item.done);
}

// TODO: 아래 함수의 내용을 채워보세요. 아래 함수는 `addTodo()` 함수를 이용하여 2개의 새 할 일을 추가하는 함수입니다.
function addTwoTodoItems(): void {
  // addTodo() 함수를 두 번 호출하여 todoItems에 새 할 일이 2개 추가되어야 합니다.
  const item1: Todo = {
    id: 4,
    title: "item1",
    done: false
  }
  const item2: Todo = {
    id: 5,
    title: "item2",
    done: false
  }
  addTodo(item1);
  addTodo(item2);
}

// NOTE: 유틸 함수
function log(): void {
  console.log(todoItems1);
}

todoItems1 = fetchTodoItems();
addTwoTodoItems();
log();