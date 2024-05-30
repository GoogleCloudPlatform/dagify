from yamale.validators import DefaultValidators, Validator
import re
import requests

class EmailValidator(Validator):
    tag = 'myEmailValidator'  # This is the tag you use in your schema

    email_regex = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'

    def _is_valid(self, value):
        return bool(re.match(self.email_regex, value, re.IGNORECASE))

    def fail(self, value):
        return f'{value} is not a valid email address.'

class URLValidator(Validator):
    tag = 'myURLValidator'  # This is the tag you use in your schema
    
    def _is_valid(self, value):
        response = requests.get(value)
        #add url code here 200
        if response.status_code == 200:
            return f'{value} is valid'

    def fail(self, value):
        response = requests.get(value)
        if response.status_code != 200:
            return f'{value} is not a valid url'
        
# Extend default validators with your custom validators
validators = DefaultValidators.copy()
validators[EmailValidator.tag] = EmailValidator
validators[URLValidator.tag] = URLValidator