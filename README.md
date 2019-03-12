# NiceBlog
一个基于Flask的开发的个人博客，用于学习，参考了《Flask Web开发：基于Python的Web应用开发实战》

主要功能如下：

**1、** 对于**普通用户**，主要有如下功能：
* 注册、登录、重置密码（邮箱验证）
* 文章列表、详情
* 评论
* 喜欢

**2、** 对于**管理员**，除了有普通用户的功能，主要有如下功能：
* 写文章（Markdown编辑）
* 用户权限管理（管理喜欢、评论的权限）
* 评论管理（删除、屏蔽）

**3、** 为移动端提供相关api接口

## env 

   python 环境： python3.7.1

**1、** 运行
```
pip install -r requirements.txt
env.bat
python manage.py runserver

```
