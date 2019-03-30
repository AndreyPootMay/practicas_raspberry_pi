#define led 30

char estadoLed = 0;

void setup()
{
	pinMode(led, OUTPUT);
	Serial.begin(9600);
}

void loop()
{
	if (Serial.available() > 0)
	{
		estadoLed = Serial.read();
		if(estadoLed == 'H') {
		    digitalWrite(led, HIGH);
		} else if (estadoLed == 'L') {
			digitalWrite(led, LOW);
		}
	}
}