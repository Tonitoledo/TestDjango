from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import EmailValidator
from django.utils import timezone

class User(AbstractUser):
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)

    email = models.EmailField(
        _('email address'), 
        unique=True,
        blank=False,
        validators=[EmailValidator()],
        error_messages={
            'unique': _("A user with that email already exists."),
        }
    )
    
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    date_joined = models.DateTimeField(_('date joined'),  default=timezone.now)
    last_updated = models.DateTimeField(_('last updated'), auto_now=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['-date_joined']
    
    def __str__(self):
        return self.get_full_name() or self.email

