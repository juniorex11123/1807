# 🚨 SZYBKA POMOC - BŁĄD 500

## 1. GDZIE JEST PLIK set_permissions.sh?

**Lokalizacja:** `/app/deployment_homepl/set_permissions.sh`

## 2. CO ZROBIĆ Z BŁĘDEM 500?

### KROK 1: Ustaw uprawnienia
```bash
# Na serwerze home.pl w katalogu public_html:
chmod 755 *.py3
chmod 644 *.py *.html *.json *.txt *.db .htaccess
chmod 755 static/
```

### KROK 2: Przetestuj minimalny CGI
Wgraj i przetestuj plik `test_minimal.py3`:
```
https://TWOJA-DOMENA.home.pl/test_minimal.py3
```

**Jeśli DZIAŁA:** CGI jest OK, problem z modułami Python
**Jeśli NIE DZIAŁA:** Problem z konfiguracją CGI

### KROK 3: Skontaktuj się z supportem home.pl
Poproś o instalację pakietów:
- bcrypt
- PyJWT
- qrcode  
- pillow

## 3. PLIKI DO PRZETESTOWANIA (W KOLEJNOŚCI):

1. `test_minimal.py3` - test bazowy
2. `test.py3` - test CGI  
3. `init_simple.py3` - test inicjalizacji
4. `https://TWOJA-DOMENA.home.pl/` - strona główna

## 4. JEŚLI NADAL NIE DZIAŁA:

Wyślij mi informację:
- Który plik powoduje błąd 500?
- Co pokazują logi błędów w panelu home.pl?
- Czy test_minimal.py3 działa?

**Pomogę Ci rozwiązać problem! 🔧**