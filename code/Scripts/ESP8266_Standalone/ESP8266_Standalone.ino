#define BLYNK_PRINT Serial    // Comment this out to disable prints and save space
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

#include <Wire.h>
#include <SoftwareSerial.h>
SoftwareSerial mySerial(D6, D5); // RX, TX

uint8_t DXr[16];
uint8_t DXw[16] = {2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2};

// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
// Token do meu projeto (Felipe): A2d3RGwoPfdfVMIAelKNz3_tzrodyBSd
// Token 2 (Felipe): vhCN_rP6T0v7fnvOhBpTNI95j5mNRK4d
// Token do Victor: g2S1xJj780Pi1StZio7D5OS4Mr_pwzlt;
char auth[] = "aadAytoWk85fG1OEV9DYaHNCY3D34_ai";

// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "LAB_DIGITAL";
char pass[] = "C1-17*2018@labdig";

uint32_t prev_millis;
uint32_t ms_cnt=0;

WidgetLED led0(V30);
WidgetLED led1(V31);
WidgetLED led2(V32);
WidgetLED led3(V33);

WidgetTerminal terminal(V0);

WidgetTerminal terminal_uart(V77);

int parity_calc = 0;
int parity = 0;

BLYNK_WRITE(V77)
{
  String dado = param.asStr();
  
  //terminal_uart.println(dado);

  //terminal_uart.flush();

  int dado2 = dado.toInt();

  Serial.println(dado2, BIN);

  mySerial.print(dado);
}

BLYNK_WRITE(V80)
{
  String sa = String(param.asInt(), BIN);

  //terminal_uart.println();
  //terminal_uart.println(sa);

  //terminal_uart.flush();

  for (int i = 1; i <= sa.length(); i++){
    DXw[i + 2] = sa.substring(sa.length() - i,sa.length() - i + 1).toInt();
    //terminal_uart.print(sa[i]);
    //terminal_uart.print(2+i);
  }
  //terminal_uart.println();

  for (int j = sa.length(); j < 7; j++){
    DXw[3+j] = 0;
    //terminal_uart.print(2+j);
  }
  //terminal_uart.println(DXw[2]);

  DXw[2] = 0;
  //DXw[10] = 1;
  //Serial.println(DXr[10]);
  parity_calc = DXw[3]^DXw[4]^DXw[5]^DXw[6]^DXw[7]^DXw[8]^DXw[9];
  //Serial.println(parity_calc);
  //if (parity != parity_calc){
  //  Serial.println("Erro de paridade!");
  //}

  dxWrite();
  dxRead();
  
  //for (int r = 2; r < 10; r++){
  //  Serial.println(DXw[r]);
  //}
  //Serial.println();

  //for (int r = 2; r < 10; r++){
  //  Serial.println(DXr[r]);
  //}

  //Serial.println();
  //Serial.println();
}

BLYNK_WRITE(V0)
{
  String cmd = param.asStr();
  
  if (cmd.startsWith("D")) {
    String pin = cmd.substring(1,2);
    String state = cmd.substring(3);

    switch (pin.toInt()) {
      case 6:
        terminal.print("D6 ");
        terminal.println(digitalRead(D6));
        break;
      case 7:
        terminal.print("D7 ");
        terminal.println(digitalRead(D7));
        break;
      case 8:
        terminal.print("D8 ");
        terminal.println(digitalRead(D8));
        break;

      case 1:
        if (state != "") digitalWrite(D1,state.toInt());
        terminal.print("D1 ");
        terminal.println(digitalRead(D1));
        break;
      case 2:
        if (state != "") digitalWrite(D2,state.toInt());
        terminal.print("D2 ");
        terminal.println(digitalRead(D2));
        break;
      case 5:
        if (state != "") digitalWrite(D5,state.toInt());
        terminal.print("D5 ");
        terminal.println(digitalRead(D5));
        break;

      case 4:
        if (state != "") digitalWrite(D4,state.toInt());
        terminal.print("D4 ");
        terminal.println(digitalRead(D4));
        break;
    }

    

    
    
    //terminal.println(pin);
    //terminal.println(state);

    terminal.flush();
   }


   if (cmd.startsWith("E")) {
   int i = cmd.indexOf(" ");
    
   String pin = cmd.substring(1,i);
   String state = cmd.substring(3);

   switch (pin.toInt()) {
     case 0:
       if (state != "") {
         DXw[0] = state.toInt();
         Blynk.virtualWrite(V10, state.toInt());
         break;
       }
     case 1:
       if (state != "") {
         DXw[1] = state.toInt();
         Blynk.virtualWrite(V11, state.toInt());
         break;
       }
     case 2:
       if (state != "") {
         DXw[2] = state.toInt();
         Blynk.virtualWrite(V12, state.toInt());
         break;
       }
     case 3:
       if (state != "") {
         DXw[3] = state.toInt();
         Blynk.virtualWrite(V13, state.toInt());
         break;
       }
     case 4:
       if (state != "") {
         DXw[4] = state.toInt();
         Blynk.virtualWrite(V14, state.toInt());
         break;
       }
     case 5:
       if (state != "") {
         DXw[5] = state.toInt();
         Blynk.virtualWrite(V15, state.toInt());
         break;
       }
     case 6:
       if (state != "") {
         DXw[6] = state.toInt();
         Blynk.virtualWrite(V16, state.toInt());
         break;
       }
     case 7:
       if (state != "") {
         DXw[7] = state.toInt();
         Blynk.virtualWrite(V17, state.toInt());
         break;
       }
     case 8:
       if (state != "") {
         DXw[8] = state.toInt();
         Blynk.virtualWrite(V18, state.toInt());
         break;
       }
     case 9:
       if (state != "") {
         DXw[9] = state.toInt();
         Blynk.virtualWrite(V19, state.toInt());
         break;
       }
     case 10:
       if (state != "") {
         DXw[10] = state.toInt();
         Blynk.virtualWrite(V20, state.toInt());
         break;
       }
     case 11:
       if (state != "") {
         DXw[11] = state.toInt();
         Blynk.virtualWrite(V21, state.toInt());
         break;
       }
   }
  }
}

BLYNK_CONNECTED() {
    Blynk.syncVirtual(V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21);
}

BLYNK_WRITE(V10)  { DXw[0] = param.asInt(); }
BLYNK_WRITE(V11)  { DXw[1] = param.asInt(); dxWrite(); }
BLYNK_WRITE(V12)  { DXw[2] = param.asInt(); }
BLYNK_WRITE(V13)  { DXw[3] = param.asInt(); }
BLYNK_WRITE(V14)  { DXw[4] = param.asInt(); }
BLYNK_WRITE(V15)  { DXw[5] = param.asInt(); }
BLYNK_WRITE(V16)  { DXw[6] = param.asInt(); }
BLYNK_WRITE(V17)  { DXw[7] = param.asInt(); }
BLYNK_WRITE(V18)  { DXw[8] = param.asInt(); }
BLYNK_WRITE(V19)  { DXw[9] = param.asInt(); }
//BLYNK_WRITE(V20)  { DXw[10] = param.asInt(); dxWrite(); parity = param.asInt(); }
BLYNK_WRITE(V20)  {
  int value = param.asInt();
  if (value == 1) DXw[10] = 0;
  if (value == 0) DXw[10] = 1;
  dxWrite();
  parity = param.asInt();
}
//BLYNK_WRITE(V20)  { parity = param.asInt(); }
BLYNK_WRITE(V21)  { DXw[11] = param.asInt(); }

void setup()
{
  pinMode(D6, INPUT); //RX
  pinMode(D7, INPUT);
  pinMode(D8, INPUT);

  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  pinMode(D5, OUTPUT);

  pinMode(D4, OUTPUT);

  Wire.begin(D2,D1); //SDA, SCL

  mySerial.begin(9600); //https://www.arduino.cc/reference/en/language/functions/communication/serial/begin/
  Serial.begin(115200);

  Blynk.begin(auth, ssid, pass);
}

void loop()
{
  Blynk.run();
  
  if(prev_millis!=millis()){
    prev_millis=millis();
    if(ms_cnt%100==0){
      dxRead();




      if ((DXr[13] == 0) and (DXr[12] == 0)) Blynk.virtualWrite(V40,0);
      if ((DXr[13] == 0) and (DXr[12] == 1)) Blynk.virtualWrite(V40,1);
      if ((DXr[13] == 1) and (DXr[12] == 0)) Blynk.virtualWrite(V40,2);
      if ((DXr[13] == 1) and (DXr[12] == 1)) Blynk.virtualWrite(V40,3);


      
      
      if (DXr[12] == 0) led0.off();
      if (DXr[12] == 1) led0.on();

      if (DXr[13] == 0) led1.off();
      if (DXr[13] == 1) led1.on();

      if (DXr[14] == 0) led2.off();
      if (DXr[14] == 1) led2.on();

      if (DXr[15] == 0) led3.off();
      if (DXr[15] == 1) led3.on();

      dxWrite();
    }
    ms_cnt++;
  }



  digitalWrite(D4,digitalRead(D6));

  if (mySerial.available()){
    //if (parity == parity_calc){
      char value = mySerial.read();
      Serial.println(value, BIN);

      char valueb = value;

      bitWrite(valueb, 8, 0);
      bitWrite(valueb, 7, 0);
      for (int i=0; i<7; i++) {
         bitWrite(valueb, 6 - i, bitRead(value, i));
       }
      Serial.println(valueb, BIN);
      
      String sa = String(value, HEX);
      
      String sa2;
      sa2 = value;
      
      //sa = sa + " " + sa2;
      
      //Serial.println(sa);
      
      terminal_uart.println(sa2);
      terminal_uart.flush();
    //}
  }
}
