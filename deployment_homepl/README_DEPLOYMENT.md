# 🚀 PAKIET DEPLOYMENT HOME.PL - TIMETRACKER PRO

## ✅ GOTOWY DO WDROŻENIA!

Ten folder zawiera wszystkie pliki potrzebne do wdrożenia aplikacji TimeTracker Pro na hostingu home.pl.

## 📁 ZAWARTOŚĆ PAKIETU:

### 1. Pliki konfiguracyjne:
- `.htaccess` - Konfiguracja Apache (KRYTYCZNY!)
- `index.html` - Strona główna aplikacji
- `asset-manifest.json` - Manifest aplikacji
- `timetracker_pro.db` - Baza danych SQLite (zainicjalizowana)
- `requirements.txt` - Lista wymaganych pakietów Python

### 2. Pliki CGI (.py3) - Backend API:
- `test.py3` - Test CGI (uruchom pierwszy!)
- `init_simple.py3` - Inicjalizacja systemu (uproszczona)
- `init.py3` - Inicjalizacja systemu (główna)
- `login_simple.py3` - Logowanie (uproszczone)
- `login.py3` - Logowanie (główne)
- `users.py3` - Zarządzanie użytkownikami
- `companies.py3` - Zarządzanie firmami
- `employees.py3` - Zarządzanie pracownikami
- `time_entries.py3` - Ewidencja czasu pracy
- `qr_generate.py3` - Generowanie kodów QR
- `qr_scan.py3` - Skanowanie kodów QR
- `api.py3` - API główne
- `utils.py3` - Funkcje pomocnicze
- `database.py3` - Operacje bazodanowe
- `auth.py3` - Uwierzytelnianie

### 3. Pliki pomocnicze Python (.py):
- `auth.py` - Moduł uwierzytelniania
- `database.py` - Moduł bazy danych
- `utils.py` - Funkcje pomocnicze

### 4. Pliki frontend:
- `static/` - Folder z plikami CSS i JavaScript
  - `static/css/` - Style CSS
  - `static/js/` - Skrypty JavaScript

## 🔧 INSTRUKCJE WDROŻENIA:

### KROK 1: Upload plików
1. Zaloguj się do panelu home.pl
2. Otwórz WebFTP
3. Przejdź do katalogu `public_html/`
4. Skopiuj **WSZYSTKIE** pliki z tego folderu do `public_html/`
5. Zachowaj strukturę folderów (szczególnie `static/`)

### KROK 2: Ustawienie uprawnień
**Pliki .py3 muszą mieć uprawnienia 755 (executable):**
- test.py3
- init_simple.py3
- init.py3
- login_simple.py3
- login.py3
- users.py3
- companies.py3
- employees.py3
- time_entries.py3
- qr_generate.py3
- qr_scan.py3
- api.py3
- utils.py3
- database.py3
- auth.py3

**Pozostałe pliki: 644 (readable)**

### KROK 3: Testowanie
1. **Test CGI**: `https://TWOJA-DOMENA.home.pl/test.py3`
   - Powinieneś zobaczyć: "Test CGI na home.pl - Jeśli widzisz ten komunikat, CGI działa!"

2. **Inicjalizacja**: `https://TWOJA-DOMENA.home.pl/init_simple.py3`
   - Powinieneś zobaczyć: {"message": "Database initialized successfully", "status": "ready"}

3. **Strona główna**: `https://TWOJA-DOMENA.home.pl/`
   - Powinieneś zobaczyć aplikację TimeTracker Pro

### KROK 4: Logowanie
Użyj domyślnych kont:
- **owner** / **owner123** (Administrator systemu)
- **admin** / **admin123** (Administrator firmy)
- **user** / **user123** (Pracownik)

## 🔍 ROZWIĄZYWANIE PROBLEMÓW:

### Problem: "Forbidden" przy .py3
**Rozwiązanie:**
1. Sprawdź uprawnienia plików .py3 (muszą być 755)
2. Sprawdź czy plik .htaccess jest wgrany
3. Skontaktuj się z supportem home.pl o obsługę Python 3

### Problem: "Internal Server Error"
**Rozwiązanie:**
1. Sprawdź czy wszystkie pliki .py są wgrane
2. Sprawdź czy wymagane pakiety Python są zainstalowane
3. Użyj plików _simple.py3 zamiast głównych

### Problem: Nie działa logowanie
**Rozwiązanie:**
1. Najpierw uruchom `init_simple.py3`
2. Użyj `login_simple.py3` zamiast `login.py3`
3. Sprawdź czy baza danych została utworzona

### Problem: Brak pakietów Python
**Rozwiązanie:**
Skontaktuj się z supportem home.pl o instalację:
- bcrypt
- PyJWT
- qrcode
- pillow

## 📊 INFORMACJE TECHNICZNE:

**Rozmiar pakietu**: ~4MB
**Liczba plików**: 25+ plików
**Wymagania**: hosting home.pl z Python 3
**Baza danych**: SQLite (zawarta w pakiecie)
**Czas wdrożenia**: 5-10 minut

## 🎯 FUNKCJONALNOŚCI:

✅ System logowania (3 poziomy dostępu)
✅ Zarządzanie użytkownikami
✅ Zarządzanie firmami
✅ Zarządzanie pracownikami
✅ Ewidencja czasu pracy
✅ Generowanie kodów QR
✅ Skanowanie kodów QR
✅ Raporty i statystyki
✅ API REST
✅ Responsywny frontend

## 🛡️ BEZPIECZEŃSTWO:

✅ Hashowanie haseł (bcrypt)
✅ Tokeny JWT
✅ Nagłówki bezpieczeństwa
✅ CORS protection
✅ Walidacja danych
✅ Ochrona przed SQL injection

## 🎉 GOTOWE DO WDROŻENIA!

Po wykonaniu powyższych kroków aplikacja TimeTracker Pro będzie w pełni funkcjonalna na hostingu home.pl.

**Powodzenia z wdrożeniem!**