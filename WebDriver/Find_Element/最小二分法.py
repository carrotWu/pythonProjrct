#coding=utf-8
'''
1.A  2.C
3.自动化测试使用场景
  产品变更少，项目开发周期长，测试用例执行频繁，手工无法胜任。
  比如说：接口测试，回归测试，性能测试，单元测试，协议测试等。
4.==与equals的区别
 ①==用于基本类型的比较，比较的是数值本身是否相等
 ②==用于引用类型的比较，则比较的是对象在内存中存放的地址
 ③equals只能用于对象的比较，比较的是对象本身内容是否一样。
5.在前端SpringMVC框架中加入拦截器(Interceptor)来对不同用户的
 请求做出不同的响应。。。。。。。
'''
#6.二分法算法
def search(arr,val):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)/2
        if arr[mid]==val:
            return mid
        elif arr[mid]>val:
            high=mid-1
        else:
            low=mid+1
    return #val不存在，返回None
