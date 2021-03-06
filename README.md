# 通讯录管理系统

## 一、系统需求

通讯录是一个可以记录亲人、好友信息的工具。

本教程主要利用C++来实现一个通讯录管理系统

系统中需要实现的功能如下：

- 添加联系人：向通讯录中添加新人，信息包括（姓名、性别、年龄、联系电话、家庭住址）最多记录1000人
- 显示联系人：显示通讯录中所有联系人信息
- 删除联系人：按照姓名进行删除指定联系人
- 查找联系人：按照姓名查看指定联系人信息
- 修改联系人：按照姓名重新修改指定联系人
- 清空联系人：清空通讯录中所有信息
- 退出通讯录：退出当前使用的通讯录

## 二、版本

#### 01.C++版本

``` c++
// 主文件：./code/utils.cpp
/* 
  ps:作者刚学C/C++，而数据可持久化为涉及,所以此项目不包含。
     学习对象 - B站视频：BV1et411b73Z，此项目来自此视频。
     因作者之前已经学过Python，所以作者是根据自己理解进行编写，内容可能有
     些出入，但逻辑思路不变。
*/
```

#### 02.Python版本

``` python
# 主文件: ./PythonVersion/__main__.py
# 环境：Python3.8+、MySQL5.5+
# 内置库：`os`、`sys`
# 第三方库：`pymysql`
'''
说明：
	（1）请在运行系统之前先保证`环境`和`第三方库`配置好；
	（2）请先在运行脚本前先通过dos界面进入MySQL中创建对表，代码如下: `address_book.sql`；
	（3）请先修改配置文件`./PythonVersion/config/ettings.py`中数据库相关配置参数。
	完成以上2个步骤再运行主文件。
'''
```

```mysql
# DOS中SQL语句
mysql -h Host -P Port -uUsername -pPassword; # 
use `databaseName`;
scorce "./PythonVersion/db/address_book.sql"
```



