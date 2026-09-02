void setup() { // 시작과 동시에 한 번만 실행, 주로 아두이노에서 몇 번 핀을 어떤 용도로 사용할 것인지를 작성
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  Serial.begin(9600);

  digitalWrite(13, LOW); // 시작할 때 LED 끄게 만들기 위해서
  Serial.println("1 : LED ON");
  Serial.println("0 : LED OFF");
}

void loop() { // 포함하는 코드를 무한히 반복 실행 (while(1)과)
  // put your main code here, to run repeatedly:
  // 입력된 문자 하나를 읽음
  if(Serial.available() > 0){
    char command = Serial.read();

    //줄바꿈 문자는 무시
    if (command == '\n' || command == '\r'){
      return;
    }
    
    if (command == '1'){ // 1이 입력되면 LED ON
      digitalWrite(13, HIGH);
      Serial.println("LED ON");
    }else if (command ='0'){ // 0이 입력되면 LED OFF
      digitalWrite(13, LOW);
      Serial.println("LED OFF");
    }else{ // 다른 문자가 입력된 경우
      Serial.println("Invalid Command");
    }
  }
}