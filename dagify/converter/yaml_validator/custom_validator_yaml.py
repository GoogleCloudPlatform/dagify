from yamale.validators import DefaultValidators, Validator
import re

class EmailValidator(Validator):
    tag = 'myemail'  # This is the tag you use in your schema

    email_regex = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'

    def _is_valid(self, value):
        return bool(re.match(self.email_regex, value, re.IGNORECASE))

    def fail(self, value):
        return f'{value} is not a valid email address.'

class UsernameValidator(Validator):
    tag = 'username'  # This is the tag you use in your schema

    username_regex = r'^[a-zA-Z0-9_]+$'

    def _is_valid(self, value):
        return bool(re.match(self.username_regex, value))

    def fail(self, value):
        return f'{value} is not a valid username.'
    
# class MappingsValidator(Validator):
#     tag = 'mappings_valid'  # This is the tag you use in your schema

#     username_regex = r'^[a-zA-Z0-9_]+$'

#     def _is_valid(self, value):
#         return bool(re.match(self.username_regex, value))

#     def fail(self, value):
#         return f'{value} is not a valid username.'

# Extend default validators with your custom validators
validators = DefaultValidators.copy()
validators[EmailValidator.tag] = EmailValidator
validators[UsernameValidator.tag] = UsernameValidator