// 주위 밝기에 따른 차량 경고음 변화
// Easy module의 조도센서와 부저를 이용하여 주변 밝기에 따라 서로 다른 높이의 소리가 발생하도록 프로그램을 작성하시오.
// 1. 조도센서는 A1을 이용하여 주변밝기를 측정한다. 사용한다.
// 2. 조도센서의 측정값을 부저의 주파수 값으로 변환한다
// 3. 주변이 어두울수록 낮은 음이 발생하도록 한다.
// 4. 주변이 밝을수록 높은 음이 발생하도록 한다.
// 5. 부저는 D5를 사용한다.
// 실습 환경의 조도센서 측정 범위(예시이며, 상황에 따라 다르게 세팅)
// - 어두움 : 약 50, - 밝음 : 약 300
// 부저 주파수 범위 : 300Hz ~ 2000 Hz
void setup() {
  // put your setup code here, to run once:
    pinMode(A1, INPUT); // 조도센서
    pinMode(5, OUTPUT); // 부저 핀을 출력 모드로 설정
}


void loop() {
  // put your main code here, to run repeatedly:
  int vin = analogRead(A1); // 조도센서 50~300
  int val = map(vin, 0, 1023, 262, 1047);

  val = constrain(val, 262, 1047);

  tone(5, val, 100);
  delay(500);
  noTone(5);
  delay(500);
}
