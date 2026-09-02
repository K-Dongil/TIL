void setup() { // 시작과 동시에 한 번만 실행, 주로 아두이노에서 몇 번 핀을 어떤 용도로 사용할 것인지를 작성
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop() { // 포함하는 코드를 무한히 반복 실행 (while(1)과 같음)
  // put your main code here, to run repeatedly:
  // 입력된 문자 하나를 읽음
  if(0 < Serial.available()){
    int idx = Serial.parseInt();

    for (int i=0; i<idx; i++){
      Serial.print(i);
      Serial.println("번째");
      digitalWrite(13, HIGH);
      delay(3000);
      digitalWrite(13, LOW);
      delay(1000);
    }
  }else{
    Serial.println("Please Enter a positive number");
  }
}