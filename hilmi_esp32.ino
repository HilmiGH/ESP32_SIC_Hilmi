//Libraries Initialization
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <WiFi.h>
#include <HTTPClient.h>

// DHT Config
#define DHT_PIN 19 // initialize pin number for DHT Sensor
#define DHT_TYPE DHT11 // DHT11

// DHT Object
DHT dht(DHT_PIN, DHT_TYPE);
HTTPClient http;

// Variables Initialization
// Wifi Config
const char* ssid = "Wokwi-GUEST";
const char* password = "";

// Server Config
const char* serverUrl = "http://192.168.0.1:5000/sensor/data";

// Variabels
float temperature = 0;
float humidity = 0;
String jsonData = "";
int httpResponseCode = 0;

void WifiPrep() {
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);         
  WiFi.begin(ssid, password); 

  // Loading while waiting for WIFI
  while (WiFi.status() != WL_CONNECTED) {
    delay(2000);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void setup() {
  Serial.begin(115200);
  WifiPrep();
	dht.begin();
}

void loop() {
  delay(2000);
  getDHTData();
  sendSensorData();
}

void getDHTData() {
  temperature = dht.readTemperature();
  humidity = dht.readHumidity();

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Failed to read from DHT Sensor!");
  } else {
    Serial.println("Here are the current situation:");
    Serial.println("Temperature: " + String(temperature) + "°C");
    Serial.println("Humidity: " + String(humidity) + "%");
  }
}

void sendSensorData() {
  jsonData = "{\"temperature\":\"" + String(temperature) + "\",\"humidity\":\"" + String(humidity) +"\"}";

  http.begin(serverUrl);
  http.addHeader("Content-Type", "Content-Type: application/json"); 
  
  httpResponseCode = http.POST(jsonData); // Send the actual POST request

  if(httpResponseCode > 0){
    String response = http.getString();   // Get the response to the request
    Serial.print("HTTP Response code: ");
    Serial.println(response);             // Print request answer
    Serial.println();
  } else {
    Serial.print("Error in HTTP POST request: ");
    Serial.println(httpResponseCode);
    Serial.println();
    http.end();
 }
}