from django.db import models
from django.utils import timezone

# 投票标题
class Vote(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="upload/vote/", null=True, blank=True) #可以为空
    # 返回标题
    def __str__(self):
        return self.title
    # 设置数据库表名
    class Meta:
        db_table = "vote"
        verbose_name = "投票主题"
        verbose_name_plural = "投票主题"

class VoteItem(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    vote_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="upload/vote/", null=True, blank=True) #可以为空
    count = models.IntegerField(default=0)

    # 百分比
    def percent(self):
        total_count = sum(item.count for item in VoteItem.objects.filter(vote=self.vote))  # 计算与当前 Vote 相关的所有 VoteItem 的总 count
        if total_count > 0:  # 避免除以零
            return (self.count / total_count) * 100  # 计算百分比
        return 0.0  # 如果总投票数为零，返回 0.0
    #返回投票名称
    def __str__(self):
        return self.vote_name
    #设置表名
    class Meta:
        db_table = "vote_item"
        verbose_name = "投票名称"
        verbose_name_plural = "投票列表"

class VoteRecord(models.Model):
    vote_item = models.ForeignKey(VoteItem, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(default='0.0.0.0')  # 设置默认值

    class Meta:
        unique_together = ('vote_item', 'ip_address', 'created_at')  # 确保每个投票项和 IP 每天唯一
        db_table = "vote_record"
        verbose_name = "投票记录"
        verbose_name_plural = "投票记录"
