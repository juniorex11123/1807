# 🚀 TimeTracker Pro - Instrukcje wdrożenia na home.pl

## ✅ GOTOWE DO WDROŻENIA!

Wszystkie pliki zostały przygotowane i są gotowe do skopiowania na hosting home.pl przez WebFTP.

## 📁 PLIKI DO UPLOADOWANIA (skopiuj wszystkie pliki z /app/ na webftp):

### 1. Pliki główne:
- `index.html` - Strona główna aplikacji
- `.htaccess` - Konfiguracja Apache (BARDZO WAŻNE!)
- `timetracker_pro.db` - Baza danych SQLite
- `asset-manifest.json` - Manifest aplikacji

### 2. Pliki CGI (Backend API):
- `init.cgi` - Inicjalizacja systemu
- `login.cgi` - Logowanie użytkowników
- `auth.cgi` - Uwierzytelnianie
- `users.cgi` - Zarządzanie użytkownikami
- `companies.cgi` - Zarządzanie firmami
- `employees.cgi` - Zarządzanie pracownikami
- `time_entries.cgi` - Ewidencja czasu
- `qr_scan.cgi` - Skanowanie QR kodów
- `qr_generate.cgi` - Generowanie QR kodów
- `api.cgi` - API główne
- `database.cgi` - Operacje bazodanowe
- `utils.cgi` - Funkcje pomocnicze

### 3. Pliki pomocnicze Python:
- `auth.py` - Moduł uwierzytelniania
- `database.py` - Moduł bazy danych
- `utils.py` - Funkcje pomocnicze

### 4. Pliki frontend:
- `static/` - Cały folder ze stylami i skryptami JS

## 🔧 KROKI WDROŻENIA:

### 1. Upload plików na home.pl:
1. Zaloguj się do panelu home.pl
2. Otwórz WebFTP
3. Przejdź do katalogu `public_html/`
4. Skopiuj **WSZYSTKIE** pliki z folderu `/app/` do `public_html/`
5. Upewnij się, że folder `static/` został skopiowany kompletnie

### 2. Ustawienie uprawnień:
1. Pliki `.cgi` muszą mieć uprawnienia 755 (executable)
2. Pliki `.py` powinny mieć uprawnienia 644
3. Folder `static/` powinien mieć uprawnienia 755

### 3. Pierwsza inicjalizacja:
1. Otwórz przeglądarkę
2. Przetestuj CGI: `https://TWOJA-DOMENA.home.pl/test.py3`
3. Jeśli test działa, uruchom: `https://TWOJA-DOMENA.home.pl/init_simple.py3`
4. Alternatywnie: `https://TWOJA-DOMENA.home.pl/init.py3`
5. Jeśli widzisz komunikat "Database initialized successfully" - GOTOWE!

### 4. Test aplikacji:
1. Otwórz: `https://TWOJA-DOMENA.home.pl/`
2. Sprawdź czy strona się ładuje
3. Kliknij "Zaloguj do panelu"
4. Użyj konta testowego: `owner` / `owner123`

## 👤 DOMYŚLNE KONTA:

Po inicjalizacji dostępne są:
- **owner/owner123** - Administrator systemu (pełny dostęp)
- **admin/admin123** - Administrator firmy (zarządzanie zespołem)
- **user/user123** - Użytkownik firmy (skanowanie QR)

⚠️ **WAŻNE: Zmień hasła po pierwszym logowaniu!**

## 🔍 ROZWIĄZYWANIE PROBLEMÓW:

### Problem: "Forbidden" przy próbie uruchomienia .py3
**Rozwiązanie:**
1. Sprawdź czy pliki `.py3` mają uprawnienia 755 (executable)
2. Sprawdź czy plik `.htaccess` jest wgrany w katalogu głównym
3. Sprawdź czy home.pl obsługuje Python 3 - skontaktuj się z supportem
4. Przetestuj najpierw `test.py3` - jeśli działa, problem z kodem

### Problem: Pliki CGI nie działają
**Rozwiązanie:**
1. Upewnij się, że pliki mają rozszerzenie `.py3` (nie `.cgi`)
2. Sprawdź shebang: `#!/usr/bin/python3`
3. Sprawdź czy wszystkie pliki pomocnicze (auth.py, database.py, utils.py) są wgrane
4. Sprawdź czy wymagane moduły są zainstalowane (bcrypt, PyJWT, qrcode)

### Problem: Błąd CORS
**Rozwiązanie:**
- Upewnij się, że plik `.htaccess` jest w katalogu głównym
- Sprawdź czy wszystkie pliki .py3 mają prawidłowe nagłówki CORS

### Problem: Nie można się zalogować / błędne dane
**Rozwiązanie:**
1. Najpierw uruchom `init_simple.py3` lub `init.py3` aby stworzyć bazę danych
2. Użyj domyślnych kont: `owner/owner123`
3. Sprawdź czy plik `timetracker_pro.db` został utworzony
4. Sprawdź czy wszystkie moduły Python są dostępne

### Problem: Brak modułów Python
**Rozwiązanie:**
1. Sprawdź plik `requirements.txt` - potrzebne: bcrypt, PyJWT, qrcode, pillow
2. Skontaktuj się z supportem home.pl o instalację pakietów
3. Niektóre moduły mogą być już zainstalowane domyślnie

## 🎯 FUNKCJONALNOŚCI SYSTEMU:

### ✅ Zarządzanie użytkownikami:
- Owner: pełny dostęp do systemu
- Admin: zarządzanie swoją firmą
- User: skanowanie QR kodów

### ✅ Ewidencja czasu:
- Automatyczne generowanie QR kodów
- Skanowanie QR kodów (mobile-friendly)
- Rejestracja wejść/wyjść
- Automatyczne liczenie godzin

### ✅ Raporty:
- Podgląd czasu pracy
- Statystyki miesięczne
- Zarządzanie firmami i pracownikami

## 📊 ENDPOINTY API:

Po wdrożeniu aplikacja będzie dostępna pod adresami:
- **Strona główna**: `https://TWOJA-DOMENA.home.pl/`
- **Inicjalizacja**: `https://TWOJA-DOMENA.home.pl/init.cgi`
- **Logowanie**: `https://TWOJA-DOMENA.home.pl/login.cgi`
- **Pracownicy**: `https://TWOJA-DOMENA.home.pl/employees.cgi`
- **QR skanowanie**: `https://TWOJA-DOMENA.home.pl/qr_scan.cgi`

## 🔐 BEZPIECZEŃSTWO:

### ✅ Wbudowane zabezpieczenia:
- JWT tokens z 24h wygaśnięciem
- Bcrypt hashing haseł
- HTTPS wymuszony przez .htaccess
- CORS protection (uniwersalne - działa z każdą domeną)
- Security headers w .htaccess

## 🎉 GOTOWE!

Po wykonaniu powyższych kroków aplikacja TimeTracker Pro będzie w pełni funkcjonalna na hostingu home.pl!

**Rozmiar całego pakietu**: ~3MB
**Czas wdrożenia**: 5-10 minut
**Wymagania**: Standardowy hosting home.pl z obsługą Python 3

---

## 📞 WSPARCIE:

W przypadku problemów:
1. Sprawdź logi błędów w panelu home.pl
2. Upewnij się, że wszystkie pliki zostały skopiowane
3. Przetestuj kolejno: `init.cgi` → strona główna → logowanie

**🚀 APLIKACJA JEST GOTOWA DO WDROŻENIA!**