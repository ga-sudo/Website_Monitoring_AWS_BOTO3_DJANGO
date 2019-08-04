from influxdb import InfluxDBClient
import time
class Retrieve:
    def __init__(self,user):
        self.user=user
    def access_data(self):
        client=InfluxDBClient(host='52.91.162.31',port=8086)
        client.switch_database('new')
        time.sleep(3);
        print(self.user)
        query="select last(response_time) as rt,last(status_code) as sc from {0}".format(self.user)        
        entry=client.query(query)
        return list(entry.get_points(measurement=self.user))
    
    def get_list_of_response_time(self,cron):
        client=InfluxDBClient(host='52.91.162.31',port=8086)
        time.sleep(3)
        client.switch_database('new')
        query="select response_time from "+self.user;
        entry=list(client.query(query))
        result=[]
        temp=0
        for i in range(0,len(entry[0])):
            abc={}
            temp=temp+int(cron)
            abc['x']=temp
            abc['y']=entry[0][i]['response_time']
            result.append(abc)
        return  result
    
    def get_list_of_status_code(self,cron):
        client=InfluxDBClient(host='52.91.162.31',port=8086)
        time.sleep(3)
        client.switch_database('new')
        query="select status_code from "+self.user;
        entry=list(client.query(query))
        result=[]
        temp=0
        for i in range(0,len(entry[0])):
            abc={}
            temp=temp+int(cron)
            abc['x']=temp
            abc['y']=entry[0][i]['status_code']
            result.append(abc)
        return  result
