void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int i=0;
  for (int i=0; i<=255; i++){
    Serial.print("Decimal : ");
    Serial.print(i);
    Serial.print("   Binary : ");
    Serial.println(i, BIN); // i의 값이 binary값으로 바뀐다
  }
}