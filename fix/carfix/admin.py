from django.contrib import admin
from .models import User,Worker,Goods,Car,FixList,Power



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    #展示字段
    list_display = ( "id",'user_name','user_tel','user_addr','user_car','is_made_order')
    #可修改字段
    fields = ('user_name','user_tel','user_addr','user_car','is_made_order')



@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    #显示字段
    list_display = ( 'id','worker_name','worker_tel','worker_addr','worker_positon','worker_type')
    #可修改域
    fields = ('worker_name','worker_tel','worker_addr','worker_positon','worker_type')




@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    # 需要展示的字段
    list_display = (  "id",'goods_name', 'goods_price','goods_count','goods_desciption')
    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    list_display_links = ( 'goods_name', 'goods_price','goods_desciption','goods_count')
    # list_per_page = 50 #每页显示的最大记录数
    # ordering = ('stu_id',)#排序规则，倒叙添- 例如 '-stu_id'
    list_filter =('goods_name',) #过滤器
    #可以用来搜索的字段，自由定制
    search_fields =( 'goods_name','goods_price','goods_count') #搜索字段
    #可修改字段
    fields = ('goods_name', 'goods_price','goods_desciption','goods_count')#显示可以修改的字段
    #date_hierarchy = 'go_time'    # 详细时间分层筛选



@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # 需要展示的字段
    list_display = ( "id",'car_brand', 'car_broken_part',)
    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    list_display_links = ('car_brand', 'car_broken_part',)
    # list_per_page = 50 #每页显示的最大记录数
    # ordering = ('stu_id',)#排序规则，倒叙添- 例如 '-stu_id'
    list_filter =( 'car_brand', 'car_broken_part',)
    search_fields =('car_brand', 'car_broken_part',) #搜索字段
    fields = ( 'car_brand', 'car_broken_part',)#显示可以修改的字段
    #date_hierarchy = 'go_time'    # 详细时间分层筛选　　



@admin.register(FixList)
class FixListAdmin(admin.ModelAdmin):

    # 需要展示的字段
    list_display = ('id','user', 'worker','price','begin_fix_time','main_goods')
    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    list_display_links = ('user',  'worker','price','begin_fix_time',)
    # list_per_page = 50 #每页显示的最大记录数
    # ordering = ('stu_id',)#排序规则，倒叙添- 例如 '-stu_id'
    #list_filter =( 'car_brand', 'car_broken_part','use_goods',)
    #search_fields =('user', 'car', 'worker','begin_fix_time',) #搜索字段
    fields = ('user', 'worker','price','main_goods')#显示可以修改的字段
    #date_hierarchy = 'go_time'    # 详细时间分层筛选　　


@admin.register(Power)
class PowerAdmin(admin.ModelAdmin):

    # 需要展示的字段
    list_display = ('id','user_name', 'boss','user_real_name')
    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    list_display_links = ('user_name', 'boss','user_real_name')
    # list_per_page = 50 #每页显示的最大记录数
    # ordering = ('stu_id',)#排序规则，倒叙添- 例如 '-stu_id'
    #list_filter =( 'car_brand', 'car_broken_part','use_goods',)
    #search_fields =('user', 'car', 'worker','begin_fix_time',) #搜索字段
    #fields = ('user', 'car', 'worker','begin_fix_time',)#显示可以修改的字段
    #date_hierarchy = 'go_time'    # 详细时间分层筛选　　


admin.site.site_header = "汽车修户后台" 
admin.site.site_title = "汽车维修系统"
