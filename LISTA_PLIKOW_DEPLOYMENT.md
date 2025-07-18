# 📋 LISTA PLIKÓW DO WDROŻENIA NA HOME.PL

## 🎯 WSZYSTKIE PLIKI DO SKOPIOWANIA NA WEBFTP:

### 1. Pliki główne (katalog główny):
- `.htaccess` - Konfiguracja Apache (KRYTYCZNY!)
- `index.html` - Strona główna aplikacji
- `timetracker_pro.db` - Baza danych SQLite
- `asset-manifest.json` - Manifest aplikacji

### 2. Pliki CGI (Backend - rozszerzenie .cgi):
- `api.cgi` - API główne
- `auth.cgi` - Uwierzytelnianie
- `companies.cgi` - Zarządzanie firmami
- `database.cgi` - Operacje bazodanowe
- `employees.cgi` - Zarządzanie pracownikami
- `init.cgi` - Inicjalizacja systemu (URUCHOM TO PIERWSZE!)
- `login.cgi` - Logowanie użytkowników
- `qr_generate.cgi` - Generowanie QR kodów
- `qr_scan.cgi` - Skanowanie QR kodów
- `time_entries.cgi` - Ewidencja czasu
- `users.cgi` - Zarządzanie użytkownikami
- `utils.cgi` - Funkcje pomocnicze

### 3. Pliki pomocnicze Python:
- `auth.py` - Moduł uwierzytelniania
- `database.py` - Moduł bazy danych
- `utils.py` - Funkcje pomocnicze

### 4. Folder statyczny (skopiuj CAŁY folder):
- `static/` - Zawiera:
  - `static/css/` - Style CSS
  - `static/js/` - Skrypty JavaScript

## 🔧 UPRAWNIENIA PLIKÓW:

### Uprawnienia 755 (executable):
- Wszystkie pliki `.cgi`
- Folder `static/`

### Uprawnienia 644 (readable):
- Wszystkie pliki `.py`
- Wszystkie pliki `.html`
- Wszystkie pliki `.json`
- Plik `.htaccess`
- Plik `.db`

## 🚀 KOLEJNOŚĆ WDROŻENIA:

1. **Skopiuj wszystkie pliki** z listy powyżej
2. **Ustaw uprawnienia** zgodnie z instrukcjami
3. **Uruchom inicjalizację**: `https://TWOJA-DOMENA.home.pl/init.cgi`
4. **Przetestuj aplikację**: `https://TWOJA-DOMENA.home.pl/`
5. **Zaloguj się**: `owner` / `owner123`

## ⚠️ WAŻNE UWAGI:

- **NIE ZAPOMNIJ** o pliku `.htaccess` - bez niego aplikacja nie będzie działać!
- **Folder `static/`** musi być skopiowany kompletnie ze wszystkimi podfolderami
- **Pliki `.cgi`** muszą mieć uprawnienia executable (755)
- **Pierwszym krokiem** po wdrożeniu jest uruchomienie `init.cgi`

## 📊 PODSUMOWANIE:

**Liczba plików do skopiowania**: ~19 plików + folder static/
**Całkowity rozmiar**: ~3MB
**Czas wdrożenia**: 5-10 minut
**Wymagania**: hosting home.pl z Python 3

**🎉 WSZYSTKO GOTOWE DO WDROŻENIA!**