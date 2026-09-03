/*
int melody[] = {262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494, 523};

void setup() {
  // put your setup code here, to run once:
  pinMode(5, OUTPUT); // 부저 핀을 출력 모드로 설정
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i=0; i<8; i++){
    tone(5, melody[i], 250); // D5에서 meldoy[i] 주파수를 250ms동안 출력
    delay(400); // 다음 음을 재생하기 전 400ms 대기
    noTone(5); // 부저 끄기
  }
}
*/
void speaker_on(int pin, int freq, int on, int off);
int melody[] = {262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494, 523};

void setup() {
  // put your setup code here, to run once:
  pinMode(5, OUTPUT); // 부저 핀을 출력 모드로 설정

  // 도레미파솔라시도 연주
  for (int i=0; i<8; i++){
    speaker_on(5, melody[i], 250, 400);
  }
}

void loop() {
  // put your main code here, to run repeatedly:

}

void speaker_on(int pin, int freq, int on, int off){
  tone(pin, freq, on); // D5에서 freq 주파수를 on동안 출력
  delay(off); // 다음 음을 재생하기 전 off만큼 대기
  noTone(5); // 부저 끄기
}