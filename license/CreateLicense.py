# -*- coding: UTF-8 -*-
###################################
#TODO: 使用密钥将MAC加密
###################################
import os
import sys
import base64

from Crypto.Cipher import AES  
from binascii import b2a_hex, a2b_hex

seperateKey = "9wshy&#)800" # 随意输入一组字符串
aesKey = "8652mk57jd%142$#" # 加密与解密所使用的密钥，长度必须是16的倍数
aesIv = "abc6789defg^&*45" # initial Vector,长度要与aesKey一致
aesMode = AES.MODE_CBC  # 使用CBC模式

def encrypt(text):
    cryptor = AES.new(aesKey, aesMode, aesIv) #参考：https://www.cnblogs.com/loleina/p/8418108.html
    
    # padding
    add, length = 0, 16
    count = len(text)
    if count % length != 0:
        add = length - (count % length)
    text = text + ('0' * add) # '\0'*add 表示add个空格,即填充add个直至符合16的倍数

    ciphertext = cryptor.encrypt(text)
    #因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题  
    #所以这里统一把加密后的字符串转化为16进制字符串 ,当然也可以转换为base64加密的内容，可以使用b2a_base64(self.ciphertext)
    print(ciphertext)
    print('b2a_hex')
    print(b2a_hex(ciphertext))
    print('b2a_hex  end')
    # return base64.b64encode(b2a_hex(ciphertext)).decode().strip().upper()
    return  str(b2a_hex(ciphertext),'utf-8').upper()

if __name__ == "__main__":
    # argLen = len(sys.argv)
    # # 无参数输入则退出
    # if argLen != 2:
    #     print("usage: python {} hostInfo".format(sys.argv[0]))
    #     sys.exit(0)
    
    hostInfo = '005056c00008' # hostInfo是运行此脚本时传入的mac地址
    
    encryptText = encrypt(hostInfo) # 将mac地址第一次加密
    print(encryptText)
    encryptText = encryptText + seperateKey + "Valid"
    print(encryptText)
    encryptText =  encrypt(encryptText) # 将加密之后的密文再次加密
    print(encryptText)
    #str(b, encoding = "utf-8")
    with open("./license.lic", "w+") as licFile:
        licFile.write(encryptText)
        licFile.close()
    
    print("生成license成功!")
