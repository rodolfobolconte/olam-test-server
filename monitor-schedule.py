import requests
import time
import urllib3
# urllib3.disable_warning()

try:
    response = response.get('http://127.0.0.1:5000')
    print(response.status_code)
    time.sleep(3)
except:
    print('--> Server Error')
    headers = {
        'Authorization': 'Bearer mvPPNToAjhHhhD4Adljiqj8dZ2TI9h'
    }
    requests.post('https://192.168.1.15/api/v2/job_templates/12/launch/', headers=headers, verify=False)
    time.sleep(7)