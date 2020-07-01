void setup() {
  Serial.begin(500000); // use the same baud-rate as the python side
}

const int analog_pins = 16;
const int output_pins = 53;
const int pwm_pins[] = {2,3,4,5,6,7,8,9,10,11,12,13,44,45,46};
int readings [analog_pins];
int outputs [output_pins];


#if !defined(ARRAY_SIZE)
    #define ARRAY_SIZE(x) (sizeof((x)) / sizeof((x)[0]))
#endif

void loop() {
  handle_serial();
}

void handle_serial() {
  while (Serial.available() > 0) {
    char incomingCharacter = Serial.read();
    switch (incomingCharacter) {
      case 'R':
        command_R();
        break;
       case 'O':
        command_O();
        break;
       case 'W':
        command_W();
        break;
       case 'U':
        command_U();
        break;
    }
  }
}

void command_R() {
  read_analogs();
  print_analogs();
}


void command_O() {
  print_outputs();
}

void command_W() {
  write_outputs();
}

void command_U() {
   int pin;
   pin = Serial.parseInt();
   Serial.read();
   int output;
   output = Serial.parseInt();
   update_output(pin, output);
}

void read_analogs() {
  for (int i = 0; i < analog_pins; i++) {
    int reading = analogRead(i);
    readings[i] = reading;
    delay(1);
  }
}

void update_output(int pin, int value) {
  outputs[pin] = value;
}

void write_outputs() {
    for (int i = 0; i < output_pins; i++) {
        int output = outputs[i];
//        Serial.print(i);
//        Serial.print(" ");
//        Serial.print(output);
//        Serial.print(" ");
        const int array_length = sizeof(pwm_pins)/sizeof(pwm_pins[0]);
        if (is_value_in_array(i, pwm_pins, ARRAY_SIZE(pwm_pins))) {
//          Serial.println("PWM");
          analogWrite(i, output);
        } else {
//          Serial.println("DIGITAL");
          digitalWrite(i, output);
        }
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


void print_outputs() {
  for (int i = 0; i < output_pins; i++) {
    Serial.print("D");
    Serial.print(i);
    Serial.print("V");
    Serial.print(outputs[i]);
  }
  Serial.println("");
}

boolean is_value_in_array(int value, const int array[], int array_length){
    for (int i = 0; i < array_length; i++){
        if (value == array[i]){
            return true;
        }
    }
    return false;
}
