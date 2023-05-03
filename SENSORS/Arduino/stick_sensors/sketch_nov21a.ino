const int buzzerPin = 9;// declaring the PWM pin</p><p>void setup() {
const int trigpin1= 8;  
const int echopin1= 7;  
const int trigpin2= 6;  
const int echopin2= 5; 
const int remote = 11;
const int receiver = 10; 
const int water= 4;
const int Light = 3; //input pin for LDR 
//const char Terminator= '|';
int Intens;
int distance1;
int duration1;
long duration2;  
int distance2; 

void setup(){  
  pinMode(buzzerPin, OUTPUT);
  pinMode(water,INPUT);
  pinMode(trigpin1,OUTPUT);  
  pinMode(echopin1,INPUT); 
  pinMode(trigpin2,OUTPUT);  
  pinMode(echopin2,INPUT); 
  pinMode(LED_BUILTIN,OUTPUT); 
  pinMode(Light,INPUT);
  pinMode(remote,INPUT);
  pinMode(receiver,OUTPUT);
  
 Serial.begin(115200);

//     while(!Serial){
//      //wait for serial por
//      } 
} 
//void  serialCom(String message){
//   if (Serial.available()>0)
//   {
//  String commandfromjetson=Serial.readStringUntil(Terminator);
//  // put your main code here, to run repeatedly:
//  String ackmsg= message +commandfromjetson ;
//  
// 
// Serial.print(ackmsg);}
// delay(500);  
// 
// }
void obstacle_deetction(){
     
  digitalWrite(trigpin1,HIGH);  
  delay(1000);  
  digitalWrite(trigpin1,LOW);  
  duration1=pulseIn(echopin1,HIGH);  
  distance1 = duration1*0.034/2; 
  Serial.println("uper ultrasonic ");
  Serial.println(distance1); 
  digitalWrite(trigpin2,HIGH);  
  delay(1000);  
  digitalWrite(trigpin2,LOW);  
  duration2=pulseIn(echopin2,HIGH);  
  distance2 = duration2*0.034/2;  
  
  Serial.println("lower ultrasonic ");
  Serial.println(distance2); 
  if ( distance2<25 && distance1<35&& distance1>25 )
    {
   String msg="stares detected"
    serialCom(msg)
    }
   else if  (distance2<25 && distance1>25)
    {
     
     tone(buzzerPin, 500);
    delay(100);
    noTone(buzzerPin);
    delay(10);
    Serial.println("small object ");
    }
    else if  (distance1<30 && distance2<30)
    {
     
    tone(buzzerPin, 100);
    delay(100);
    noTone(buzzerPin);
    delay(10);
    Serial.println("large object ");
    }
    
    else
    { digitalWrite(LED_BUILTIN ,HIGH);}
}
void water_detection(){
  if (digitalRead (water)==LOW)
    {
    
    tone(buzzerPin, 100);
    delay(300);
    noTone(buzzerPin);
    delay(5);
    Serial.println("wet surface detected");
    
    }
  else
    { digitalWrite(LED_BUILTIN ,HIGH);}
}
void light_detection() { //infinite loopy



//If very dark
if (digitalRead (Light)==HIGH)
{
 tone(buzzerPin, 3000);
    delay(100);
    noTone(buzzerPin);
    delay(10);
    Serial.println("its very dark here ");
}


}
void RF(){
  digitalWrite (remote,LOW);
  if (digitalRead (receiver)==LOW)
  {
     Serial.println("RF detected ");
      }
 else if (digitalRead (receiver)==HIGH)
    {  Serial.println("RF Not detected ");
      }
  
}
void loop()
{
  obstacle_deetction();
water_detection();
//light_detection ();
RF();
}
