void setup() {
  // put your setup code here, to run once:
    Serial.begin(115200);
    while(!Serial){
      //wait for serial por
      }
}
const char Terminator= '|';
void loop() {
  if (Serial.available()>0)
{
  String commandfromjetson=Serial.readStringUntil(Terminator);
  // put your main code here, to run repeatedly:
  String ackmsg="hellow nano this is the mesage what i received "+commandfromjetson;
  
 
 Serial.print(ackmsg);}
 delay(500);
}
