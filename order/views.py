from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from apartment.models import Apartment
from order.models import Order, Star
import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@login_required
def order(request):
    # 查询用户对象
    user = request.user
    # 根据提交查询购物车信息
    # 构造传递到模板中的数据
    context = {'title': '提交订单',
               'page_name': 1,
               'user': user,
               }
    return render(request, 'df_order/order.html', context)


'''
事务：一旦操作失败则全部回退
1、创建订单对象
2、判断商品的库存
3、创建详单对象
4、修改商品库存
5、删除购物车
'''


@transaction.atomic
@login_required
def order_handle(request):
    tran_id = transaction.savepoint()
    apartment_id = request.POST('apartment_id')
    try:
        apartment = Apartment.objects.filter(id=apartment_id).first()
        if apartment.is_rent is False:
            order = Order()
            user = request.user
            now = datetime.now()
            order.id = '%s%d' % (now.strftime('%Y%m%d%H%M%S'), user.id)
            order.consumer = user
            # print order.oid
            order.created_date = now
            order.apartment = apartment
            order.save()

        else:
            transaction.savepoint_rollback(tran_id)
            return redirect('/apartment/' + str(apartment_id))
            # return HttpResponse('no')
        # 保存总价
        order.save()
        transaction.savepoint_commit(tran_id)
    except Exception as e:
        print('================%s' % e)
        transaction.savepoint_rollback(tran_id)

    # return HttpResponse('ok')
    return redirect('/order/')


@login_required
def check_order(request, order_id):
    order = Order.objects.filter(id=order_id).first()
    if order.is_check is False:
        tran_id = transaction.savepoint()
        order.is_check = True
        order.save()
        transaction.savepoint_commit(tran_id)
    else:
        return redirect('')

@csrf_exempt
@login_required
def star(request,apartment_id):
    user = request.user
    apartment = Apartment.objects.filter(id=apartment_id).first()


    var = Star.objects.filter(user=user).filter(apartment=apartment)

    if len(var) ==0:
        star = Star()
        star.apartment = apartment
        star.user = user
        star.save()
    else:
        star = var.first()
        star.delete()

    return JsonResponse({
        'status':'success'
    })
