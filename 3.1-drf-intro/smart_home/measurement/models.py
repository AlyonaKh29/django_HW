from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.name, self.description


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='measurement/picture/', default=None, blank=True, null=True)

