## 学习python

> 1. javascript 技术栈reactjs
> 2. 预处理器less

## 目录结构

```
+ -- dist           前端文件输出文件夹
+ -- config         webpack 及环境相关配置
+ -- mock           系统mock数据
+ -- scripts        npm 对应的相关命令
+ -- src            源代码
  + -- assets       资源库
  + -- css          样式文件（scss）
  + -- js           业务逻辑
  + -- index.ejs    入口页面模板

```

##工程配置

####安装淘宝镜像
```bash
$ npm install -g cnpm --registry=https://registry.npm.taobao.org
```

####工程依赖

``` bash
# install dependencies
cnpm install

# serve with hot reload at http://localhost:8088
npm run dev 或者 npm start

# check the javascript coding unify and illegal
npm run eslint

```
