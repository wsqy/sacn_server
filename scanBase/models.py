from django.db import models
import django.utils.timezone as timezone
# Create your models here.

# 标签表：标签id,标签名,标签url
class CountryInfo(models.Model):
    country_cn = models.CharField(max_length=30, verbose_name="中文名")
    country_en = models.CharField(max_length=30, verbose_name="英文名")
    letter2 = models.CharField(max_length=2, verbose_name="二位英文代码")
    letter3 = models.CharField(max_length=3, verbose_name="三位英文代码", unique=True, blank=True, null=True)
    digital_code = models.CharField(max_length=5, verbose_name="数字代码")
    ISO_3166_2_code = models.CharField(max_length=30, verbose_name="ISO-3166-2标准代码", unique=True, blank=True, null=True)

    class Meta:
        verbose_name = "国家地区信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.country_cn


class IPSection(models.Model):
    country = models.ForeignKey(CountryInfo, verbose_name="所属国家")
    ip_section = models.CharField(max_length=30, verbose_name="ip段", unique=True, blank=True, null=True)
    network = models.GenericIPAddressField(verbose_name="网关地址", blank=True, null=True)
    netmask = models.GenericIPAddressField(verbose_name="广播地址", blank=True, null=True)
    total = models.IntegerField(verbose_name="总量", blank=True, null=True)
    deal_time = models.DateTimeField(verbose_name="处理时间", blank=True, null=True)

    class Meta:
        verbose_name = "ip段信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip_section


class IPInfo(models.Model):
    country = models.ForeignKey(CountryInfo, verbose_name="所属国家")
    iP_section = models.ForeignKey(IPSection, verbose_name="所属ip段")
    ip = models.GenericIPAddressField(verbose_name="ip", blank=True, null=True)
    deal_time = models.DateTimeField(verbose_name="扫描时间", blank=True, null=True)

    class Meta:
        verbose_name = "ip信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip
