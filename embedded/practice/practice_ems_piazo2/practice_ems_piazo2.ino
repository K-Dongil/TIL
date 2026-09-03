// 전진/후진 기어에 따른 후방 경고음 시스템
// Easy module Shield의 두 개 버튼을 이용하여, 차량의 전진/후진 기어를 모사한다.
// 1. SW1(D2)버튼을 누르면 전진 기어로 설정한다.
// 2. SW2(D3)버튼을 누르면 후진 기어로 설정한다.
// 3. 전진 기어에서는 부저가 울리지 않는다.
// 4. 후진 기어에서는 후방카메라가 작동한다고 가정하고, 부저가 일정한 간격으로 "삐-삐-" 소리를 반복한다.
// 5. 다시 전진 기어 버튼을 누르면 경고음을 중지한다.
int gear = 0; // 정차: 0 True: 1, False: 2

void setup() {
  // put your setup code here, to run once:
  pinMode(2, INPUT); // SW1, input Switch버튼
  pinMode(3, INPUT); // SW2, input Switch버튼
  pinMode(5, OUTPUT); // 부저 핀을 출력 모드로 설정
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(2) == LOW){
    gear = 1;
  }else if (digitalRead(3) == LOW){
    gear = 2;
  }

  if (gear == 1){
    noTone(5);
  }else if(gear == 2){
    tone(5, 1000, 20);
    delay(200);
  }


}