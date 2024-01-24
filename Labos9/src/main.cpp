#include <Arduino.h>
#include "WiFi.h"
#include <HTTPClient.h>
#include <ArduinoJson.h>


const char *serverName = "http://192.168.86.219/hocu_bod?id=202";
HTTPClient http;
StaticJsonDocument<200> doc;

WiFiServer server(80);
WiFiClient client;


const char* SSID = "Lab1202";
const char* PASSWORD = "%Pr0j3ct2021%";

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
  //server.begin();
  delay(500);
}

void loop1()
{
  http.begin(serverName);
  int httpResponseCode = http.GET();
  Serial.print("Status code: ");
  Serial.println(httpResponseCode);
  Serial.println(http.getString());
  http.end();
  delay(1000);
}

void loop2()
{
  http.begin(serverName);
  int httpResponseCode = http.GET();

  Serial.print("Status code: ");
  Serial.println(httpResponseCode);

  String json = http.getString();

  deserializeJson(doc, json);

  const char *ip = doc["ip"];

  Serial.print("Globalna ip adresa je: "); // Globalna:193.198.206.131 Lokalna:192.168.86.215
  Serial.println(ip);

  http.end();

  delay(10000);
}

void loop4()
{
  String temperatura = "22";
  doc["temperatura"] = temperatura;

  String json;
  serializeJson(doc, json);

  http.begin(serverName);
  http.addHeader("Content-Type", "application/json");

  int httpResponseCode = http.POST(json);

  Serial.print("Status code: ");
  Serial.println(httpResponseCode);
  Serial.println(http.getString());

  http.end();

  delay(10000);
}

void loop5()
{
  if (client = server.available())
  {
    String zahtjev = client.readString();
    if (zahtjev.indexOf("GET") != -1)
    {
      Serial.println("Zaprimljen je GET zahtjev");
    }
    if (zahtjev.indexOf("POST") != -1)
    {
      Serial.println("Zaprimljen je POST zahtjev");
    }
    client.println("HTTP/1.1 200 OK");
    client.println("Connection: close");
    client.println();
    client.stop();
  }
}

#define LED 32
void loop6()
{
  if (client = server.available())
  {
    String zahtjev = client.readString();
    if (zahtjev.indexOf("POST") != -1 && zahtjev.indexOf("ON") != -1)
    {
      digitalWrite(LED, HIGH);
      Serial.println("ON");
    }
    if (zahtjev.indexOf("POST") != -1 && zahtjev.indexOf("OFF") != -1)
    {
      digitalWrite(LED, LOW);
      Serial.println("OFF");
    }
    client.println("HTTP/1.1 200 OK");
    client.println("Connection: close");
    client.println();
    client.stop();
  }
}


void loop7()
{
  String ime = "Fran";
  String prezime = "Orlovic";

  doc["ime"] = ime;
  doc["prezime"] = prezime;
  doc["ip"] = WiFi.localIP();

  String json;
  serializeJson(doc, json);

  http.begin(serverName);
  http.addHeader("Content-Type", "application/json");

  int httpResponseCode = http.POST(json);

  Serial.print("Status code: ");
  Serial.println(httpResponseCode);
  Serial.println(http.getString());

  http.end();

  delay(10000);
}

void loop8()
{
  http.begin(serverName);
  int httpResponseCode = http.GET();
  Serial.print("Status code: ");
  Serial.println(httpResponseCode);
  Serial.println(http.getString());
  http.end();
  delay(1000);
}
