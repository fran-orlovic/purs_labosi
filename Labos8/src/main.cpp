#include <Arduino.h>

#define GREEN_LED 21
#define BLUE_LED 22
#define POT 32
void setup()
{
  Serial.begin(9600);
  //Serial.println("Setup function");
  pinMode(GREEN_LED, OUTPUT);
  pinMode(BLUE_LED, OUTPUT);
}

void loop()
{
  int del = 0;
  //Serial.println("Loop function");
  if (analogRead(POT) > 2000)
    {
      del = 250;
    }
  else del = 500;
  Serial.println(analogRead(POT));
  digitalWrite(GREEN_LED, HIGH);
  digitalWrite(BLUE_LED, LOW);
  //Serial.println("GREEN ON");
  delay(del);

  digitalWrite(GREEN_LED, LOW);
  digitalWrite(BLUE_LED, HIGH);
  //Serial.println("BLUE ON");
  delay(del);

}

#define BUTTON 32
void setup3()
{
  Serial.begin(9600);
  Serial.println("Setup function");
  pinMode(GREEN_LED, OUTPUT);
  pinMode(BLUE_LED, OUTPUT);
  pinMode(BUTTON, INPUT_PULLDOWN);
}

void loop3()
{
  Serial.println("Loop function");
  if (digitalRead(BUTTON) == LOW)
  {
    digitalWrite(GREEN_LED, HIGH);
    digitalWrite(BLUE_LED, LOW);
    Serial.println("GREEN ON");
  }
  else
  {
    digitalWrite(GREEN_LED, LOW);
    digitalWrite(BLUE_LED, HIGH);
    Serial.println("BLUE ON");
  }
  delay(1000);
}


void setup4()
{
  Serial.begin(9600);
  Serial.println("Setup function");
}

void loop4()
{
  Serial.println("Loop function");
  Serial.println(analogRead(POT));
  delay(500);
}

#define PWM_PIN 32
#define PWM_CHANNEL 0
#define FREQUENCY 5000
#define RESOLUTION 12
void setup5()
{
  ledcSetup(PWM_CHANNEL, FREQUENCY, RESOLUTION);
  ledcAttachPin(PWM_PIN, PWM_CHANNEL);
}
void loop5()
{
  ledcWrite(PWM_CHANNEL, analogRead(POT));
}