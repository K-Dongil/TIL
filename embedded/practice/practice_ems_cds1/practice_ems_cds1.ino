void setup() {
  // put your setup code here, to run once:
  pinMode(9, OUTPUT); // LED Red 
}

void loop() {
  // put your main code here, to run repeatedly:
  int vin = analogRead(A1); // 조도센서 A1 값 읽기.
  int val = map(vin, 0, 1023, 255, 0); // ADC 값(0~1023)을 PWM 값(255~0)으로 변환
  analogWrite(9,val); // 주변이 어두어질수록 LED를 밝게 제어
                      // 조도센서 주변을 손으로 가림 -> 밝기 감소 -> 조도센서의 저항 증가 -> Vin 감소
}
