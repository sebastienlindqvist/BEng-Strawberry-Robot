#include <Servo.h>
#include <Stepper.h>


//--------------------------------------------------
//      variables
//--------------------------------------------------
int stepsPerRevolution = 1000;  
int pos = 0; 
char c;
int d;
//--------------------------------------------------
//     Gantry motor
//--------------------------------------------------
const int stepPin = 51; 
const int dirPin = 50; 
const int stepPin2 = 42; 
const int dirPin2 = 43;
//--------------------------------------------------
//      End effector
//--------------------------------------------------
Servo EndEffector;
Servo EndEffectorJoint;
Stepper EndEffectorWrist(stepsPerRevolution, 1, 3, 2, 4);
Stepper armmotor(stepsPerRevolution, 4, 6, 5, 7);
//--------------------------------------------------
//
//--------------------------------------------------
 
void setup() {
  Serial.begin(9600);
  //--------------------------------------------------
  //
  //--------------------------------------------------
  EndEffector.attach(9);
  EndEffectorJoint.attach(8);
  //--------------------------------------------------
  //
  //--------------------------------------------------
  EndEffector.write(0);
  EndEffectorJoint.write(0);
  //--------------------------------------------------
  //
  //--------------------------------------------------
  EndEffectorWrist.setSpeed(20);
  //--------------------------------------------------
  //
  //--------------------------------------------------
  pinMode(stepPin,OUTPUT); 
  pinMode(dirPin,OUTPUT);
  pinMode(stepPin2,OUTPUT); 
  pinMode(dirPin2,OUTPUT);
  Servo EndEffectorJoint;
  //--------------------------------------------------
  //
  //--------------------------------------------------
}

void loop() {
  if(Serial.available()){
    c = Serial.read();
    switch (c){
      //-----------------------------------
      //
      //-----------------------------------
    case 1:
      d = Serial.read();
      moveForwardGantt(d);
      break;
    case 2:
      d = Serial.read();
      moveBackwardGantt(d);
      break;
    case 3:
      d = Serial.read();
      moveLeftGantt(d);
      break;
    case 4:
      d = Serial.read();
      moveRightGantt(d);
      break;
      //-----------------------------------
      //   
      //-----------------------------------
    case 5:
      d = Serial.read();
      moveEndEffector(d);
      break;
    case 6:
      d = Serial.read();
      moveEndEffectorJoint(d);
      break;
    case 7:
      d = Serial.read();
      moveEndEffectorWrist();
      break;
    default:
      break;
    }
  
  }  
  /*moveForwardGantt();
  delay(1000);
  moveBackwardGantt();
  delay(1000);
  moveRightGantt();
  delay(1000);
  moveLeftGantt();
  delay(1000);*/
}
//-----------------------------------

//-----------------------------------
void moveEndEffector(int a ){
  EndEffector.write(a);
}
void moveEndEffectorJoint(int a){
  EndEffectorJoint.write(a);
}
void moveEndEffectorWrist(){
  EndEffectorWrist.step(-stepsPerRevolution);
}
//-----------------------------------

//-----------------------------------

void moveForwardGantt(int a) {
  digitalWrite(dirPin,HIGH);
  digitalWrite(dirPin2,LOW);
  MoveGantt(a);
}

void moveBackwardGantt(int a) {
  digitalWrite(dirPin,LOW);
  digitalWrite(dirPin2,HIGH);
  MoveGantt(a);
}

void moveLeftGantt(int a) {
  digitalWrite(dirPin,LOW); 
  digitalWrite(dirPin2,LOW);
  MoveGantt(a);
  
}
void moveRightGantt(int a) {
  digitalWrite(dirPin,HIGH); 
  digitalWrite(dirPin2,HIGH);
  MoveGantt(a);
}
//-----------------------------------

//-----------------------------------
void MoveGantt(int a){
  for(int x = 0; x < a; x++) {
    digitalWrite(stepPin,HIGH); 
    digitalWrite(stepPin2,HIGH); 
    delayMicroseconds(500); 
    digitalWrite(stepPin,LOW);
   digitalWrite(stepPin2,LOW);  
    delayMicroseconds(500); 
  }
}
