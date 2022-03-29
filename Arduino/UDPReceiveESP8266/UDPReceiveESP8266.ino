#include <WiFiUdp.h>
#include <ESP8266WiFi.h>

#define WIFI_SSID "D-Link 114"
#define WIFI_PASSWORD "1sampai8"

IPAddress ip(192, 168, 100, 169);
IPAddress subnet(255, 255, 255, 0);
IPAddress gateway(192, 168, 100, 1);
IPAddress dns(192, 168, 100, 1);

//============UDP Setting ==================
WiFiUDP Udp;
unsigned int localUdpPort = 2609;
char incomingPacket[255];  // buffer for incoming packets

void setup() {
  Serial.begin(9600);
  Serial.println("بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيم");

  // ----------------- connect to wifi -----------------
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  WiFi.config(ip, dns, gateway, subnet);

  Serial.print("connecting");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(50);
  }

  Serial.println();
  Serial.print("connected: ");
  Serial.println(WiFi.localIP());
  // ----------------------------------------------------

  Udp.begin(localUdpPort);
}

void loop() {
  getData();
  delay(91);
}
