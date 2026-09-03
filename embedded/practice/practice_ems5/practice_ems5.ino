void setup() {
  // put your setup code here, to run once:
  pinMode(2, INPUT);
  pinMode(12, OUTPUT);
  Serial.begin(9600); // PC와 아두이노 사이 통신 설정
}

void loop() {
  // put your main code here, to run repeatedly:
  int value = digitalRead(2); // 누르면 value가 1 - pull down구조 (수업자료 회로가 pull down, easy module shield는 pull up이였으나 수업자료 회로가 pull down이여서 code를 pull down으로 작성)
 
  if (value == HIGH){
    digitalWrite(12, HIGH); // 누를 때(버튼 누름) 2번 pin이 내부적으로 5V 전원에 연결되어 있어, 전압이 5V가 잡힘, value = 1(HIGH)
    Serial.println(value); // 1
  }else{
    digitalWrite(12, LOW);  // 평소(버튼 안 누름) 버튼을 누르는 순간 2번 pin이 GND(0V) 통로와 직접 연결, 전기는 저항이 없는 곳으로 흐르기 때문에 2번 pin의 전압이 0V로 떨어짐
    Serial.println(value); // 0
  }
}
