void setup() { // 시작과 동시에 한 번만 실행, 주로 아두이노에서 몇 번 핀을 어떤 용도로 사용할 것인지를 작성
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop() { // 포함하는 코드를 무한히 반복 실행 (while(1)과 같음)
  // put your main code here, to run repeatedly:
  int on_time = random(100, 1001);
  int off_time = random(100, 1001);

  Serial.print("LEN ON:");
  Serial.println(on_time);
  Serial.print("LEN OFF:");
  Serial.println(off_time);

  digitalWrite(13, HIGH);
  delay(on_time);

  digitalWrite(13, LOW);
  delay(off_time);

  Serial.println("Loop End");
}