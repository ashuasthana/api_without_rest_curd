import requests
import json

BASE_URL="http://127.0.0.1:8000/"
END_POINT="api/"


#For get paticular records via id
def show(id):
    resp=requests.get(BASE_URL + END_POINT+str(id)+'/')
    data=resp.json()
    print(resp.status_code)
    print(data)

#For get all records
def all():
    resp=requests.get(BASE_URL + END_POINT)
    data=resp.json()
    print(resp.status_code)
    print(data)
    
#For create records
def create_resource():
    new_emp={'name':'Ashish Asthana','eno':2,'email':'ashu@gmail.com','esal':35000,}
    resp=requests.post(BASE_URL + END_POINT,data=json.dumps(new_emp))
    print(resp.status_code)
    # print(resp.text)
    print(resp.json)

#For update particular records via id
def update_resource(id):
    new_emp={'name':'Ashish Asthana','email':'ashishasthana@microsoft.com','esal':125000,}
    resp=requests.put(BASE_URL + END_POINT+str(id)+'/',data=json.dumps(new_emp))
    print(resp.status_code)
    # print(resp.json)
    print(resp.text)   

#For delete particular records via id
def del_resource (id):
    resp=requests.delete(BASE_URL + END_POINT+str(id)+'/')
    print(resp.status_code)
    # print(resp.json)
    print(resp.text)       


#******Action via calling functionn  *********
# create_resource()
# all()
# show(1)
# update_resource(1)
del_resource (3)

