from __future__ import division
import time
import os
import boto3
from botocore.vendored import requests

# url=os.getenv('url')
# res = requests.head(url)
# status_code_check=int(os.getenv('status'))

def listf(event,context):
    url=os.getenv('url')
    status_code_check=int(os.getenv('status'))

    final_output = []

    default_request_body = {
    'url': '',
    'params': {},
    'headers': {},
    'data': {},
    'timeout' : 60,
    'allow_redirects': True,
    }

    default_response_body = {
    'status_code': 700,
    'url': '',
    'headers':{},
    'elapsed': -1
    }

    default_output = {
    'status':False,
    'message': 'Failed',
    'method': 'GET',
    'request_body': default_request_body,
    'response_body': default_response_body 
    }


    try:
        params = default_request_body['params']
        headers = default_request_body['headers']
        data = default_request_body['data']
        timeout = default_request_body['timeout']
        allow_redirects = default_request_body['allow_redirects']
        response = requests.get(url=url, params=params, headers=headers, data=data, timeout=timeout, allow_redirects=allow_redirects)
        default_output['status'] = True
        default_output['message'] = 'Success'
        default_response_body['status_code'] = response.status_code
        default_response_body['url'] = response.url
        default_response_body['headers'] = response.headers,
        default_response_body['elapsed'] = response.elapsed.total_seconds()
        if (status_code_check==response.status_code):
            print ("Valid")
        else:
            print ("Invalid")
        #     sns_client=boto3.client('sns')
        #     message="your website status is "+str(check) +" and response time is = "+str(requests.post(url).elapsed.total_seconds())
        #     send=sns_client.publish(TargetArn='arn:aws:sns:us-east-1:754068459088:yash',Message=message,Subject='pingdom')
        # print (requests.post(url).elapsed.total_seconds())

        return default_output
    except Exception as e:
        print(e)
        return default_output
    


# def my_request(url, params, headers, data, timeout, allow_redirects):
  