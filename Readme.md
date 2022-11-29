# Donate通知

```mermaid
graph LR;
1(Ecpay)
2(Opay)
django(django)
ap(ap-scheduler)
1---|requests|ap
2---|requests|ap
ap-->django
django-->|boto3|AWS_SQS
AWS_SQS-->b(bot)-->|websockets|twitch_irc
```
* Database
![](https://i.imgur.com/P92PMcd.png)


> Readme Will be sync with hackmd