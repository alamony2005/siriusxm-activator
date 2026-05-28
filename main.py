import requests
import uuid
import json
import urllib.parse
import sys

def login():
    # login
    # POST https://dealerapp.siriusxm.com/authService/100000002/login

    try:
        params = {"os":deviceiOSVersion,"dm":deviceModel,"did":uuid4,"ua":"iPhone","aid":"DealerApp","aname":"SiriusXM Dealer","chnl":"mobile","plat":"ios","aver":appVer,"atype":"native","stype":"b2c","kuid":"","mfaid":"df7be3dc-e278-436c-b2f8-4cfde321df0a","mfbaseid":"efb9acb6-daea-4f2f-aeb3-b17832bdd47b","mfaname":"DealerApp","sdkversion":"9.5.40","sdktype":"js","sessiontype":"I","clientUUID":"1753190238810-b0b8-58ce-f72e","rsid":"1753213816663-89a7-7c9c-3ea3","svcid":"login_$anonymousProvider"}
        paramsStr = json.dumps(params, separators=(',', ':'))
        response = session.post(
            url="https://dealerapp.siriusxm.com/authService/100000002/login",
            headers={
                "X-Voltmx-Platform-Type": "ios",
                "Accept": "application/json",
                "X-Voltmx-App-Secret": "c086fca8646a72cf391f8ae9f15e5331",
                "Accept-Language": "en-us",
                "X-Voltmx-SDK-Type": "js",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": userAgent,
                "X-Voltmx-SDK-Version": "9.5.40",
                "X-Voltmx-App-Key": "67cfe0220c41a54cb4e768723ad56b41",
                "X-Voltmx-ReportingParams": urllib.parse.quote(paramsStr, safe='$:,'),
            },
        )
        return response.json().get('claims_token').get('value')
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        #print('Response HTTP Response Body: {content}'.format(
        #    content=response.content))
    except Exception:
        print('HTTP Request failed')


def getProperties():
    # getProperties
    # POST https://dealerapp.siriusxm.com/services/USNewGetProperties/getProperties

    try:
        params = {"os":deviceiOSVersion,"dm":deviceModel,"did":uuid4,"ua":"iPhone","aid":"DealerApp","aname":"SiriusXM Dealer","chnl":"mobile","plat":"ios","aver":appVer,"atype":"native","stype":"b2c","kuid":"","mfaid":"df7be3dc-e278-436c-b2f8-4cfde321df0a","mfbaseid":"efb9acb6-daea-4f2f-aeb3-b17832bdd47b","mfaname":"DealerApp","sdkversion":"9.5.40","sdktype":"js","fid":"frmHome","sessiontype":"I","clientUUID":"1753190238810-b0b8-58ce-f72e","rsid":"1753213816663-89a7-7c9c-3ea3","svcid":"getProperties"}
        paramsStr = json.dumps(params, separators=(',', ':'))
        response = session.post(
            url=
            "https://dealerapp.siriusxm.com/services/USNewGetProperties/getProperties",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": userAgent,
                "X-Voltmx-Authorization": auth_token,
                "X-Voltmx-ReportingParams": urllib.parse.quote(paramsStr, safe='$:,'),
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        #print('Response HTTP Response Body: {content}'.format(
        #    content=response.content))
    except Exception:
        print('HTTP Request failed')


def ESNRefreshComposite():
    # ESNRefreshComposite
    # POST https://dealerapp.siriusxm.com/services/USPartnerAppRefreshComposite/ESNRefreshComposite

    try:
        params = {"os":deviceiOSVersion,"dm":deviceModel,"did":uuid4,"ua":"iPhone","aid":"DealerApp","aname":"SiriusXM Dealer","chnl":"mobile","plat":"ios","aver":appVer,"atype":"native","stype":"b2c","kuid":"","mfaid":"df7be3dc-e278-436c-b2f8-4cfde321df0a","mfbaseid":"efb9acb6-daea-4f2f-aeb3-b17832bdd47b","mfaname":"DealerApp","sdkversion":"9.5.40","sdktype":"js","fid":"frmRadioRefresh","sessiontype":"I","clientUUID":"1753190238810-b0b8-58ce-f72e","rsid":"1753213816663-89a7-7c9c-3ea3","svcid":"ESNRefreshComposite"}
        paramsStr = json.dumps(params, separators=(',', ':'))
        response = session.post(
            url=
            "https://dealerapp.siriusxm.com/services/USPartnerAppRefreshComposite/ESNRefreshComposite",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": userAgent,
                "X-Voltmx-Authorization": auth_token,
                "X-Voltmx-ReportingParams": urllib.parse.quote(paramsStr, safe='$:,'),
            },
            data={
                "deviceId": radio_id_input,
                "appVersion": appVer,
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except Exception:
        print('HTTP Request failed')

def VINRefreshComposite():
    # VINRefreshComposite
    # POST https://dealerapp.siriusxm.com/services/USPartnerAppRefreshComposite/VINRefreshComposite

    try:
        params = {"os":deviceiOSVersion,"dm":deviceModel,"did":uuid4,"ua":"iPhone","aid":"DealerApp","aname":"SiriusXM Dealer","chnl":"mobile","plat":"ios","aver":appVer,"atype":"native","stype":"b2c","kuid":"","mfaid":"df7be3dc-e278-436c-b2f8-4cfde321df0a","mfbaseid":"efb9acb6-daea-4f2f-aeb3-b17832bdd47b","mfaname":"DealerApp","sdkversion":"9.5.40","sdktype":"js","fid":"frmRadioRefresh","sessiontype":"I","clientUUID":"1753190238810-b0b8-58ce-f72e","rsid":"1753213816663-89a7-7c9c-3ea3","svcid":"VINRefreshComposite"}
        paramsStr = json.dumps(params, separators=(',', ':'))
        response = session.post(
            url=
            "https://dealerapp.siriusxm.com/services/USPartnerAppRefreshComposite/VINRefreshComposite",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": userAgent,
                "X-Voltmx-Authorization": auth_token,
                "X-Voltmx-ReportingParams": urllib.parse.quote(paramsStr, safe='$:,'),
            },
            data={
                "vin": radio_id_input,
                "appVersion": appVer,
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except Exception:
        print('HTTP Request failed')

# Global variables used for requests
radio_id_input = input("Enter Radio ID or VIN: ").upper()
uuid4 = str(uuid.uuid4())
auth_token = ""
deviceModel = "iPhone 14 Pro"
deviceiOSVersion = "17.0"
appVer = "3.3.0"
userAgent = "SiriusXM%20Dealer/3.3.0 CFNetwork/1568.200.51 Darwin/24.1.0"

session = requests.Session()

if len(radio_id_input) == 17:
    # VIN Activiation
    print("login")
    auth_token = login()
    print("getProperties")
    getProperties()
    print("VINRefreshComposite")
    VINRefreshComposite()
elif len(radio_id_input) == 8 or len(radio_id_input) == 12:
    # Radio ID Activation
    print("login")
    auth_token = login()
    print("getProperties")
    getProperties()
    print("ESNRefreshComposite")
    ESNRefreshComposite()
else:
    print("The VIN/Radio ID you entered is incorrect. Radio IDs are either 8 characters or 12 digits long and VINs are 17 characters long.")