import base64
import hashlib
import datetime
import time


def generateSecureLink(secret, url, expiry):
    link = f"{secret}{url}{expiry}"

    hash = hashlib.md5(str(link).encode('utf-8')).digest()
    base64_hash = base64.urlsafe_b64encode(hash)
    str_hash = base64_hash.decode('utf-8').rstrip('=')

    return f"{url}?md5={str_hash}&expires={expiry}"

secret = "1274891274917hd12d"
url = "/file/test.mp3"
date_time = datetime.datetime(2019, 12, 30, 00, 00)
new_expiry = int(time.mktime(date_time.timetuple()))

print(generateSecureLink(secret,url,new_expiry))