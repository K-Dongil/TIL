void setup() { // 시작과 동시에 한 번만 실행, 주로 아두이노에서 몇 번 핀을 어떤 용도로 사용할 것인지를 작성
  // put your setup code here, to run once:
  Serial.begin(9600); //아두이노가 컴퓨터와 데이터를 주고받을 수 있도록 '통신 통로를 열고 속도를 맞추는' 코드
}

void loop() { // 포함하는 코드를 무한히 반복 실행 (while(1)과)
  // put your main code here, to run repeatedly:
  for(int i=0; i<5; i++){
    Serial.print(i);
    Serial.println("번째"); //Serial.println("%d", i);같이 서식 지정자 불가능
    Serial.println("Hello PC!"); // 줄 바꿔서 출력, 1초당 Hello PC!라는 메세지가 시리얼 모니터에 출력됨
    delay(1000); // put your main code here, to run repeatedly;
  }
}
