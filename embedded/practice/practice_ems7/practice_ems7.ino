// 1. 기본 상태는 초록색으로 유지
// 2. SW1 버튼을 누르면 1초 동안 초록색을 유지
// 3. 이후 노란색으로 변경하고 1초간 유지
// 4. 이후 빨간색으로 변경하고 3초간 유지
// 5. 다시 초록색으로 돌아감
void setup() {
  // put your setup code here, to run once:
  pinMode(2, INPUT); // input Switch버튼
  pinMode(9, OUTPUT); // RED , analogWrite 사용할 때는 pinMode 생략가능
  pinMode(10, OUTPUT); // GREEN
  pinMode(11, OUTPUT); // BLUE
}

void loop() {
  // put your main code here, to run repeatedly:
  // 1. 기본 상태 초록색으로 유지
  analogWrite(9, 0);
  analogWrite(10, 255);
  analogWrite(11, 0);

  // 2. 버튼을 누르면 1초 동안 초록색을 유지, 
  
  if (digitalRead(2) == LOW){
    delay(1000);

    // 3. 이후 노란색으로 변경하고 1초간 유지
    analogWrite(9, 255);
    analogWrite(10, 212);
    analogWrite(11, 0);
    delay(1000);

    // 4. 이후 빨간색으로 변경하고 3초간 유지
    analogWrite(9, 255);
    analogWrite(10, 0);
    analogWrite(11, 0);
    delay(3000);
  }
}
