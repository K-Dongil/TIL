// 버튼으로 색상&세기 바꾸
int red = 0; // red, green, blue 세기 0~255 (0~5V)
int green = 0;
int blue = 0;
int color = 0; // 0: RED, 1: GREEN, 2: BLUE

void setup() {
  // put your setup code here, to run once:
  pinMode(2, INPUT); // 색상 변경 버튼
  pinMode(3, INPUT); // 밝기 증가 버튼
  Serial.begin(9600); // PC와 아두이노 사이 통신 설정
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(2) == LOW){ // 버튼을 눌렀을 때 신호가 LOW(0)로 떨어지는 것을 감지하여 색상 변경 - pull up
    color++;
    Serial.println(color);

    if(2 < color){
      color = 0; // red, green, blue 한 바퀴돌면 red로 초기화
    }

    // 색상 변경 버튼 눌렀을 때 red, green, blue 0으로 초기화
    red = 0;
    green = 0;
    blue = 0;

    // 버튼을 뗄 때까지 대기
    while(digitalRead(2) == LOW);
    delay(50);
  }

  // D3 버튼을 누르면 선택된 색의 밝기 증가
  if(digitalRead(3) == LOW){
    if(color == 0){
      red += 51;
      if (255 < red){
        red = 0;
      }
    }

    if(color == 1){
      green += 51;
      if(255 < green){
        green = 0;
      }
    }

    if(color == 2){
      blue += 51;
      if(255 < blue){
        blue = 0;
      }
    }

    // 버튼을 뗄 때까지 대기
    while (digitalRead(3) == LOW);
    delay(50);
  }

  // RGB LED 출력
  analogWrite(9,red);
  analogWrite(10,green);
  analogWrite(11,blue);
}
