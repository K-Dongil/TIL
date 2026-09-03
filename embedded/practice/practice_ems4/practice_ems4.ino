void setup() {
  // put your setup code here, to run once:
  pinMode(2, INPUT); // 2번 핀을 입력핀으로 설정
  Serial.begin(9600); // PC와 아두이노 사이 통신 설정
}

void loop() {
  // put your main code here, to run repeatedly:
  int value = digitalRead(2); // 2번 핀 전압을 value에 저
  Serial.println(value); // 아두이노 우노 - easy module shield 에서는 눌렀을 때 0 => Pull up // value 값을 시리얼 모니터에 출력
  delay(1000); // 1초 대기
}
