void setup() { // 시작과 동시에 한 번만 실행, 주로 아두이노에서 몇 번 핀을 어떤 용도로 사용할 것인지를 작성
  // put your setup code here, to run once:
  pinMode(13, OUTPUT); //pinMode(LED_BUILTIN, OUTPUT); - initialize digital pin LED_BUILTIN as an output
}

void loop() { // 포함하는 코드를 무한히 반복 실행 (while(1)과)
  // put your main code here, to run repeatedly:
  for(int i=1; i<5; i++){
    digitalWrite(13, HIGH); // pinMode(LED_BUILTIN, HIGH); - turn the LED on
    delay(i*1000); // wait for a second
    digitalWrite(13, LOW); // pinMode(LED_BUILTIN, LOW); - turn the LED off by marking the voltage LOW
    delay(i*1000); // wait for a second
  }
}
// 아두이노 IDE에는 매우 중요한 규칙이 있다.
// 메인 .ino 파일의 이름과, 그 파일이 담긴 폴더의 이름이 토씨 하나 안 틀리고 완벽하게 똑같아야 함