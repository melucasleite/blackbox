
void setup() {
  Serial.begin(500000); // use the same baud-rate as the python side
}

const int analog_pins = 16;
int readings [analog_pins];

void loop() {
  handle_serial();
}

void handle_serial() {
  while (Serial.available() > 0) {
    char incomingCharacter = Serial.read();
    switch (incomingCharacter) {
      case 'R':
        command_r();
        break;
    }
  }
}

void command_r() {
  read_analogs();
  print_analogs();
}

void read_analogs() {
  for (int i = 0; i < analog_pins; i++) {
    int reading = analogRead(i);
    readings[i] = reading;
    delay(1);
  }
}


void print_analogs() {
  for (int i = 0; i < analog_pins; i++) {
    Serial.print("A");
    Serial.print(i);
    Serial.print("R");
    Serial.print(readings[i]);
  }
  Serial.println("");
}

void test_a0() {
  int reading = analogRead(0);
  Serial.print(reading);
}
