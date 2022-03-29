void parsingData(String dataTerima) {
  //    Convert from String Object to String.
  char buf[255];
  char *p = buf;
  char *str;
  char *data[6];
  int i;
  String bahuKiri, bahuKanan, sikuKiri, sikuKanan;

  dataTerima.toCharArray(buf, sizeof(buf));
  while ((str = strtok_r(p, ";", &p)) != NULL) // delimiter is the semicolon
  {
    data[i] = str;
    i++;
  }

  bahuKiri = data[0];
  bahuKanan = data[1];
  sikuKiri = data[2];
  sikuKanan = data[3];

  Serial.print("Bahu Kanan  : "); Serial.println(bahuKanan);
  Serial.print("Bahu Kiri  : "); Serial.println(bahuKiri);
  Serial.print("Siku Kanan  : "); Serial.println(sikuKanan);
  Serial.print("Siku Kiri  : "); Serial.println(sikuKiri);

}
