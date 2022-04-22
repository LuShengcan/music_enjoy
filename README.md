# music_enjoy（0.0.10）

## 项目介绍


## 正在开发的功能

### 音视频合成
### 酷我、酷狗下载

## 目前支持功能
### 哔哩哔哩弹幕网视频与音频的下载

## 使用方法

### 包安装
```shell
pip install music_enjoy
```



### 使用实例

```python
import music_enjoy as me

url = 'https://www.bilibili.com/video/BV1aP4y177x2/?spm_id_from=autoNext' # 你的视频网址
dest = './1.m4a' 			# 资源存放位置，可以是绝对路径或相对路径
audio_or_video = 'audio' 	# 要下载音频还是视频（目前不支持同时下载，可分开下载后合成）

me.bilibili(url=url, dest=dest, audio_or_video=audio_or_video)
```

