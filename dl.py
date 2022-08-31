import sys, os
from skillshare import Skillshare, splash


# or by class ID:
# dl.download_course_by_class_id(189505397)

cookie = f"""
    muted=true; muted=true; PHPSESSID={sys.argv[2]}; _tt_enable_cookie=1; _ttp=93fd4540-e29c-429b-8fca-27314903579a; G_ENABLED_IDPS=google; __ssid=6f611175042417736ac6778acf03a67; show-like-copy=1; YII_CSRF_TOKEN=TDg2MGFVSzF1WEdrMjI4MTl1ZHpNVkZxSGRyTmd0MWIqLDsATVuYxdX8P-3G-v_Z-aHrFp9E9i09lZHgBYlU1w%3D%3D; ss_hide_default_banner=1661068554.966; __stripe_mid=b7a9c866-771c-4351-9c78-3c5b2840aefbf1b96d; accept_language=en-US; device_session_id=449d81c1-141a-4d94-a927-a237ceb41e76; first_landing=utm_campaign%3D%26utm_source%3D%26utm_medium%3D%26utm_term%3D%26referrer%3Dhttps%3A%2F%2Fwww.google.com%2F%26referring_username%3D; ss-ref=%7B%22student%22%3A9257408%2C%22teacher%22%3A%7B%226595003%22%3A%7B%22classId%22%3Anull%2C%22referralType%22%3A%22affiliate%22%7D%7D%7D; _gcl_au=1.1.2120866914.1661949172; _pin_unauth=dWlkPU5qWm1NVE15WmpVdE9UWTFPUzAwT1dZd0xUazRObVl0WmpkaU5tWmlNVFUwWkRKbQ; __pdst=76895264485e4644ae3d166684891345; IR_gbd=skillshare.com; __utmc=99704988; __utmz=99704988.1661949176.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=99704988.|1=visitor-type=user=1; sm_uuid=1661949556614; _gid=GA1.2.578676110.1661949398; _clck=totzh3|1|f4h|0; visitor_tracking=utm_campaign=student-referral-settings&utm_source=ShortUrl&utm_medium=student-referral-general&utm_term=&referrer=&referring_username=485104674; __utma=99704988.1391556367.1661949174.1661949176.1661953023.2; __utmt=1; _uetsid=ff42b100292811edb249eb0553597f99; _uetvid=ff43c690292811ed8714df87bb5f6da8; __utmb=99704988.3.10.1661953023; IR_4650=1661953086507%7C0%7C1661953086507%7C%7C; IR_PI=9aa72ba3-1c48-3056-98ba-872cee535584%7C1662039486507; _clsk=1kus5fk|1661953089045|9|0|n.clarity.ms/collect; _ga=GA1.1.1391556367.1661949174; _ga_J5NPJ1XD74=GS1.1.1661949156.1.1.1661953118.0.0.0; ss-subscription-coupon=referral2m
"""
def main():
    dl = Skillshare(cookie)
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


if __name__ == "__main__":
    splash()
    main()
