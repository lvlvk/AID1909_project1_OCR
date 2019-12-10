 ## README

目录&文件

1. docs：资料、文档等
2. libs：需要导入的包
3. log：项目修改记录
4. project：代码相关文件、目录
   1. config：配置文件
   2. view：图形界面
   3. faceid：人脸识别
   4. ocr：车牌识别
   5. server：服务端
   6. database：数据库

客户端与服务端的TCP协议

+ 格式：`请求类型+空格+值` 多个值之间用空格连接
  + "请求类型\t值1\t值2..."

+ 客户端的请求类型：
  + 测试：TEST
  + 人脸识别：FACE
  + 车牌识别：OCR
  + 注销：EXIT
+ 服务端的相应：
  + 测试：OK
  + 人脸识别：
  + 车牌识别：
  + 注销：FINISH