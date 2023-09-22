from django.db import models

class Locality(models.Model):
    VIZAG = 'VZ'
    CHENNAI = 'CI'
    VIJAYAWADA = 'VW'
    NELLORE = 'NE'
    SRICITY = 'SC'
    LOCALITY_CHOICES = [
        (VIZAG, 'VIZAG'),
        (CHENNAI, 'CHENNAI'),
        (VIJAYAWADA, 'VIJAYAWADA'),
        (NELLORE, 'NELLORE'),
        (SRICITY, 'SRICITY'),
    ]
    schools_choices = [
        (VIZAG, (
        ('SCHOOL1', 'SC1'),
        ('SCHOOL2', 'SC2'),
        ('SCHOOL3', 'SC3'),
        ('SCHOOL4', 'SC4'),
        ('SCHOOL5', 'SC5'),
        ('SCHOOL6', 'SC6')
        )
     ),
    (CHENNAI, (
        ('SCHOOL1', 'SC1'),
        ('SCHOOL2', 'SC2'),
        ('SCHOOL3', 'SC3'),
        ('SCHOOL4', 'SC4'),
        ('SCHOOL5', 'SC5'),
    )
     ),
    (VIJAYAWADA, (
        ('SCHOOL1', 'SC1'),
        ('SCHOOL2', 'SC2'),
        ('SCHOOL3', 'SC3'),
        ('SCHOOL4', 'SC4'),
        ('SCHOOL5', 'SC5'),
    )
     ),
     (NELLORE, (
        ('SCHOOL1', 'SC1'),
        ('SCHOOL2', 'SC2'),
        ('SCHOOL3', 'SC3'),
        ('SCHOOL4', 'SC4'),
        ('SCHOOL5', 'SC5'),
    )
     ),
     (SRICITY, (
        ('SCHOOL1', 'SC1'),
        ('SCHOOL2', 'SC2'),
        ('SCHOOL3', 'SC3'),
        ('SCHOOL4', 'SC4'),
        ('SCHOOL5', 'SC5'),
    )
     )

    ] 
    Locality = models.CharField(
        max_length=20,
        choices=LOCALITY_CHOICES,
        default=VIZAG,
    ) 


    schoolname = models.CharField(choices=schools_choices, max_length=200,verbose_name='schoolname')  
    

    
class Person(models.Model):
    ACADEMICS = 'AC'
    SPORTS = 'SP'
    PENALTY = 'PL'
    FEE_CHOICES = [
        (ACADEMICS, 'ACADEMICS'),
        (SPORTS, 'SPORTS'),
        (PENALTY, 'PENALTY'),
        
    ]
    fee_type = models.CharField(
        max_length=20,
        choices=FEE_CHOICES,
        default=ACADEMICS,) 
    amount = models.CharField(max_length=6)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    youremail = models.EmailField(max_length=45)
    phonenumber = models.CharField(max_length=30)
    classandsection = models.CharField(max_length=30)
    guardian_name = models.CharField(max_length=30,null=True)
    Locality=models.ForeignKey(Locality,on_delete=models.CASCADE,null=True)

    
    