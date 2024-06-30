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
    tag = 'validURL'  # This is the tag you use in your schema
    
    def _is_valid(self, value):
        
        try:
            response = requests.get(value)
            return response.status_code == 200
        except requests.exceptions.RequestException as e:
            print(f"Error checking URL: {e}")
   
# Extend default validators with your custom validators
validators = DefaultValidators.copy()
validators[EmailValidator.tag] = EmailValidator
validators[URLValidator.tag] = URLValidator