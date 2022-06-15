#include <BluetoothSerial.h>
//Parte bluetooth
BluetoothSerial SerialBT;
//Motores
#include <TB6612_ESP.h>
Motor M1;
Motor M2;
int  VELOCIDAD_AD = 500;
char instruccion = 'k';
#define TIEMPO 1000
void setup() {
  Serial.begin(115200);
  SerialBT.begin("Arduino_JMV"); //nombre bluetooh
  // M1.init(12, 17, 16, 0, 2500); // 17 16 12
  //M2.init(27, 14, 26, 1, 2500); //  27 14 26
  M1.init(17, 16, 12, 0, 2500);
  //M1.SetSpeed(1023);
  M2.init(27, 14, 26, 1, 2500);
  //M2.SetSpeed(1023);
}
void loop() {
  //Eliminar

  //leer Bluetooth enviar PC
  if (SerialBT.available())
  {
    instruccion = SerialBT.read();
    Serial.write(instruccion);


    //W adelante
    //S atras
    //a izquierda
    //d derecha
    //PARTE SENSOR DISTANCIA
    //M1.SetSpeed(VELOCIDAD_AD);
    //M2.SetSpeed(VELOCIDAD_AD);
    if (instruccion == 'a') {//30 maximo
      VELOCIDAD_AD = 250;
      delay(TIEMPO);
    }
    if (instruccion == 'b') {//60 maximo
      VELOCIDAD_AD = 390;
      delay(TIEMPO);
    }
    if (instruccion == 'c') {//pare
      M1.SetSpeed(0);
      M2.SetSpeed(0);
      delay(TIEMPO);
      M1.SetSpeed(VELOCIDAD_AD);
      M2.SetSpeed(VELOCIDAD_AD);
    }
    if (instruccion == 'd') {//derecha
      M1.SetSpeed(VELOCIDAD_AD * -1);
      M2.SetSpeed(VELOCIDAD_AD);
      delay(TIEMPO);
      M1.SetSpeed(0);
      M2.SetSpeed(0);
    }
    if (instruccion == 'e') {//izquierda
      M1.SetSpeed(VELOCIDAD_AD);
      M2.SetSpeed(VELOCIDAD_AD * -1);
      delay(TIEMPO);
      M1.SetSpeed(0);
      M2.SetSpeed(0);
    }
    if (instruccion == 'f') {//siga
      M1.SetSpeed(VELOCIDAD_AD);
      M2.SetSpeed(VELOCIDAD_AD);
      delay(TIEMPO);
    }

    if (instruccion == 'g') {//Cruce peatonal
      M1.SetSpeed(0);
      M2.SetSpeed(0);
      delay(TIEMPO);
      M1.SetSpeed(VELOCIDAD_AD);
      M2.SetSpeed(VELOCIDAD_AD);
    }
    if (instruccion == 'y') {
      M1.SetSpeed(VELOCIDAD_AD);
      M2.SetSpeed(VELOCIDAD_AD * -1);
      delay(TIEMPO);
      M1.SetSpeed(0);
      M2.SetSpeed(0);
    }
    if (instruccion == 'z') {
      M1.SetSpeed(VELOCIDAD_AD * -1);
      M2.SetSpeed(VELOCIDAD_AD * -1);
      delay(TIEMPO);
      M1.SetSpeed(0);
      M2.SetSpeed(0);
    }
  }
}
