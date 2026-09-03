// 가변 저항값(가속페달 입력) 변화에 따른 점멸 속도 제어
// Easy module Shield의 가변저항과 RGB LED를 이용하여 가변저항 값에 따라 파란색 LED의 점멸 속도가 변하도록 프로그램을 작성하여라.
// 1. 가변저항(A0)의 값을 읽는다.
// 2. 가변저항 값이 작을 때는 파란색 LED가 천천히 깜빡인다.
// 3. 가변저항 값이 클 때는 빨간색 LED가 빠르게 깜빡인다.
// 4. RGB LED의 Blue는 D11, RED는 D9을 사용한다.
void setup() {
  // put your setup code here, to run once:
  pinMode(A0, INPUT);
  pinMode(9, OUTPUT);
  pinMode(11, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int value = analogRead(A0);

  if (value < 512){
    digitalWrite(9,LOW);
    digitalWrite(11,HIGH);
    delay(1000);
    digitalWrite(11,LOW);
    delay(1000);
  }else{
    digitalWrite(11,LOW);
    digitalWrite(9,HIGH);
    delay(1000);
    digitalWrite(9,LOW);
    delay(1000);
  }
}
