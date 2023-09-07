from django.shortcuts import render
from django.views import View
from .models import Employee
from .forms import EmployeeApiForm
import json
from .utils import is_json,get_obj_by_id
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.mixin import HttpResponseMixin,SerializeMixin

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeListlCBV(HttpResponseMixin,SerializeMixin,View):
    #For get all records
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        json_data=self.serialize(qs)
        return self.render_to_http_response(json_data)
    
    #For Add record from partner application
    def post(self,request,*args,**kwargs): 
        #Partner app data 
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json data only.'})
            return self.render_to_http_response(json_data,400)
        empdata=json.loads(data)
        form=EmployeeApiForm(empdata)    
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Resource created successfully.'})
            return self.render_to_http_response(json_data)


# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeDetailCBV(HttpResponseMixin,SerializeMixin,View):

    #For get paticular records
    def get(self,request,id,*args,**kwargs):
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:   
            json_data=json.dumps({'msg':'Specific Record Not Found.'})
            return self.render_to_http_response(json_data,status=403) 
        else:     
            json_data=self.serialize([emp,])
            return self.render_to_http_response(json_data)  
    
    #For update paticular records
    def put(self,request,id,*args,**kwargs):
        emp=get_obj_by_id(id)
        if emp==None: 
            json_data=json.dumps({'msg':'Specific Record Not Found.'})
            return self.render_to_http_response(json_data,status=403) 
    
        data=request.body
        data_json=is_json(data)
        if not data_json:
            json_data=json.dumps({'msg':'Please send json data only.'})
            return self.render_to_http_response(json_data,status=403)
        new_data=json.loads(data)
        old_data={
            'name':emp.name,
            'eno':emp.eno,
            'email':emp.email,
            'esal':emp.esal,
        }
        old_data.update(new_data)
        # json_data=json.dumps(old_data)
        form=EmployeeApiForm(old_data,instance=emp)
        if form.is_valid:
            form.save(commit=True)
            json_data=json.dumps({'msg':'Updated Successfully.'})
            return self.render_to_http_response(json_data) 
            
    #For Delete paticular records
    def delete(self,request,id,*args,**kwargs):
        emp_obj=get_obj_by_id(id)
        if emp_obj==None: 
            json_data=json.dumps({'msg':'Specific Record Not Found.'})
            return self.render_to_http_response(json_data,status=403)  
        status,deleted_item=emp_obj.delete()
        print(deleted_item)
        if status==1:
            json_data=json.dumps({'msg':'Data Deleted Successfully.'})
            return self.render_to_http_response(json_data)   
        json_data=json.dumps({'msg':'Data is not Deleted Please try after sometime.'})
        return self.render_to_http_response(json_data) 


