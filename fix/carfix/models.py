from django.db import models

class User(models.Model):
    #用户id
    #user_id = models.AutoField(primary_key = True)
    #用户姓名
    user_name = models.CharField(max_length = 32,verbose_name = "用户姓名")
    #用户电话
    user_tel = models.CharField(max_length = 32,verbose_name = "用户联系方式")
    #用户地址
    user_addr = models.CharField(max_length=32,verbose_name="地址")
    #用户拥有车辆 外键
    user_car = models.ForeignKey('Car',on_delete=models.CASCADE,verbose_name="车辆")

    is_made_order = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = '用户管理'
    
    def __str__(self):
        return self.user_name


class Car(models.Model):
    #编号
    #car_id  = models.AutoField(primary_key = True,verbose_name = "车辆编号")
    #品牌
    car_brand = models.CharField(max_length = 32,verbose_name = "品牌")
    #损坏部位
    car_broken_part = models.CharField(max_length = 32,verbose_name = "损坏部位")
    #拥有车辆
    #use_goods = models.ForeignKey('Goods',on_delete = models.CASCADE,verbose_name = "使用配件")
    #设置admin中显示的管理的内容
    class Meta:
        verbose_name_plural = '车辆管理'
    #字符串表示
    def __str__(self):
        return self.car_brand

        
class Goods(models.Model):
    #配件(配件编号，配件名称,配件价格，配件描述，配件个数) 主键 ：配件编号
    #goods_id  = models.AutoField(primary_key = True,verbose_name = "配件编号")
    #配件名称字段
    goods_name = models.CharField(max_length = 32,verbose_name = "配件名称")
    #配件价格字段
    goods_price = models.IntegerField(verbose_name = "配件价格")
    #配件描述字段
    goods_desciption = models.CharField(max_length = 32,verbose_name = "配件描述")
    #配件数量字段
    goods_count = models.IntegerField(verbose_name="配件数量")
    class Meta:
        verbose_name_plural = '配件管理'
    def __str__(self):
        return self.goods_name



class Worker(models.Model):
    #人员工号，姓名，联系方式，出生地，职位，薪资
    choice = (
        (1,"高级员工"),
        (2,"中级员工"),
        (3,"初级员工"),
    )
    #员工工号
    # worker_id = models.IntegerField(primary_key = True,verbose_name = "工号")
    #员工姓名
    worker_name = models.CharField(max_length = 32,verbose_name = "姓名")
    #员工电话
    worker_tel = models.CharField(max_length = 32,verbose_name = "联系方式")
    #员工住址
    worker_addr =  models.CharField(max_length = 32,verbose_name = "地址")
    #员工职位字段
    worker_positon = models.CharField(max_length = 32,verbose_name = "职务")
    #员工类型字段：
    worker_type = models.IntegerField(choices=choice,verbose_name = "员工类型",default=1) #枚举类型
    
    class Meta:
        verbose_name_plural = '员工管理'
    
    def __str__(self):
        return self.worker_name


# 车辆(车辆编号，车辆车牌，损坏部位,使用配件) 主键：编号


class FixList(models.Model):
    
    #用户 外键
    user = models.ForeignKey('User',models.CASCADE,verbose_name="用户")
    #车辆 外键 
    price = models.IntegerField(default=0,verbose_name = "交易价格")
    #维修人员 外键
    worker = models.ForeignKey('Worker',models.CASCADE,verbose_name="主要负责人")
    #提交时间
    begin_fix_time = models.DateTimeField(auto_now = True,verbose_name="提交订单时间")

    #主要使用的配件
    main_goods = models.CharField(max_length=100,verbose_name="主要使用配件",default="1")
    
    #admin中显示的管理内容
    class Meta:
        verbose_name_plural = '维修列表'
    def __str__(self):
        return str(self.begin_fix_time)

class Power(models.Model):
    user_name = models.CharField(max_length=20,verbose_name="用户名")
    password = models.CharField(max_length=20,verbose_name="密码",default="12345678")
    user_real_name = models.CharField(max_length=30,verbose_name="真实姓名",default="zz")
    boss = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = '人员权限记录'


