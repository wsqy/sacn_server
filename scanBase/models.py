from django.db import models
import django.utils.timezone as timezone
# Create your models here.

# 标签表：标签id,标签名,标签url
class CountryInfo(models.Model):
    country_cn = models.CharField(max_length=30, verbose_name="中文名")
    country_en = models.CharField(max_length=30, verbose_name="英文名")
    letter2 = models.CharField(max_length=2, verbose_name="二位英文代码")
    letter3 = models.CharField(max_length=3, verbose_name="三位英文代码")
    digital_code = models.CharField(max_length=5, verbose_name="数字代码")
    ISO_3166_2_code = models.CharField(max_length=30, verbose_name="ISO-3166-2标准代码")

    class Meta:
        verbose_name = "国家地区信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.country_cn
