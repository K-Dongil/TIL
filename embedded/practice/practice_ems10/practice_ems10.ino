// 주차장 차량 수 관리 시스템
// 입차 버튼과 출차 버튼으로 현재 주차된 차량 수를 관리하고, 남은 주차 공간에 따라 RGB LED의 색상을 변경하는 시스템을 작성하시오.
// 1. SW1(D2)을 누르면 차량 수가 1대 증가한다.
// 2. SW2(D3)을 누르면 차량 수가 1대 감소한다
// 3. 주차장의 최대 차량 수는 5대로 한다.
// 4. 차량 수가 0대 미만 또는 5대 초과가 되지 않도록 한다.
// 5. 0~2대이면 RGB LED를 초록색으로 켠다.
// 6. 3~4대이면 RGB LED를 파란색으로 켠다.
// 7. 5대이면 RGB LED를 빨간색으로 켠다.
// 8. 현재 차량 수를 시리얼 모니터에 출력한다.
// 9. 버튼은 평상히 HIGH, 누르면 LOW가 입력되는 것을 이용한다. - 풀업
int car = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(2, INPUT); // SW1, input Switch버튼
  pinMode(3, INPUT); // SW2, input Switch버튼
  pinMode(9, OUTPUT); // RED , analogWrite 사용할 때는 pinMode 생략가능
  pinMode(10, OUTPUT); // GREEN
  pinMode(11, OUTPUT); // BLUE
  Serial.begin(9600);
  Serial.print("현재 주차되어 있는 차량 수: ");
  Serial.println(car);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(2) == LOW & car <5){
    car += 1;
    Serial.print("현재 주차되어 있는 차량 수: ");
    Serial.println(car);  
    while(digitalRead(2) == LOW){
      delay(50);
    }
  }

  if (digitalRead(3) == LOW & 0 < car){
    car -= 1;
    Serial.print("현재 주차되어 있는 차량 수: ");
    Serial.println(car);
    while(digitalRead(3) == LOW){
      delay(50);
    }
  }

  
  if (0<=car & car <=2){
    analogWrite(9, 0);
    analogWrite(11, 0);
    analogWrite(10, 255);
  }else if(3<=car & car <=4){
    analogWrite(9, 0);
    analogWrite(10, 0);
    analogWrite(11, 255);
  }else{
    analogWrite(10, 0);
    analogWrite(11, 0);
    analogWrite(9, 255);
  }
}
