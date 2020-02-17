from django import forms
from HMS_Master.models import*


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'emp_name': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'on', 'pattern': '[A-Za-z ]+',
                                               'title': 'Enter your name Characters Only ', 'label': 'Employee name'}),
            'emp_pan_no': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'on',
                                                 'pattern': '[0-9A-Za-z ]+', 'title': 'Enter valid Pan Number '}),
            'emp_age': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 100,
                                                'autocomplete': 'on',
                                                'title': 'Enter valid Age In Numeric form Only Under 1-100 Year'}),

            'emp_gender': forms.Select(attrs={'class': 'form-control'}),
            'emp_email': forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': 'on',
                                                 'title': 'Enter Valid Email ID '}),
            'emp_city': forms.Select(attrs={'class': 'form-control', 'autocomplete': 'on', 'title': 'Select Valid City '}),
        }

    # def clean_emp_pan_no(self):  # Validates the Computer Name Field
    #     emp_pan_no = self.cleaned_data.get('emp_pan_no')
    #     for instance in Employee.objects.all():
    #         if instance.emp_pan_no == emp_pan_no:
    #             raise forms.ValidationError(emp_pan_no + ' is already added')
    #     return emp_pan_no

    def clean_emp_age(self):
        emp_age = self.cleaned_data.get("emp_age")

        if emp_age >= 100:
            raise forms.ValidationError("Age should be greater than 1 and less then 100")
        return emp_age
