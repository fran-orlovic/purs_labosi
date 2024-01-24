#include <WiFi.h>
#include "PubSubClient.h"

const char *MQTT = "192.168.86.216";
const char *MQTT_2 = "192.168.86.216";
const char* SSID = "Lab1202";
const char* PASSWORD = "%Pr0j3ct2021%";


WiFiClient espClient;
PubSubClient client(espClient);

void callback(char* topic, byte* payload, unsigned int length)
{
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++)
  {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}

void setup()
{
  Serial.begin(9600);
  WiFi.begin(SSID, PASSWORD);
  Serial.print("Connecting to WiFi ..");
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print('.');
    delay(500);
  }
  Serial.println(WiFi.localIP());

  client.setServer(MQTT_2, 1883);
  client.setCallback(callback);
  //client.setServer(MQTT, 1883); // -> 1.zadatak
  while (!client.connected())
  {
    Serial.print("Attempting MQTT connection...");
    if (client.connect("ESP32Client"))
    {
      Serial.println("connected");
    }
    else
    {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
  client.subscribe("esp32/temperatura");
}

// void loop()
// {
//   client.publish("esp32/temperatura", "100");
//   delay(1000);
// }

void loop()
{
  client.loop();
}