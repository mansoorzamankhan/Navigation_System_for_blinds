const int buzzerPin = 9;// declaring the PWM pin</p><p>void setup() {
const int trigpin1= 8;  
const int echopin1= 7;  
const int trigpin2= 6;  
const int echopin2= 5; 
const int remote = 11;
const int receiver = 10; 
const int water= 4;
const int Light = 3; //input pin for LDR 
const char Terminator= '|';
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

   while(!Serial){
      //wait for serial por
    } 
} 
void  serialCom(String message){
   if (Serial.available()>0)
   {
  String commandfromjetson=Serial.readStringUntil(Terminator);
  // put your main code here, to run repeatedly:
  String ackmsg= message +commandfromjetson ;
  
 
 Serial.print(ackmsg);}
 delay(500);  
 
 }
void obstacle_deetction(){
     
  digitalWrite(trigpin1,HIGH);  
  delay(1000);  
  digitalWrite(trigpin1,LOW);  
  duration1=pulseIn(echopin1,HIGH);  
  distance1 = duration1*0.034/2; 
   
  digitalWrite(trigpin2,HIGH);  
  delay(1000);  
  digitalWrite(trigpin2,LOW);  
  duration2=pulseIn(echopin2,HIGH);  
  distance2 = duration2*0.034/2;  
   
  if ( distance2<25 && distance1<35&& distance1>25 )
    {
   String msg="stares detected";
    serialCom(msg);
    }
   else if  (distance2<25 && distance1>25)
    {
     
    String msg="small object  detected";
    serialCom(msg);
    }
    else if  (distance1<30 && distance2<30)
    {
     
    String msg="large object ";
    serialCom(msg);
    }
    
    else
    { digitalWrite(LED_BUILTIN ,HIGH);}
}
void water_detection(){
  if (digitalRead (water)==LOW)
    {
    
    String msg="wet surface detected ";
    serialCom(msg);
    }
  else
    { digitalWrite(LED_BUILTIN ,HIGH);}
}
void light_detection() { //infinite loopy



//If very dark
if (digitalRead (Light)==HIGH)
{
 String msg="its very dark here";
    serialCom(msg);
}


}

void loop()
{
  obstacle_deetction();
water_detection();
light_detection ();

}
