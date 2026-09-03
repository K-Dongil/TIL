// 양손 안전 작동장치
// Easy module Shield의 두 개의 버튼을 모두 누르고 있을 때만 장치가 작동하는 양손 안전 시스템을 작성하시오.
// 1. 왼쪽 안전 버튼은 SW2(D3), 오른쪽 안전 버튼은 SW1(D2)를 사용한다.
// 2. 두 버튼을 모두 누르면 파란색 LED(D13)가 켜진다.
// 3. 두 버튼 중 하나라도 누르지 않으면 파란색 LED가 꺼진다.
// 4. 장치가 작동하지 않을 때는 빨간색 LED(D12)가 켜진다.
// 5. 빨간색 LED와 파란색 LED가 동시에 켜지지 않도록 한다.
// 6. 버튼은 평상시 HIGH, 누르면 LOW가 입력되는 것을 이용한다. - 풀업
void setup() {
  // put your setup code here, to run once:
  pinMode(2, INPUT); // 오른쪽 안전 버튼, input Switch버튼
  pinMode(3, INPUT); // 왼쪽 안전 버튼, input Switch버튼
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  digitalWrite(12, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(2) == LOW & digitalRead(3) == LOW){
    digitalWrite(12, LOW);
    digitalWrite(13, HIGH);
  }else{
    digitalWrite(12, HIGH);
    digitalWrite(13, LOW);
  }

}
