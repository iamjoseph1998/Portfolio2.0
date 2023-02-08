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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    def clean(self):
        super().clean()
        if not self.id and Profile.objects.exists():
            profile = Profile.objects.all().first()
            raise ValidationError(f'You can only add a single profile. Please edit {profile.first_name} {profile.last_name}\'s profile.')

    
    class Meta:
        verbose_name_plural = 'Profile'


class Education(models.Model):
    degree = models.CharField(max_length=200)
    school = models.CharField('School or University', max_length=200)
    is_pursuing = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField(help_text='Do not add end date if currently pursuing, please tick below pursing')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.degree
    
    def clean(self):
        super().clean()
        if Education.objects.filter(is_pursuing=True).first():
            profile = Education.objects.filter(is_pursuing=True).first()
            raise ValidationError(f'You are currently pursuing {profile.degree}. Cannot pursue two degree\'s at a time.')
    

    class Meta:
        verbose_name_plural = 'Education'
