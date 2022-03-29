//void parsingData(String dataTerima) {
//  //    Convert from String Object to String.
//  char buf[255];
//  char *p = buf;
//  char *str;
//  char *data[6];
//  int i;
//
//  dataTerima.toCharArray(buf, sizeof(buf));
//  while ((str = strtok_r(p, ";", &p)) != NULL) // delimiter is the semicolon
//  {
//    data[i] = str;
//    i++;
//  }
//
//  jenisData = data[0];
//  Serial.print("Data Paket  : "); Serial.println(dataTerima);
//  Serial.print("Jenis Data  : "); Serial.println(jenisData);
//
//  if (jenisData == "T") {
//    sFixTemp      = data[1];
//    sFixHumi      = data[2];
//    sFixWindSpeed = data[3];
//    
//    Serial.print("Suhu        : "); Serial.println(sFixTemp);
//    Serial.print("Kelembaban  : "); Serial.println(sFixHumi);
//    Serial.print("K. Angin    : "); Serial.println(sFixWindSpeed);
//    Serial.println("");
//    
//    sendSTetap();
//    sendBlower();
//  }
//
//  if (jenisData == "P") {
//    idGrid    = data[1];
//    berat     = data[2];
//    amonia    = data[3];
//    hum       = data[4];
//    temp      = data[5];
//    
//    Serial.print("ID Grid     : "); Serial.println(idGrid);
//    Serial.print("Berat       : "); Serial.println(berat);
//    Serial.print("Amonia      : "); Serial.println(amonia);
//    Serial.print("Kelembaban  : "); Serial.println(hum);
//    Serial.print("Suhu        : "); Serial.println(temp);
//    Serial.println("");
//    
//    sendSPortabel();
//    sendSPortabelGrafik();
//  }
//
//}
