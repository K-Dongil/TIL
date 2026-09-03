void setup() {
  // put your setup code here, to run once:
  // analog
  pinMode(11, OUTPUT); // 아날로그 출력 범위는 0~255 (0V ~ 5V)
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i=0; i<=255; i++){
    analogWrite(11, i);
    delay(100);
  }

  analogWrite(11, 0);
  delay(2000);

  for(int i=255; 0<=i; i--){
    analogWrite(11, i);
    delay(100);
  }
}
