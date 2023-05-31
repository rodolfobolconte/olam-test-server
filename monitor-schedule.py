import requests
import time
import urllib3
urllib3.disable_warning()

try:
    response = response.get('http://127.0.0.1:5000')
    print(response.status_code)
    time.sleep(3)
except:
    print('--> Server Error')
    headers = {
        'Authorization': 'Bearer 7tlF7D4aOqf2XWYdAMU7q4EG3pujoL'
    }
    requests.post('https://150.165.80.94/api/v2/job_templates/12/launch/', headers=headers, verify=False)
    time.sleep(7)