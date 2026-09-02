void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(0< Serial.available()){
    int idx = Serial.parseInt();

    // 줄바꿈 문자는 무시
    if (idx == '\n' || idx == '\r'){
      return;
    }

    if(0 <= idx & idx <= 10){
      // 입력된 숫자만큼 LED 밝기를 막대그래프 형태로 표현 (막대그래프 길이는 10칸)
      Serial.print(idx);
      Serial.println("입력");
      Serial.print("Brightness : [");
      for (int i=0; i<idx; i++){
        Serial.print("#");
      }
      for (int i=idx; i<10; i++){
        Serial.print(" ");
      }
      Serial.println("]");
    }else{
      Serial.println("Please enter the positive value(0~10)");
    }
    
  }
}