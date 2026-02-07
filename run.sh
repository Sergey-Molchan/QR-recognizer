#!/bin/bash
# run.sh - QR Code Reader

echo "🔧 Запуск QR Reader..."

# Активируем виртуальное окружение
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
    echo "✅ Виртуальное окружение активировано"
    echo "Python: $(which python)"
else
    echo "❌ Виртуальное окружение не найдено"
    exit 1
fi

# Настройка для macOS
if [[ "$OSTYPE" == "darwin"* ]]; then
    export DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH"
    export PATH="/opt/homebrew/bin:$PATH"
    echo "✅ Пути для macOS настроены"
fi

# Запускаем
echo "🚀 Запускаем программу..."
echo "══════════════════════════════"
python main.py