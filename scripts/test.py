import json

# الكود JSON
data = 'http://ptc-play.com/portal.php?type=itv&action=create_link&cmd=ffmpeg%20http://localhost/ch/444017_&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml&mac=00:1a:79:00:43:B8'

# تحليل الكود JSON
parsed_data = json.loads(data)

# استخراج الرابط من المفتاح "cmd"
url = parsed_data["js"]["cmd"].split(" ")[1]

print(url)
