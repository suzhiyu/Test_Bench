import rsa
import base64


class Crypto:
    def __init__(self):
        pass

    def savekey(self):
        '''
        新建公钥和私钥并保存到本地
        :return:
        '''
        pubkey, privkey = rsa.newkeys(1024)
        pub = pubkey.save_pkcs1()  # 以pem格式保存pubkey
        pri = privkey.save_pkcs1()  # 以pem格式保存privkey
        with open('./keys/pubkey.pem', 'w+') as f:
            f.write(pub.decode('utf8'))
        with open('./keys/privkey.pem', 'w+') as f:
            f.write(pri.decode('utf8'))

    def encrypto(self, msg):
        '''
        用公钥加密msg
        :return:
        '''
        with open('./keys/pubkey.pem', 'r') as f:
            p = f.read()
        pubkey = rsa.PublicKey.load_pkcs1(p.encode('utf8'))  # pem格式加载公钥,返回pkcs
        crypto = rsa.encrypt(msg.encode('utf8'), pub_key=pubkey)  # 使用PKCS加密给定的消息,返回类型bytes
        # 对于保存，网络传输，打印不乱码，需要通base64编码进行转换；
        # base64编解码能把一些无法直接用文件本信息编码的二进制数据，转换成常规的二进制数据。
        crypto_msg = base64.encodebytes(crypto).decode('utf8')  # 加密后的文本信息msg
        print(crypto_msg)
        # 保存加密后的信息到本地
        with open('./keys/msg.txt', 'w+') as f:
            f.write(crypto_msg)
        return crypto_msg

    def decrypto(self, crypto_msg=None):
        '''
        私钥解密msg文件
        :return:
        '''
        # 读取本地私钥
        with open('./keys/pubkey.pem', 'r') as f:
            p = f.read()
        privkey = rsa.PrivateKey.load_pkcs1(p.encode('utf8'))  # pem格式加载私钥

        # 读取加密文件
        with open('./keys/msg.txt', 'r') as f:
            crypto_msg = f.read()

        # base64解码
        crypto_msg = base64.decodebytes(crypto_msg.encode('utf8'))


        decrypto_msg = rsa.decrypt(crypto_msg, privkey)  # 私钥解密
        decrypto_msg = decrypto_msg.decode('utf8')  # utf8解码
        print(decrypto_msg)
        return decrypto_msg


crypto = Crypto()
crypto.savekey()  # 保存公钥私钥
# crypto.encrypto('你好')  # 使用公钥加密信息
crypto.decrypto()  # 使用私钥解密信息
