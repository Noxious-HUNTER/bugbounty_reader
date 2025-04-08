#!/bin/bash

# تنظیمات اولیه
echo "📥 Installing BugBounty Reader CLI tool..."

# بررسی اینکه آیا قبلاً نصب شده است یا خیر
if [ -d "bugbounty_reader" ]; then
    echo "🔄 Existing installation found. Updating..."

    # وارد پوشه پروژه شویم
    cd bugbounty_reader

    # بروزرسانی مخزن
    git pull origin main

    # فعال کردن محیط مجازی
    source venv/bin/activate

    # بروزرسانی وابستگی‌ها
    pip install --upgrade -r requirements.txt

    # بروزرسانی اسکریپت
    chmod +x BBreader
    sudo mv BBreader /usr/local/bin/

    echo "✅ Update complete. You can now use BBreader."

else
    # در صورتی که نصب قبلی وجود نداشت
    echo "📥 Installing BugBounty Reader..."

    # کلون کردن مخزن
    git clone https://github.com/YOUR_USERNAME/bugbounty_reader.git
    cd bugbounty_reader

    # ایجاد محیط مجازی
    python3 -m venv venv
    source venv/bin/activate

    # نصب وابستگی‌ها
    pip install -r requirements.txt

    # تغییر دسترسی به اسکریپت BBreader
    chmod +x BBreader

    # انتقال اسکریپت به /usr/local/bin برای دسترسی سراسری
    sudo mv BBreader /usr/local/bin/

    echo "✅ Installation complete. You can now use BBreader."
fi
