#!/bin/bash
# 🔧 Skrypt do ustawienia uprawnień dla home.pl
# Uruchom ten skrypt na serwerze home.pl po uploadzie plików

echo "🔧 Ustawianie uprawnień plików dla home.pl..."

# Uprawnienia 755 dla plików .py3 (executable)
echo "📝 Ustawianie uprawnień 755 dla plików .py3..."
chmod 755 *.py3

# Uprawnienia 644 dla pozostałych plików
echo "📝 Ustawianie uprawnień 644 dla pozostałych plików..."
chmod 644 *.py *.html *.json *.txt *.db .htaccess

# Uprawnienia 755 dla folderu static
echo "📝 Ustawianie uprawnień 755 dla folderu static..."
chmod 755 static/
chmod 755 static/*/
chmod 644 static/*/*.* 2>/dev/null || true

echo "✅ Uprawnienia ustawione!"
echo ""
echo "🧪 Przetestuj teraz:"
echo "1. https://TWOJA-DOMENA.home.pl/test.py3"
echo "2. https://TWOJA-DOMENA.home.pl/init_simple.py3"
echo "3. https://TWOJA-DOMENA.home.pl/"
echo ""
echo "🔑 Domyślne konta:"
echo "- owner/owner123"
echo "- admin/admin123"
echo "- user/user123"