import requests
import re

# استبدل هذا بمسار ملف app_info.txt الخاص بك
config_url_path = 'app_info.txt'

with open(config_url_path, 'r') as file:
    config_url = file.read().strip()

response = requests.get(config_url)
response.raise_for_status()
config_data = response.json()

# استخرج الـ URL الأساسي من الرابط الذي يحتوي على ملف `.m3u8`
m3u8_url = config_data['request']['files']['hls']['cdns']['fastly_live']['url']
base_url = re.match(r'https?://[^/]+/', m3u8_url).group(0)

m3u8_response = requests.get(m3u8_url)
m3u8_response.raise_for_status()
m3u8_content = m3u8_response.text

# استبدل جميع المسارات النسبية بمسارات مطلقة باستخدام الـ base_url
updated_m3u8_content = re.sub(r'chunklist_b(\d+).m3u8', base_url + r'chunklist_b\1.m3u8', m3u8_content)

with open('app.m3u8', 'w') as m3u8_file:
    m3u8_file.write(updated_m3u8_content)
