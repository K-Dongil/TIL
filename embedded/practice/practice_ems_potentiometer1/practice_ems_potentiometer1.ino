// 가변 저항값(가속페달 입력) 변화에 따른 엔진음 변화
// Easy module Shield의 가변저항을 차량의 가속페달이라고 가정한다. 가변저항의 위치에 따라 부저의 소리가 변하도록 프로그램을 작성
// 1. 가변저항(A0)의 값을 읽는다.
// 2. 가변저항 값이 작을수록 낮은 음이 천천히 반복된다.
// 3. 가변저항 값이 클수록 높은 음이 빠르게 반복된다.
// 4. 부저는 D5를 사용한다.

void setup() {
  // put your setup code here, to run once:
  pinMode(A0, INPUT);
  pinMode(5, OUTPUT); // 부저 핀을 출력 모드로 설정
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int value = analogRead(A0);

  int frequency = map(value, 0, 1023, 300, 2000);
  int interval = map(value, 0, 1023, 800, 100); // 간격
  
  tone(5, frequency, 50); // 5번 pin, 낼 소리의 높낮이(주파수, Hz), 소리를 켜두는 시간
  delay(100);
  noTone(5);
  delay(interval);
}
