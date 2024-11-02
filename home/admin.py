from django.contrib import admin
from .models import Vote, VoteItem, VoteRecord

class VoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class VoteItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'vote_name', 'count', 'display_percent')  # 使用 display_percent 方法

    def display_percent(self, obj):
        return f"{obj.percent():.2f}%"  # 确保调用 percent 方法并格式化返回值
    display_percent.short_description = '百分比'  # 设置列标题

admin.site.register(Vote)
admin.site.register(VoteItem, VoteItemAdmin)  # 注册 VoteItem 时使用自定义管理类
admin.site.register(VoteRecord)