// 후진 주차 경고시스템2
// Easy module Shield 버튼과 부저를 이용하여 차량의 전진/후진 상태를 구현하시오.
// 1. SW1(D2)을 누르면 전진 기어로 설정한다.
// 2. SW(D3)을 누르면 후진 기어로 설정한다.
//    - 후진 단계는 총 3단계로 구성한다.
//    - SW2를 누를 때마다 후진 1단계 -> 2단계 -> 3단계 -> 1단계 순으로 변경한다.
// 3. 후진 단계가 높아질수록 부저의 경고음 간격이 점점 빨라지도록 구현한다.
// * SW1, SW2 버튼은 눌렀을 때 LOW(0)가 입력된다.
// tone()과 noTone() 함수를 사용한다.

int gear = 0; // 정차: 0 전진: 1, 후진 1단계: 2, 후진 2단계: 3, 후진 3단계: 4 

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
    if (gear == 0 || gear == 1){
      gear = 2;
    }else if (gear <4){
      gear += 1;
    }
  }

  if (gear == 0 || gear == 1){
    noTone(5);
  }else{
    tone(5, 1000, 20);
    delay(800 / gear);
  }

}
