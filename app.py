from urllib.parse import urlparse, urlunparse
import requests

# استبدل هذا بمسار ملف app_info.txt الخاص بك
config_url_path = 'app_info.txt'

with open(config_url_path, 'r') as file:
    config_url = file.read().strip()

response = requests.get(config_url)
response.raise_for_status()
config_data = response.json()

# استخرج الـ URL الأساسي لـ m3u8
m3u8_url = config_data['request']['files']['hls']['cdns']['fastly_live']['url']
parsed_url = urlparse(m3u8_url)

# أزل الجزء الأخير من الـ path (filename) للحصول على الـ base URL
base_path = '/'.join(parsed_url.path.split('/')[:-1]) + '/'
base_url = urlunparse(parsed_url._replace(path=base_path))

m3u8_response = requests.get(m3u8_url)
m3u8_response.raise_for_status()
m3u8_content = m3u8_response.text

# إضافة الـ base URL إلى كل chunklist في المحتوى
m3u8_content = m3u8_content.replace('chunklist', base_url + 'chunklist')

with open('app.m3u8', 'w') as m3u8_file:
    m3u8_file.write(m3u8_content)
