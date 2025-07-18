# 📋 LISTA PLIKÓW DO WDROŻENIA NA HOME.PL

## 🎯 WSZYSTKIE PLIKI DO SKOPIOWANIA NA WEBFTP:

### 1. Pliki główne (katalog główny):
- `.htaccess` - Konfiguracja Apache (KRYTYCZNY!)
- `index.html` - Strona główna aplikacji
- `timetracker_pro.db` - Baza danych SQLite
- `asset-manifest.json` - Manifest aplikacji

### 2. Pliki CGI (Backend - rozszerzenie .py3):
- `api.py3` - API główne
- `auth.py3` - Uwierzytelnianie
- `companies.py3` - Zarządzanie firmami
- `database.py3` - Operacje bazodanowe
- `employees.py3` - Zarządzanie pracownikami
- `init.py3` - Inicjalizacja systemu (URUCHOM TO PIERWSZE!)
- `init_simple.py3` - Alternatywna inicjalizacja (jeśli init.py3 nie działa)
- `login.py3` - Logowanie użytkowników
- `login_simple.py3` - Alternatywne logowanie (jeśli login.py3 nie działa)
- `qr_generate.py3` - Generowanie QR kodów
- `qr_scan.py3` - Skanowanie QR kodów
- `time_entries.py3` - Ewidencja czasu
- `users.py3` - Zarządzanie użytkownikami
- `utils.py3` - Funkcje pomocnicze
- `test.py3` - Plik testowy CGI

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
- Wszystkie pliki `.py3`
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