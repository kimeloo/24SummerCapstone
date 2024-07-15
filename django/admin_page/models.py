from django.db import models

# Create your models here.
class UserAccount(models.Model):
    id = models.AutoField(primary_key=True) # 기본 키, 자동 생성되는 필드
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True, blank=True) # 고유함, NULL 허용, 빈 문자열 허용
    phone_num = models.CharField(max_length=15, unique=True, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True) # 자동으로 현재 시간 기록
    is_active = models.BooleanField(default=True)
    
    # login() 함수에서 사용자를 식별하는 데 사용할 필드를 정의
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['phone_num', 'email']
    is_anonymous = False
    is_authenticated = True
    class Meta:
        db_table = 'useraccount' # 실제 데이터베이스 테이블의 이름

    def __str__(self):
        return self.name


class Details(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE) # 해당 사용자 계정이 삭제될 경우 관련된 Details 데이터도 함께 삭제됨
    SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    sex = models.CharField(max_length=6, choices=SEX_CHOICES) # 필드에 사용할 수 있는 선택 옵션을 정의
    bmi = models.FloatField(null=True, blank=True) # 필드에 대해 NULL 값을 허용, 빈 값도 허용
    fat = models.FloatField(null=True, blank=True)
    age = models.FloatField(null=True, blank=True)
    fat_percentage = models.FloatField(null=True, blank=True)
    hr = models.FloatField(null=True, blank=True)
    waist = models.FloatField(null=True, blank=True)
    whr = models.FloatField(null=True, blank=True)
    muscle = models.FloatField(null=True, blank=True)
    sbp = models.FloatField(null=True, blank=True)
    dbp = models.FloatField(null=True, blank=True)
    hdl = models.FloatField(null=True, blank=True)
    ldl = models.FloatField(null=True, blank=True)
    tg = models.FloatField(null=True, blank=True)
    total_chol = models.FloatField(null=True, blank=True)
    fg = models.FloatField(null=True, blank=True)
    ppg = models.FloatField(null=True, blank=True)
    alt = models.FloatField(null=True, blank=True)
    hb = models.FloatField(null=True, blank=True)
    tsh = models.FloatField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'details'

    def __str__(self):
        return f"Details for {self.user.name}"


class Health(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE) 
    diabetes_status = models.FloatField(null=True, blank=True)
    dyslipidemia_status = models.FloatField(null=True, blank=True)
    fatty_liver_status = models.FloatField(null=True, blank=True)
    metabolic_syndrome = models.FloatField(null=True, blank=True)
    anemia_status = models.FloatField(null=True, blank=True)
    hypertension_status = models.FloatField(null=True, blank=True)
    obesity_status = models.FloatField(null=True, blank=True)
    hypothyroidism_status = models.FloatField(null=True, blank=True)
    hyperthyrodism_status = models.FloatField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'health'

    def __str__(self):
        return f"Health status for {self.user.name}"


class Sensors(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    rm01 = models.FloatField(null=True, blank=True)
    rm02 = models.FloatField(null=True, blank=True)
    rm03 = models.FloatField(null=True, blank=True)
    rm04 = models.FloatField(null=True, blank=True)
    rm05 = models.FloatField(null=True, blank=True)
    rm06 = models.FloatField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sensors'

    def __str__(self):
        return f"Sensors data for {self.user.name}"

class Recommend(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.IntegerField()
    recommendation = models.CharField(max_length=100)
    recommendation2 = models.CharField(max_length=100)
    recommendation3 = models.CharField(max_length=100)

    def __str__(self):
        return f"Recommendation {self.id}"