import json
import os
import subprocess

def merge_writeups(new_writeups, existing_file='data/writeups.json'):
    # اگر فایل وجود نداشت، یکی جدید بساز
    if not os.path.exists(existing_file):
        with open(existing_file, 'w') as f:
            json.dump(new_writeups, f, indent=4)
        print(f"✅ {existing_file} created with new writeups.")
        return

    # بارگذاری رایتاپ‌های قبلی
    with open(existing_file, 'r') as f:
        existing_writeups = json.load(f)

    # افزودن رایتاپ‌های جدید
    for new_writeup in new_writeups:
        # بررسی اینکه آیا رایتاپ قبلاً وجود داشته یا نه
        if new_writeup not in existing_writeups:
            existing_writeups.append(new_writeup)

    # ذخیره داده‌ها به فایل
    with open(existing_file, 'w') as f:
        json.dump(existing_writeups, f, indent=4)
    
    print(f"✅ Merged new writeups into {existing_file}")

def extract_new_writeups():
    # این تابع فقط مثالی است و شما می‌توانید استخراج داده‌های جدید خود را در اینجا قرار دهید.
    # اینجا فرض می‌کنیم که با سایت PentesterLand داده‌ها را می‌گیریم.
    new_writeups = [
        {
            "title": "New XSS Writeup",
            "url": "https://example.com/xss-writeup",
            "description": "XSS vulnerability",
            "date": "2025-04-10",
            "source": "pentesterland",
            "tags": ["xss"]
        },
        {
            "title": "New SSRF Writeup",
            "url": "https://example.com/ssrf-writeup",
            "description": "SSRF vulnerability",
            "date": "2025-04-10",
            "source": "pentesterland",
            "tags": ["ssrf"]
        }
    ]
    return new_writeups

def main():
    new_writeups = extract_new_writeups()  # اینجا رایتاپ‌های جدید رو می‌گیریم
    merge_writeups(new_writeups)  # مرج کردن رایتاپ‌های جدید با رایتاپ‌های قبلی

if __name__ == "__main__":
    main()
