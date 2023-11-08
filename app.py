import json
import requests

def lambda_handler(event, context):
    # الرابط الذي يحتوي على بيانات التكوين
    config_url = 'https://player.vimeo.com/video/881909784/config?h=0c1725d19a'

    try:
        # جلب بيانات التكوين من Vimeo
        config_response = requests.get(config_url)
        config_response.raise_for_status()
        config_data = config_response.json()

        # استخراج الرابط الذي يحتوي على ملف .m3u8
        m3u8_url = config_data['request']['files']['hls']['cdns']['fastly_live']['url']

        # جلب محتوى m3u8
        m3u8_response = requests.get(m3u8_url)
        m3u8_response.raise_for_status()

        # إرجاع محتوى m3u8 كاستجابة
        return {
            'statusCode': 200,
            'body': m3u8_response.text,
            'headers': {
                'Content-Type': 'application/vnd.apple.mpegurl'
            }
        }
    except requests.RequestException as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
