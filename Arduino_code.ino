char character;

void setup() 
{
  Serial.begin(9600);
}

void loop() 
{
  Receive_Send_Info();
}

void Receive_Send_Info()
{
  if(Serial.available() > 0)
  {
    character = Serial.read();
    Serial.println("The character has been recieved by Arduino");
    delay(500);
    Serial.println(character);
    delay(100);
  } 
}
