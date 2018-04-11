# -*- coding: utf-8 -*-

from django.http import HttpResponse
from TestModel.models import Test

def handledata(datas):
    s = ''
    for d in datas:
        s+=d.name + ' '
    return s

# operate db
def testdb(request):
    
    # test1 = Test(name='mousde', age = 23)
    # test1.save()

    response = ''
    response1 = ''

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    dlist = Test.objects.all()
        
    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id=1).update(name = 'dandywe')
    # response2.delete()
    # Test.objects.filter(id=1).delete();
    Test.objects.all().update(name = 'testdiango')
    # Test.objects.all().delete()
    # 获取单个对象
    response3 = Test.objects.get(id=1)

    response3.name= 'opperlu'
    response3.save()
    
    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    response =  Test.objects.order_by('name')[1:3]

    # return HttpResponse("<p>" + handledata(response) + "</p>")
    
    #数据排序
    Test.objects.order_by("id")
    
    # 上面的方法可以连锁使用
    Test.objects.filter(name="mousde").order_by("id")
    
    # 输出所有数据
    return HttpResponse("<p>" + handledata(dlist) + "</p>")