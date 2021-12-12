# mrvl(支持windows+linux的多币机器人,交易所目前只支持币安)  本策略不提供永久白嫖

## 非开源，慎用! 建议使用一定要加群，机器人收集到错误会在群里提醒(打开https://small.yjyzj.cn:8443/ 可以扫码加开发者微信)

此机器人我从2021-08-20左右开始调试，初始资金是100U，到2021-09-26(币安今天27只能看前一天26的整天收益)为止，总收益103.89971234U。

config.py的symbols_conf配置，币对的后一个值为每个币下单的量，如果完全按照我的量来跑，至少200U资金，并不要动手加仓，只要不是币跌去3分之2就不会爆仓。

可以修改为每个币最低下单量，资金为100U就可以跑，如果资金不够，建议少跑几个币。

## 启动说明
启动运行的有两种，为启动部分币(Run.py,Main.py和Start.py)和Runner.py为启动全部币(默认也是启动部分,要启动全部币config.json里的select_all_symbols参数值要为true).

## 配置说明(一定要细看)
must_edit_config.json这个文件必须要填。

config.json里的@select_symbols_2，@select_symbols_1，@select_symbols_3，这为三个列表，对应不同的三个启动脚本。
symbol_metas.json里的trading_size为下单数量，win_arg为追踪止盈触发参数，add_arg为下跌补仓参数，当在开仓状态下止盈后价格下跌，下跌到最近一次持仓价*该参数时又开仓。
loss_arg是止损参数,trace_win为追踪止盈对比值。


## 收益图

![](https://github.com/mn3711698/mrvl/blob/main/win1.png)

![](https://github.com/mn3711698/mrvl/blob/main/win2.png)

![](https://github.com/mn3711698/mrvl/blob/main/win3.png)

# 使用授权说明(2021-11-25，每个币安密钥都可以无偿体验，如果无法使用请加我微信)

所有新使用者都可以白嫖7天(1倍)。过后不付费将无法使用。

授权将按不同等级进行不同收费。为保证机器人效果除最低级外，其他级别都会限制授权人数，达到了将暂停该级别的授权。


双向持仓:每1倍默认下单量30元/月，最高可以开10倍。

现货：每1倍默认下单量50元/月，最高可以开10倍(下单量为5u)。(可能会有两种不同的策略，一种是跟合约一样的，一种是抄底。抄底的开单量少。)

除1倍外，每个倍数最多50个授权，第51个将无法使用授权只能使用1倍授权。

授权价格后续不再更改

无限制倍数授权:合约8888元/永久，现货与合约同价,无法共用。预计20个授权(此授权考虑内部开放更多的代码，甚至开源，机器人定制共享化)

授权说明：
    
    1、一个币安帐户同一唯一标识，多个api无法共用授权，需要一个api密钥开一个授权且无法同时授权同一倍数，要求不同授权倍数。
    2、会出于保证无限制版本用户的收益，在某个时间不再进行其他授权,已购授权能正常使用完结，后续无法续费。
    
    @flamhaze5946帮助改进代码送一个无限制授权
    

## 本项目只是提供代码，不对使用者因使用本代码实际产生的盈亏负责。不要跟我说开源，我从来就没有想过要开源，只是开放使用。

## 可以自行设置计算止盈的配置参数及修改止损配置

# 注意(白嫖更要注意安全，因为核心代码没有开源，大家慎用)

## API的权限只需要有交易权限就够了，不要开提币权限,还要限制ip！

## API的权限只需要有交易权限就够了，不要开提币权限,还要限制ip！

## API的权限只需要有交易权限就够了，不要开提币权限,还要限制ip！

# 需要准备云主机，windows支持64位的python,3.8或3.7,linux系统支持python3.6

# 需要网络可以访问币安交易所，否则机器人无法使用

# 关于服务器说明

各位购买vps云服务器，建议买日本的，币安的服务器是日本的。如果买美国的服务器，是便宜，但网络问题会导致持仓价会比日本的高。

## windows使用说明(路径写死了)
如果会git就用git下载代码，不会就全按说明进行。

安装步骤请参考: mrvl在windows系统安装部署说明.doc文件

相关持仓及订单信息请看币安的网页或者APP对应的交易对下的数据。

如果后续有更新代码，可以直接git下载就好了。下载好后，关掉cdm窗口，重新打开窗口执行python3 Run.py就好了

注意:持仓方向是双向持仓，杠杆是must_edit_config.json里的leverage

## linux使用说明(路径写死了)

安装请看  mrvl在linux系统安装部署说明.doc文件

如果后续有更新代码，可以直接git下载就好了。在/var/games/mrvl目录下执行git pull就可以更新代码了。

注意:持仓方向是双向持仓，杠杆是must_edit_config.json里的leverage

## 关于代码更新说明
建议使用git命令来下载，这样更新就不影响。

# 更新日志

2021-12-12  初始始上传

# 联系
打开https://small.yjyzj.cn:8443/ 可以扫码加开发者微信

# 关于核心代码编译的说明

    大家想赚钱，那只有跟着大户的车赚点小钱。那些已经实现财富自由的人，请不要使用本机器人，为散户留口汤喝。
    当一个交易对某开仓的方向资金量达到一定的程度，那必然会成为大户的目标，这样再好的策略或者机器人都只能是下酒菜。
    所以，我为了一个策略能使用的足够久而不需要经常去修改参数只能对部分代码进行编译。
    这样首先就让一部分担心安全的人没有了使用的冲动，那会使用的人必然资金量不大或者会使用小号去跑这个机器人。
    这样的结果必然是只要机器人够好，那使用者都可以跟着大户的车赚点小钱。
    当然我也有点小心思，想着这个机器人足够好的话，那我完全可以基于这个策略去做量化平台或者进行收费。为了收费核心代码编译是必须的。

# 用到的链接

    wss://fstream.binance.com/  币安ws
    
    https://fapi.binance.com  币安api
    
    https://oapi.dingtalk.com  发送钉钉webhook消息
    
    https://link.yjyzj.cn/  我的，用来收集异常错误及发微信公众号消息，后续如果收费也会用这个进行授权

## 看到这还在担心资金安全问题，请不要使用本机器人
