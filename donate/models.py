from django.db import models
import uuid
import datetime

# Create your models here.


class Streamer(models.Model):
    twitchId = models.CharField(max_length=30)
    opayId = models.CharField(null=True, max_length=50)
    ecpayId = models.CharField(null=True, max_length=50)
    deleteKey = models.UUIDField(default=uuid.uuid4())


class Opay(models.Model):
    streamer = models.ForeignKey("Streamer", on_delete=models.CASCADE)
    donateId = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    msg = models.TextField()
    dateTime = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        constraints = [models.UniqueConstraint(fields=["donateId","streamer"],name="simpleConstrain")]


class Ecpay(Opay):
    pass
