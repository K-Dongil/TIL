void setup() { // 시작과 동시에 한 번만 실행, 주로 아두이노에서 몇 번 핀을 어떤 용도로 사용할 것인지를 작성
  // put your setup code here, to run once:
  Serial.begin(9600); // 아두이노가 컴퓨터와 데이터를 주고받을 수 있도록 '통신 통로를 열고 속도를 맞추는' 코드
}

void loop() { // 포함하는 코드를 무한히 반복 실행 (while(1)과)
  // put your main code here, to run repeatedly:
  if(Serial.available()){ // 입력이 들어오면, 창고에 데이터가 하나라도 있으면 참(True), Serial.available()은 현재 아두이노의 임시 창고(시리얼 버퍼)에 읽지 않은 데이터가 몇 바이트(몇 글자) 쌓여 있는지 그 '개수'를 알려주는 함수
    char c = Serial.read(); // 컴퓨터가 아두이노로 보낸 데이터 중에서 딱 1글자(1바이트)만 꺼내서 읽는 명령어, 창고에서 데이터를 꺼내는 Serial.read()
    Serial.print("입력 값:");
    Serial.println(c);
    if (c == 'a'){
      Serial.println("c");
    }
  }
}
