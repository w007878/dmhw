# coding: utf-8
from Crypto.Cipher import AES
import base64
import requests
import sys

headers = {
    'Cookie': 'appver=1.5.0.75771;',
    'Referer': 'http://music.163.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

# first_param = "{rid:\"\", offset:\"0\", total:\"true\", limit:\"20\", csrf_token:\"\"}"
first_param = "{\"ids\":\"[%d]\",\"br\":128000,\"csrf_token\":\"\"}"
second_param = "010001"
third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
forth_param = "0CoJUm6Qyw8W8jud"


def get_params():
    iv = "0102030405060708"
    first_key = forth_param
    second_key = 16 * 'F'
    h_encText = AES_encrypt(first_param, first_key, iv)
    h_encText = AES_encrypt(h_encText, second_key, iv)
    return h_encText


def get_encSecKey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey


def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    if isinstance(text, str):
        text = text + pad * chr(pad)
    else:
        text = text.decode('utf-8') + pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text)
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text


def get_json(url, params, encSecKey):
    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    response = requests.post(url, headers=headers, data=data).json()
    return response['data']


id_list = open("song_id_list", "r").read().split()
print(id_list)

for music_id in id_list:
    # music_id = input('请输入歌曲ID：')
    first_param = "{\"ids\":\"[%d]\",\"br\":128000,\"csrf_token\":\"\"}" % int(music_id)
    url = 'https://music.163.com/weapi/song/enhance/player/url?csrf_token='
    params = get_params()
    encSecKey = get_encSecKey()
    """
    rsp:{
        'data': [{
            'gain': 2.3073,
            'type': 'mp3',
            'url': 'http://m10.music.126.net/20180111133509/24c79548414f7aa7407985818cb16a39/ymusic/333c/66b1/e5ec/
                72aeb13aca24c989295e58e8384e3f97.mp3',
            'md5': '72aeb13aca24c989295e58e8384e3f97',
            'flag': 0, 'code': 200, 'payed': 0, 'id': 151619, 'expi': 1200, 'size': 3868307,
            'uf': None, 'br': 128000, 'fee': 0, 'canExtend': False}], 'code': 200}
    """
    rsp = get_json(url, params, encSecKey)
    music_url = rsp[0].get('url')
    if music_url:
        music = requests.get(music_url)
        name = sys.path[0] + "/music/%s.mp3" % rsp[0]['id']
        with open(name, "wb") as code:
            code.write(music.content)