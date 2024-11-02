from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import VoteItem, VoteRecord, Vote
from django.utils import timezone
import logging

# 设置日志记录
logger = logging.getLogger(__name__)

def index(request):
    # 获取投票1
    votes = Vote.objects.all()
    return render(request, "home/index.html", {"votes": votes})

def vote(request, item_id):
       if request.method == 'POST':
           vote_item = get_object_or_404(VoteItem, id=item_id)
           ip_address = request.META.get('REMOTE_ADDR')  # 获取用户的 IP 地址

           print("User IP Address:", ip_address)

           # 检查用户今天是否已经投过票
           today = timezone.now().date()
           if VoteRecord.objects.filter(vote_item=vote_item, ip_address=ip_address, created_at__date=today).exists():
               return JsonResponse({'status': 'error', 'message': 'You have already voted today.'})

           # 记录投票
           vote_item.count += 1
           vote_item.save()

           # 创建新的投票记录
           VoteRecord.objects.create(vote_item=vote_item, ip_address=ip_address)

           # 计算总票数和百分比
           total_votes = sum(item.count for item in VoteItem.objects.filter(vote=vote_item.vote))
           current_percent = (vote_item.count / total_votes) * 100 if total_votes > 0 else 0

           return JsonResponse({
               'status': 'success',
               'message': 'Vote successful!',
               'vote_item_id': vote_item.id,
               'count': vote_item.count,
               'percent': current_percent
           })

       return JsonResponse({'status': 'error', 'message': 'Invalid request'})