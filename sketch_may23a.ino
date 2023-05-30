#include <SPI.h>
#include <MFRC522.h>
#define RST_PIN         5        
#define SS_PIN          4      

MFRC522 rfid(SS_PIN, RST_PIN);   
MFRC522::MIFARE_Key key;         
MFRC522::StatusCode status;      

void setup() {
  Serial.begin(9600);              
  SPI.begin();                     
  rfid.PCD_Init();                 
  rfid.PCD_SetAntennaGain(rfid.RxGain_max);  
  rfid.PCD_AntennaOff();           
  rfid.PCD_AntennaOn();           
}

void loop() {
  
        

        
  static uint32_t rebootTimer = millis(); 
  if (millis() - rebootTimer >= 1000) {   
    rebootTimer = millis();               
    digitalWrite(RST_PIN, HIGH);          
    delayMicroseconds(2);                 
    digitalWrite(RST_PIN, LOW);           
    rfid.PCD_Init();                      
  }
  if (!rfid.PICC_IsNewCardPresent()) return;  
  if (!rfid.PICC_ReadCardSerial()) return;   

  String uid_;
  uid_ += String(rfid.uid.uidByte[1]) + String(rfid.uid.uidByte[2]) + String(rfid.uid.uidByte[3]) + String(rfid.uid.uidByte[4]);
  Serial.print("UID: "); Serial.println(uid_.toInt());
  Serial.println("");
  delay(1000);
}
