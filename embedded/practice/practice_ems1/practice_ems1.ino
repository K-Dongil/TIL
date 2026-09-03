const int RED_LED = 12; // 이지모듈쉴드에서 빨간색 LED가 12번 pin에 연결

void setup() {
  // put your setup code here, to run once:
  pinMode(RED_LED, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  // 발간색 LED 켜기
  digitalWrite(RED_LED, HIGH);
  delay(1000);

  // 빨간색 LED 끄기
  digitalWrite(RED_LED, LOW);
  delay(1000);
}
