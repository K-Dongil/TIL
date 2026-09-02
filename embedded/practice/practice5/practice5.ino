void LED_long(); // 모스부호 -
void LED_short(); // 모스부호 .

void setup() { // 시작과 동시에 한 번만 실행, 주로 아두이노에서 몇 번 핀을 어떤 용도로 사용할 것인지를 작성
  // put your setup code here, to run once:
  //내장 기본 LED를 이용해 모스 부호를 빛으로 구현, 자신의 이름 이니셜을 빛으로 켜보기
  pinMode(13, OUTPUT);
}

void loop() { // 포함하는 코드를 무한히 반복 실행 (while(1)과)
  // put your main code here, to run repeatedly:
  // K -.-
  LED_long();
  LED_short();
  LED_long();

  // D -..
  LED_long();
  LED_short();
  LED_short();

  // I ..
  LED_short();
  LED_short();
}

void LED_long(){
  digitalWrite(13, HIGH);
  delay(3000);
  digitalWrite(13, LOW);
  delay(1000);
}

void LED_short(){
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000);
}