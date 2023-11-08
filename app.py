from flask import Flask, redirect, request, Response
import requests

app = Flask(__name__)

@app.route('/get_m3u8')
def get_m3u8():
    config_url = 'https://player.vimeo.com/video/881909784/config?h=0c1725d19a'
    try:
        # جلب بيانات التكوين من Vimeo
        config_response = requests.get(config_url)
        config_response.raise_for_status()  # سيقوم بإثارة خطأ إذا كان الطلب ليس 200
        config_data = config_response.json()

        # استخراج رابط m3u8 من بيانات التكوين
        m3u8_url = config_data['request']['files']['hls']['cdns']['fastly_live']['url']

        # جلب محتوى m3u8 من الرابط المستخرج
        m3u8_response = requests.get(m3u8_url)
        m3u8_response.raise_for_status()
        m3u8_content = m3u8_response.text

        # إرجاع المحتوى مباشرةً كاستجابة
        return Response(m3u8_content, mimetype='application/vnd.apple.mpegurl')
    except requests.HTTPError as http_err:
        return f'HTTP error occurred: {http_err}', 500
    except Exception as err:
        return f'Other error occurred: {err}', 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
