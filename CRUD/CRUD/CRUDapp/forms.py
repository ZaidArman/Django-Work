from django import forms
from .models import Student_Entry

class StudentEntryForm(forms.ModelForm):
    class Meta:
        model = Student_Entry
        fields = ['roll_no', 'fname', 'lname', 's_class', 'subject', 'marks']
        
    def clean_fname(self):
        fname = self.cleaned_data['fname']
        if not fname.isalpha():
            raise forms.ValidationError('First Name should contain only alphabetic characters.')
        return fname

    def clean_lname(self):
        lname = self.cleaned_data['lname']
        if not lname.isalpha():
            raise forms.ValidationError('Last Name should contain only alphabetic characters.')
        return lname
    
    def clean_s_class(self):
        s_class = self.cleaned_data['s_class']
        if not s_class.isalpha():
            raise forms.ValidationError('Student Class should contain only alphabetic characters.')
        return s_class
    
    def clean_subject(self):
        subject = self.cleaned_data['subject']
        if not subject.replace(" ", "").isalpha():
            raise forms.ValidationError('Subject should contain only alphabetic characters. ')
        return subject
    
    def clean_marks(self):
        marks = self.cleaned_data['marks']
        if marks > 100:
            raise forms.ValidationError('marks cannot be greater than 100')
        return marks