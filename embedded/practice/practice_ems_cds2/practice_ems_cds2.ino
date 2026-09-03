// 주위 밝기에 따라 LED 빛 바꾸기
// 조도에 따른 차량 주변 밝기 상태 표시
// Easy module의 조도센서와 RGB LED를 이용하여 주변 밝기에 따라 LED 색상이 변하도록 프로그램을 작성
// 1. 조도센서는 A1을 사용한다.
// 2. 주변이 어두우면 빨간색 LED를 출력한다.
// 3. 중간 밝기에서는 파란색 LED를 출력한다.
// 4. 주변이 밝으면 초록색 LED를 출력한다.
// 조도센서 기준값 예시 (환경에 따라 다르게 세팅해야함)
// - 130 미만 : 어두움 : 빨간색, - 130이상 220미만 : 중간 -> 파란색, - 220이상 : 밝음 -> 초록색
void setup() {
  // put your setup code here, to run once:
  pinMode(9, OUTPUT); // Red
  pinMode(10, OUTPUT); // Green
  pinMode(11, OUTPUT); // Blue
  pinMode(A1, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int vin = analogRead(A1);
  int val = map(vin, 0, 1023, 0, 255);
  
  if (val <130){
    analogWrite(10, 0);
    analogWrite(11, 0);
    analogWrite(9, 255);
  }else if(val <220){
    analogWrite(9, 0);
    analogWrite(11, 0);
    analogWrite(11, 255);
  }else{
    analogWrite(9, 0);
    analogWrite(10, 0);
    analogWrite(10, 255);
  }
  Serial.println(val);
}
