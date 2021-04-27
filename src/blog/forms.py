from django import forms
from django.contrib.auth import get_user_model

# from captcha.fields  import CaptchaField  # add a Simple Captcha field

#email sending
from django.core.mail import send_mail
from django.core.mail import EmailMessage


from django.conf import settings


from django.urls import reverse

# from ecommerce.settings import SITE_URL

User = get_user_model()


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your full name"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your email"
            }
        )
    )
    subject = forms.CharField(widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your Subject"
            }
        )
        
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                "placeholder": "Your message"
            }
        )
    
    )

    # captcha = CaptchaField()
    # success_url = '/thanks/'

   
    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     # if not "gmail.com" in email:
    #     #     raise forms.ValidationError("Email has to be gmail.com")
    #     return email

    # Call this method after the form is validated
    def send_email(self):
        # origin = settings.SITE_URL + reverse('contact')

        # subject = '[ContactForm] from %s' %origin


        sender = settings.SENDER
        receipients = settings.RECEIVERS

        subject=self.cleaned_data['subject'] + ' [CONTACTFORM] ' + SITE_URL
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        body = """
        Name: %s
        Email: %s
        Content: %s
        """ %(name, email, message,)

        email = EmailMessage(subject,body,
            from_email = sender,
            to = receipients,
            #bcc = ['bcc@anotherbestuser.com'],
            reply_to = [email],
            )



        

        response = 0
      
        # try:
        #     response = send_mail(
        #         subject,
        #         body,
        #         sender,
        #         receipients,
        #         fail_silently=False,
        #         #auth_user='no_such_user',  # uncomment this line to test for a failed send_mail()
        #     )
        try:
            response = email.send()
           
            
        except Exception as ex:
            print("====ERR EMAIL EXCEPTION:" ,ex)

        return response