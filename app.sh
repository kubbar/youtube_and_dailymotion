#!/bin/bash

# تأكد من أن السكريبت يتم تنفيذه في المجلد الذي يحتوي على app.py و app_info.txt
cd "$(dirname "$0")"

# تنفيذ السكريبت البايثوني وتوجيه الإخراج إلى ملف m3u8
python3 app.py

# التحقق من نجاح العملية
if [[ $? -eq 0 ]]; then
    echo "M3U8 grabbed successfully."
else
    echo "Failed to grab M3U8."
fi
