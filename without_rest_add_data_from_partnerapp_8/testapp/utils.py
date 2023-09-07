import json
from .models import Employee

#Check data formate is json or not
def is_json(data):
    try:
        real_data=json.loads(data)
        valid=True
    except ValueError:
        valid=False
    return valid    

#Return object via id 
def get_obj_by_id(id):
        try:
            obj=Employee.objects.get(id=id)
        except Employee.DoesNotExist:   
             obj=None 
             return obj
        else:     
            return obj