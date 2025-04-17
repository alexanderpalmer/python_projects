unsigned long previousMillis = 0; // Speichert den letzten Zeitpunkt
const long interval = 5000;       // Intervall in Millisekunden (z.B. 2 Sekunden)

void setup() {
  Serial.begin(115200);
  // Warten, bis serieller Port verfügbar ist
  while (! Serial) {
    delay(1);
  }

}
void loop() {
  // 1000
  unsigned long currentMillis = millis();

  // Prüfen, ob das Intervall vergangen ist
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis; // Zeitstempel aktualisieren

    // Hier kommt die auszuführende Aktion hin
    Serial.println("Aktion ausgeführt, ohne die Schleife zu blockieren!");

     // Anderer Code kann hier parallel laufen
  doSomethingElse();
  }
}

void doSomethingElse() {
  // Beispiel: Eine andere Aufgabe
  Serial.println("Ich mache etwas anderes!");

}
