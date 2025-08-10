#!/usr/bin/env bash
# setup.sh — поэтапная установка тяжёлых пакетов

echo "1/3: Установка базовых пакетов..."
pip install -r requirements.txt

echo "2/3: Установка torch без CUDA..."
pip install torch --index-url https://download.pytorch.org/whl/cpu

echo "3/3: Установка chromadb и эмбеддингов..."
pip install chromadb
pip install sentence-transformers

echo "✅ Установка завершена!"

# Запуск бота
echo "🚀 Запуск ingest.py..."
python ingest.py

echo "🚀 Запуск bot.py..."
python bot.py