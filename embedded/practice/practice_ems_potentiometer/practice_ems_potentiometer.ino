void setup() {
  // put your setup code here, to run once:
  pinMode(A0, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int value = analogRead(A0); // 가변저항을 돌리면 A0의 입력 전압이 0~5V로 변하고, analogRead(A0)는 이를 0~1023의 값으로 변환한다.
  Serial.println(value);
  delay(100);
}
