# 🔧 ROZWIĄZANIE BŁĘDU 500 - TIMETRACKER PRO

## 🚨 BŁĄD 500 - DIAGNOZA I ROZWIĄZANIE

### 1. NAJPIERW SPRAWDŹ UPRAWNIENIA PLIKÓW

**Na serwerze home.pl wykonaj:**
```bash
# Przejdź do katalogu public_html
cd public_html

# Uruchom skrypt uprawnień
bash set_permissions.sh
```

**LUB ustaw ręcznie:**
```bash
# Uprawnienia 755 dla plików .py3
chmod 755 *.py3

# Uprawnienia 644 dla pozostałych
chmod 644 *.py *.html *.json *.txt *.db .htaccess

# Uprawnienia dla folderu static
chmod 755 static/
chmod 644 static/*/*.* 2>/dev/null || true
```

### 2. PRZETESTUJ KROK PO KROKU

**KROK 1: Test CGI**
```
https://TWOJA-DOMENA.home.pl/test.py3
```
**Oczekiwany rezultat:** "Test CGI na home.pl - Jeśli widzisz ten komunikat, CGI działa!"

**KROK 2: Test inicjalizacji**
```
https://TWOJA-DOMENA.home.pl/init_simple.py3
```
**Oczekiwany rezultat:** JSON z komunikatem "Database initialized successfully"

**KROK 3: Test strony głównej**
```
https://TWOJA-DOMENA.home.pl/
```
**Oczekiwany rezultat:** Strona aplikacji TimeTracker Pro

### 3. NAJCZĘSTSZE PRZYCZYNY BŁĘDU 500:

#### ❌ Problem 1: Shebang (pierwsza linia)
**Sprawdź czy pliki .py3 zaczynają się od:**
```python
#!/usr/bin/python3
```

#### ❌ Problem 2: Brakujące moduły Python
**Potrzebujesz pakietów:**
- bcrypt
- PyJWT  
- qrcode
- pillow

**Rozwiązanie:** Skontaktuj się z supportem home.pl o instalację tych pakietów.

#### ❌ Problem 3: Nieprawidłowe uprawnienia
**Sprawdź uprawnienia:**
```bash
ls -la *.py3
```
**Wszystkie pliki .py3 muszą mieć uprawnienia 755**

#### ❌ Problem 4: Błędny .htaccess
**Sprawdź czy plik .htaccess jest wgrany i zawiera:**
```apache
Options +ExecCGI
AddHandler cgi-script .py3
```

### 4. ALTERNATYWNE ROZWIĄZANIA:

#### Opcja A: Użyj uproszczonych plików
Zamiast głównych plików, użyj:
- `init_simple.py3` zamiast `init.py3`
- `login_simple.py3` zamiast `login.py3`

#### Opcja B: Sprawdź logi błędów
W panelu home.pl sprawdź:
- Logi błędów Apache
- Logi PHP/CGI

#### Opcja C: Test minimalny
Stwórz plik `test_minimal.py3`:
```python
#!/usr/bin/python3
print("Content-Type: text/html")
print()
print("Minimal test OK!")
```

### 5. KOMENDY DIAGNOSTYCZNE:

```bash
# Sprawdź uprawnienia
ls -la *.py3

# Sprawdź czy pliki istnieją
ls -la test.py3 init_simple.py3

# Sprawdź zawartość .htaccess
cat .htaccess

# Sprawdź wersję Python
python3 --version
```

### 6. KONTAKT Z SUPPORTEM HOME.PL:

Jeśli nadal masz problemy, skontaktuj się z supportem home.pl i poproś o:
1. Instalację pakietów: bcrypt, PyJWT, qrcode, pillow
2. Sprawdzenie czy CGI Python jest włączone
3. Sprawdzenie logów błędów dla Twojej domeny

### 7. SZYBKA DIAGNOZA:

**Jeśli test.py3 NIE DZIAŁA:**
- Problem z uprawnieniami lub konfiguracją CGI

**Jeśli test.py3 DZIAŁA, ale init_simple.py3 NIE:**
- Problem z modułami Python

**Jeśli init_simple.py3 DZIAŁA, ale strona główna NIE:**
- Problem z frontendem lub .htaccess

## 🎯 NAJCZĘSTSZE ROZWIĄZANIE:

1. **Ustaw uprawnienia 755 dla wszystkich plików .py3**
2. **Uruchom test.py3**
3. **Skontaktuj się z supportem home.pl o pakiety Python**

**Powodzenia! 🚀**