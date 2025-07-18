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
2. Idź do: `https://TWOJA-DOMENA.home.pl/init.cgi`
3. Jeśli widzisz komunikat "Database initialized successfully" - GOTOWE!

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

### Problem: Pliki CGI nie działają
**Rozwiązanie:**
1. Sprawdź czy pliki `.cgi` mają uprawnienia 755
2. Sprawdź czy plik `.htaccess` został wgrany
3. Upewnij się, że home.pl obsługuje Python 3

### Problem: Błąd CORS
**Rozwiązanie:**
- Upewnij się, że plik `.htaccess` jest w katalogu głównym
- Sprawdź czy wszystkie pliki CGI mają prawidłowe nagłówki CORS

### Problem: Nie można się zalogować
**Rozwiązanie:**
1. Najpierw uruchom `init.cgi` aby stworzyć bazę danych
2. Użyj domyślnych kont: `owner/owner123`
3. Sprawdź czy `timetracker_pro.db` został utworzony

### Problem: Strona nie ładuje się
**Rozwiązanie:**
1. Sprawdź czy `index.html` jest w katalogu głównym
2. Sprawdź czy folder `static/` został skopiowany kompletnie
3. Sprawdź czy plik `.htaccess` jest wgrany

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