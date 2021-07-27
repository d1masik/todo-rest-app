import re
import warnings

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.deprecation import RemovedInDjango41Warning
from django.utils.encoding import punycode
from django.utils.translation import gettext_lazy as _
from django.core import validators


class FirstCapitalLetterValidator:
    def validate(self, password, user=None):
        if not re.search('[A-Z]', password[0]):
            raise ValidationError(
                _("Your password must start with capital char."),
            )

    def get_help_text(self):
        return _(
            "Your password must start with capital char."
        )


class PasswordRegexValidator:
    def validate(self, password, user=None):
        if not re.search(r'^[a-zA-Z0-9_]*$', password):
            raise ValidationError(
                _("Only digits and letters"),
            )
    def get_help_text(self):
        return _(
            "Only digits and letters"
        )


class ExcludeEmailValidator(validators.EmailValidator):
    domain_excludelist = []  # maybe it will be better to create model for this list
    exclude_message = 'This domain in exclude list'

    def __init__(self, message=None, code=None, allowlist=None, *, excludelist=None, whitelist=None):
        super().__init__(message, code, allowlist, whitelist=whitelist)
        if excludelist is not None:
            self.domain_excludelist = excludelist

    def __call__(self, value):
        if not value or '@' not in value:
            raise ValidationError(self.message, code=self.code, params={'value': value})

        user_part, domain_part = value.rsplit('@', 1)

        if not self.user_regex.match(user_part):
            raise ValidationError(self.message, code=self.code, params={'value': value})

        if domain_part in self.domain_excludelist:
            raise ValidationError(self.exclude_message, code=self.code, params={'value': value})

        if (domain_part not in self.domain_allowlist and
                not self.validate_domain_part(domain_part)):
            # Try for possible IDN domain-part
            try:
                domain_part = punycode(domain_part)
            except UnicodeError:
                pass
            else:
                if self.validate_domain_part(domain_part):
                    return
            raise ValidationError(self.message, code=self.code, params={'value': value})


last_name_validator = RegexValidator(r'^[A-Za-zА-Яа-я]*$')

first_name_validator = RegexValidator(r'^[A-Za-zА-Яа-я ]*$')

