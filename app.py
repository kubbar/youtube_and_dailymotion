import requests
import sys

# قراءة الرابط من ملف نصي
with open('app_info.txt', 'r') as file:
    config_url = file.read().strip()  # يحذف المسافات البيضاء والأسطر الجديدة

try:
    # جلب بيانات التكوين من Vimeo
    response = requests.get(config_url)
    response.raise_for_status()  # سيقوم بإثارة خطأ إذا كان الطلب ليس 200
    config_data = response.json()

    # استخراج رابط m3u8
    m3u8_url = config_data['request']['files']['hls']['cdns']['fastly_live']['url']

    # جلب محتوى m3u8
    m3u8_response = requests.get(m3u8_url)
    m3u8_response.raise_for_status()

    # كتابة محتوى m3u8 إلى ملف جديد
    with open('app.m3u8', 'w') as m3u8_file:
        m3u8_file.write(m3u8_response.text)

except requests.HTTPError as e:
    print(f'HTTP error: {e}', file=sys.stderr)
except Exception as e:
    print(f'An error occurred: {e}', file=sys.stderr)
