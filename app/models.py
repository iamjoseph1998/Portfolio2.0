from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, validate_email


phone_regex = RegexValidator(
    regex = r"^\d{10}", message="Phone number must be 10 digits only."
)


class Profile(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(validators=[validate_email])
    phone = models.CharField(max_length=10, validators=[phone_regex])
    address = models.TextField()
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.email

    def clean(self):
        super().clean()
        if not self.id and Profile.objects.exists():
            raise ValidationError('You can only add a single profile.')

    
    class Meta:
        verbose_name_plural = 'Profile'
