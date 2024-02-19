# qrcode_send_file

A sender generates a QR code and the receiver uploads a video to parse the QR code for wireless file transfer.

这是一个使用二维码无线传输文件的项目。

## Usage

1, configuration environment
2, come up with a device that can record video ready to record your screen
3, in the device can not be connected to the Internet to run python sender.py -f your_file_path
4, record the screen appeared on the QR code
5, upload the video to the target computer you want to copy
6, run python receiver.py -f your_audio_file_path

## 使用方法

1、配置环境
2、拿出一个一个可以录像的设备准备录制你的屏幕
3、在不能联网的设备上运行python sender.py -f your_file_path
4、录制屏幕上出现的二维码
5、上传视频到你想要拷贝的目标电脑
6、运行python receiver.py -f your_audio_file_path

## TODO

1、可以考虑加个顺序校验
2、优化生成的文件名
