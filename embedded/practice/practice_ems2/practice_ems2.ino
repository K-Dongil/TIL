const int RED_LED = 12; // 이지모듈쉴드에서 빨간색 LED가 12번 pin에 연결
const int BLUE_LED = 13;
int count = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(RED_LED, OUTPUT);
  pinMode(BLUE_LED, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  // 5번 반복
  if (count == 5){
    return 0;
  }else{
    count++ ;
  }

  // 발간색 LED 켜기
  digitalWrite(RED_LED, HIGH);
  delay(1000);

  // 빨간색 LED 끄기
  digitalWrite(RED_LED, LOW);
  delay(1000);

  // 파란색 LED 켜기
  digitalWrite(BLUE_LED, HIGH);
  delay(1000);

  // 파란색 LED 끄기
  digitalWrite(BLUE_LED, LOW);
  delay(1000);
}
