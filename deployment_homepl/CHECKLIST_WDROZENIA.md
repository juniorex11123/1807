# ✅ CHECKLIST WDROŻENIA - TIMETRACKER PRO

## 📋 PRZED WDROŻENIEM

- [ ] Mam dostęp do panelu home.pl
- [ ] Mam dostęp do WebFTP
- [ ] Sprawdziłem czy home.pl obsługuje Python 3
- [ ] Skopiowałem cały folder deployment_homepl

## 🚀 WDROŻENIE KROK PO KROKU

### 1. Upload plików
- [ ] Zalogowałem się do panelu home.pl
- [ ] Otworzyłem WebFTP
- [ ] Przeszedłem do katalogu `public_html/`
- [ ] Skopiowałem **WSZYSTKIE** pliki z `deployment_homepl/` do `public_html/`
- [ ] Sprawdziłem czy folder `static/` został skopiowany kompletnie

### 2. Ustawienie uprawnień
**Opcja A: Automatycznie (jeśli masz SSH)**
- [ ] Uruchomiłem: `bash set_permissions.sh`

**Opcja B: Ręcznie przez WebFTP**
- [ ] Ustawiłem uprawnienia 755 dla wszystkich plików .py3
- [ ] Ustawiłem uprawnienia 644 dla pozostałych plików
- [ ] Ustawiłem uprawnienia 755 dla folderu static/

### 3. Testowanie CGI
- [ ] Otworzyłem: `https://TWOJA-DOMENA.home.pl/test.py3`
- [ ] Zobaczyłem komunikat: "Test CGI na home.pl"
- [ ] ✅ CGI działa poprawnie

### 4. Inicjalizacja systemu
- [ ] Otworzyłem: `https://TWOJA-DOMENA.home.pl/init_simple.py3`
- [ ] Zobaczyłem: `{"message": "Database initialized successfully"}`
- [ ] ✅ System zainicjalizowany

### 5. Test aplikacji
- [ ] Otworzyłem: `https://TWOJA-DOMENA.home.pl/`
- [ ] Aplikacja się załadowała poprawnie
- [ ] ✅ Frontend działa

### 6. Test logowania
- [ ] Kliknąłem "Zaloguj się" lub przeszedłem do panelu logowania
- [ ] Użyłem konta: `owner` / `owner123`
- [ ] Zalogowałem się pomyślnie
- [ ] ✅ Logowanie działa

### 7. Test funkcji (opcjonalnie)
- [ ] Sprawdziłem zarządzanie użytkownikami
- [ ] Sprawdziłem zarządzanie firmami
- [ ] Sprawdziłem zarządzanie pracownikami
- [ ] Sprawdziłem ewidencję czasu
- [ ] ✅ Wszystkie funkcje działają

## 🔧 ROZWIĄZYWANIE PROBLEMÓW

### Problem: "Forbidden" przy test.py3
**Sprawdź:**
- [ ] Plik test.py3 ma uprawnienia 755
- [ ] Plik .htaccess jest wgrany
- [ ] Home.pl obsługuje Python 3

### Problem: "Internal Server Error"
**Sprawdź:**
- [ ] Wszystkie pliki .py są wgrane
- [ ] Wymagane pakiety Python są zainstalowane
- [ ] Użyj `init_simple.py3` zamiast `init.py3`

### Problem: Nie działa logowanie
**Sprawdź:**
- [ ] Uruchomiłem najpierw `init_simple.py3`
- [ ] Użyj `login_simple.py3` zamiast `login.py3`
- [ ] Plik `timetracker_pro.db` został wgrany

### Problem: Brak pakietów Python
**Zrób:**
- [ ] Skontaktuj się z supportem home.pl
- [ ] Poproś o instalację: bcrypt, PyJWT, qrcode, pillow

## 📞 WSPARCIE

Jeśli masz problemy:
1. Sprawdź logi błędów w panelu home.pl
2. Upewnij się, że wszystkie pliki zostały skopiowane
3. Przetestuj kolejno: test.py3 → init_simple.py3 → strona główna → logowanie
4. Skontaktuj się z supportem home.pl o wymagane pakiety Python

## 🎯 DOMYŚLNE KONTA

Po pomyślnym wdrożeniu dostępne konta:
- **owner** / **owner123** - Administrator systemu
- **admin** / **admin123** - Administrator firmy
- **user** / **user123** - Pracownik

⚠️ **WAŻNE: Zmień hasła po pierwszym logowaniu!**

## 🎉 GOTOWE!

Jeśli wszystkie punkty są zaznaczone ✅, aplikacja TimeTracker Pro jest gotowa do użycia!

**Powodzenia! 🚀**