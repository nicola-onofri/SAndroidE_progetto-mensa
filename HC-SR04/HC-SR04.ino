/*
* HC-SR04 Ultrasonic distance sensor sketch
* authors: Sara Ghanami, Nicola Onofri
*/
#define trigPin 9
#define echoPin 10

long duration;
int distance;

void setup() {
pinMode(echoPin, INPUT);
pinMode(trigPin, OUTPUT);
Serial.begin(9600);
}

void loop() {
//clear sensor
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);

//read and convesion
duration = pulseIn(echoPin, HIGH);
distance= duration*0.034/2;

//debug
Serial.print("Distance: ");
Serial.println(distance);
}
