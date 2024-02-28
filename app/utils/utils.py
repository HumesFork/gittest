import json
import requests
from response import MyResponse
import time
import oss2
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdksts.request.v20150401.AssumeRoleRequest import AssumeRoleRequest

appId="wx286987d21aeb176a"
appSecret="86fc04af11843f0248b43a5abb93b067"
access_token=""

class Utils:
    access_token=None
    expires=None
    # 阿里云配置
    AccessKeyID = 'LTAI5tQPNwbgaaDDsC89CYs5'
    AccessKeySecret='Pobds8bzE3nveyeGavEGXe0x8QQgN6'
    bucket=None


    @classmethod
    def getAccessToken(cls):
        #没过期就不调用
        if(cls.expires!=None and int(time.time())<cls.expires):
            return
        else:
            url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (
            appId, appSecret)
            res = requests.get(url).json()
            print(res)
            if ('access_token' in res):
                #秒级时间戳
               timestamp=int(time.time())
               cls.access_token=res['access_token']
               cls.expires=timestamp+res['expires_in']-60*5
               return cls.access_token
            else:
                return MyResponse.fail()

    @classmethod
        #oss域名初始化
    def getBucket(cls):
        # 阿里云账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM用户进行API访问或日常运维，请登录RAM控制台创建RAM用户。
        auth = oss2.Auth(cls.AccessKeyID, cls.AccessKeySecret)
        # yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
        endpoint = 'https://oss-cn-hangzhou.aliyuncs.com'
        # 填写Bucket名称。
        bucket = oss2.Bucket(auth, endpoint, 'jojotest')
        cls.bucket=bucket
        return cls.bucket

    @classmethod
        #获取文件签名用于访问
    def getSignedUrl(cls,name):
        if(cls.bucket==None):
            cls.getBucket()
        else:
            bucket=cls.bucket
            # 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。

            # 生成上传文件的签名URL，有效时间为1小时。
            # 生成签名URL时，OSS默认会对Object完整路径中的正斜线（/）进行转义，从而导致生成的签名URL无法直接使用。
            # 设置slash_safe为True，OSS不会对Object完整路径中的正斜线（/）进行转义，此时生成的签名URL可以直接使用。
            url = bucket.sign_url('PUT', name, 60*60, slash_safe=True)
            print('签名URL的地址为：', url)

    @classmethod
    #临时授权STS,该ram用户拥有管理oss权限,当前过期时间设置为1小时
    def getSts(cls):
        # 构建一个阿里云客户端，用于发起请求。
        # 设置调用者（RAM用户或RAM角色）的AccessKey ID和AccessKey Secret。
        client = AcsClient('LTAI5tQDxBphcGUG6vwfMfBs', 'XZufUNcyJSDGGiUYXRQRobB4OaRGaP', 'cn-hangzhou')
        # 构建请求。
        request = AssumeRoleRequest()
        request.set_accept_format('json')

        # 设置参数。
        request.set_RoleArn("acs:ram::1745005142459771:role/ramosstest")
        request.set_RoleSessionName("test")

        # 发起请求，并得到响应。
        response = client.do_action_with_exception(request)
        response=json.loads(str(response,'utf-8'))
        return MyResponse.success(response['Credentials'])
