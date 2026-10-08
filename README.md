# Python 学习记录

> 每天至少 1 个 commit，不断更。

## 目录约定

| 内容 | 说明 |
| --- | --- |
| `#案例
base = 20.7 #基础播放量
increase = 50 #新增加播放量
print("未来一个月播放量:",base + increase)
print("未来两个月播放量:",base + increase + increase)


#升级：一次性可以定义多个变量
base,increase = 20.7,50
print("未来一个月播放量:",base + increase)
print("未来两个月播放量:",base + increase + increase)` | 一天一个文件，比如 `day01_guess_number.py` |
| `notes/` | 学习笔记、踩坑记录 |

## 每天怎么提交

三条命令（必须记住）：

```bash
git add .
git commit -m "今天写了什么"
git push
```

或者用一键脚本，只敲一条：

```bash
./push.sh "今天写了通讯录的增删改查"
```
