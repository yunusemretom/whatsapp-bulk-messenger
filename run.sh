#!/bin/bash
# macOS/Linux için otomatik başlatıcı

# Python yüklü mü kontrol et
if ! command -v python3 &> /dev/null; then
    echo "Python3 yüklü değil. Lütfen Python3 kurun."
    exit 1
fi

# Gerekli paketler yüklü mü kontrol et
python3 -m pip show PySide6 > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Gerekli paketler yükleniyor..."
    python3 -m pip install -r requirements.txt
fi

# Uygulamayı başlat
python3 main.py
