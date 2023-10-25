import urllib.parse

# الرابط الذي ترغب في استخراج الرابط البصري منه
url = "http://ptc-play.com/portal.php?type=itv&action=create_link&cmd=ffmpeg%20http://localhost/ch/444017_&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml&mac=00:1a:79:00:43:B8"

# استخراج الجزء بعد "cmd=" في الرابط
parsed_url = urllib.parse.urlparse(url)
query_params = urllib.parse.parse_qs(parsed_url.query)
cmd = query_params.get("cmd", [""])[0]

# إزالة "%20" واستبدالها بمساحة فارغة
cmd = cmd.replace(" ", " ")

print(cmd)
