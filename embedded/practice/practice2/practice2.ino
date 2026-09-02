void setup() { // 시작과 동시에 한 번만 실행, 주로 아두이노에서 몇 번 핀을 어떤 용도로 사용할 것인지를 작성
  // put your setup code here, to run once:
  pinMode(13, OUTPUT); // 13번 pin(내장 LED)을 출력 지정
}

void loop() { // 포함하는 코드를 무한히 반복 실행 (while(1)과)
  // put your main code here, to run repeatedly:
  for(int=1; i<=5; i++){
    digitalWrite(13, HIGH); // turn the LED on (HIGH is the voltage level)
    delay(i*1000); // wait for a i*1000 sec
    degitalWrite(13, LOW); // turn the LED off by making the voltage LOW
    delay(i*1000); // wait for a i*1000 sec
  }
}
