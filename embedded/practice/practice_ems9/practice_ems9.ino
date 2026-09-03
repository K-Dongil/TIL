// 모스부호 송신기
// Easy module Shield의 두 개의 버튼으로 모스부호의 점(.)과 선(-)을 입력하고, LED와 시리얼 모니터로 입력한 신호를 확인하는 프로그램을 작성하시오.
// 1. SW1(D2)을 누르면 짧은 신호인 점(.)을 입력한다.
// 2. SW2(D3)을 누르면 짧은 신호인 선(-)을 입력한다.
// 3. 점을 입력하면 파란색 LED(D13)를 1000ms 동안 켠다.
// 4. 선을 입력하면 빨간색 LED(D12)를 3000ms 동안 켠다.
// 5. 점을 입력하면 시리얼 모니터에 .을 출력한다.
// 6. 선을 입력하면 시리얼 모니터에 -를 출력한다.
// 7. 버튼을 계속 누르고 있어도 신호가 한 번만 입력되도록 한다.
// 8. 버튼은 평상히 HIGH, 누르면 LOW가 입력되는 것을 이용한다. - 풀업
void setup() {
  // put your setup code here, to run once:
  pinMode(2, INPUT); // SW1, input Switch버튼
  pinMode(3, INPUT); // SW2, input Switch버튼
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  Serial.begin(9600); // PC와 아두이노 사이 통신 설정
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(2) == LOW){
    Serial.print(".");

    digitalWrite(13, HIGH);
    delay(1000);
    digitalWrite(13, LOW);

    while(digitalRead(2) == LOW){ // 버튼을 계속 누르고 있어도 신호가 한 번만 입력되게 한다.
      delay(50);
    }
  }

  if(digitalRead(3) == LOW){
    Serial.print("-");

    digitalWrite(12, HIGH);
    delay(3000);
    digitalWrite(12, LOW);

    while(digitalRead(3) == LOW){
      delay(50);
    }
  }

}
