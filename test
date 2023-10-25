from flask import Flask, request, jsonify

app = Flask(__name__)

# قم بتخزين رابط الفيديو في المتغير التالي
video_url = "http://ptc-play.com:80/play/live.php?mac=00:1a:79:00:43:B8&stream=444017&extension=ts"

# يمكنك تخزين الرمز المميز في المتغير التالي
token = "57BEFAB1CF9D38C02540482977602D10"

@app.route('/play_video', methods=['GET'])
def play_video():
    # التحقق من صحة الرمز المرفق في الطلب
    received_token = request.args.get('token')

    if received_token == token:
        return f" <video controls autoplay><source src='{video_url}'></video>"
  
    return "Invalid token"

if __name__ == '__main__':
    app.run()
