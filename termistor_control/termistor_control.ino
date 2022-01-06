//Thermistor NTC 110 control program using arduino UNO
//The code is prepared for four same thermistors

/*thermistor parameters:
 * RT0: 1000 Ω
 * B: 3270 K +- 0.75%
 * T0:  25 C
 * +- 5%
 */

//These values are in the datasheet
#define RT0 1000  // 1 kΩ
#define B 3270      // K
//--------------------------------------

#define VCC 5.0    //Supply voltage
#define R 1000  // R=1 kΩ

//Variables for each thermistor
float RT0, VR0, ln0, TX0, T0, VRT0;
float RT1, VR1, ln1, TX1, T1, VRT1;
float RT2, VR2, ln2, TX2, T2, VRT2;
float RT3, VR3, ln3, TX3, T3, VRT3;

//Calibration of thermistor and conversion from Celsius to kelvin
void setup() {
  Serial.begin(9600);
  T0 = 19 + 273.15;
  T1 = 18.5 + 273.15;
  T2 = 18.3 + 273.15;
  T3 = 16.8 + 273.15;
}

void loop() {
  //FRIST A0
  VRT0 = analogRead(A0);              //Acquisition analog value of VRT
  VRT0 = (5.00 / 1023.00) * VRT0;      //Conversion to voltage
  VR0 = VCC - VRT0;
  RT0 = VRT0 / (VR0 / R);               //Resistance of RT

  ln = log(RT0 / RT0);
  TX0 = (1 / ((ln0 / B) + (1 / T0))); //Temperature from thermistor

  TX0 = TX0 - 273.15;                 //Conversion to Celsius

  //SECOND A1
  VRT1 = analogRead(A1);              //Acquisition analog value of VRT
  VRT1 = (5.00 / 1023.00) * VRT1;      //Conversion to voltage
  VR1 = VCC - VRT1;
  RT1 = VRT1 / (VR1 / R);               //Resistance of RT

  ln1 = log(RT1 / RT0);
  TX1 = (1 / ((ln1 / B) + (1 / T1))); //Temperature from thermistor

  TX1 = TX1 - 273.15;                 //Conversion to Celsius

  //THIRD A2
  VRT2 = analogRead(A2);              //Acquisition analog value of VRT
  VRT2 = (5.00 / 1023.00) * VRT2;      //Conversion to voltage
  VR2 = VCC - VRT2;
  RT2 = VRT2 / (VR2 / R);               //Resistance of RT

  ln2 = log(RT2 / RT0);
  TX2 = (1 / ((ln2 / B) + (1 / T2))); //Temperature from thermistor

  TX2 = TX2 - 273.15;                 //Conversion to Celsius

  //FOURTH A3
  VRT3 = analogRead(A3);              //Acquisition analog value of VRT
  VRT3 = (5.00 / 1023.00) * VRT3;      //Conversion to voltage
  VR3 = VCC - VRT3;
  RT3 = VRT3 / (VR3 / R);               //Resistance of RT

  ln3 = log(RT3 / RT0);
  TX3 = (1 / ((ln3 / B) + (1 / T3))); //Temperature from thermistor

  TX3 = TX3 - 273.15;                 //Conversion to Celsius

  //SERIAL PRINTING CELSIUS TEMPERATURE VALUES
  Serial.print(TX0);
  Serial.print(";");
  Serial.print(TX1);
  Serial.print(";");
  Serial.print(TX2);
  Serial.print(";");
  Serial.print(TX3);
  Serial.print("\n");

  //DELAS 1000ms
  delay(1000);

}
