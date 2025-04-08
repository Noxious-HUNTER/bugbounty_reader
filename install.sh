#!/bin/bash

# نصب ابزار BugBounty Reader CLI
echo "📥 Installing BugBounty Reader CLI tool..."

# کلون کردن مخزن از گیت‌هاب
git clone https://github.com/Noxious-HUNTER/bugbounty_reader.git

cd bugbounty_reader || exit

# نصب وابستگی‌ها
echo "📥 Installing dependencies from requirements.txt..."
sudo pip3 install -r requirements.txt  # اضافه کردن sudo برای نصب در سیستم

# کپی کردن اسکریپت BBreader به /usr/local/bin
echo "📥 Installing BBreader CLI command..."
chmod +x BBreader.py
sudo mv BBreader.py /usr/local/bin/BBreader  # اضافه کردن sudo برای کپی فایل

# بررسی نصب درست
if ! command -v BBreader &> /dev/null
then
    echo "❌ Failed to install BBreader. Please check permissions."
    exit 1
fi

# نصب کامل شد
echo "✅ Installation complete. You can now use BBreader from anywhere in the terminal."
