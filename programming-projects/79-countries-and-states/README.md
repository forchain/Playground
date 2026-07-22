# 79. Countries and States

## 题目
平台提供异步 `getCountry(index)` 和 `getStates(country)`。返回指定国家中人口最多的州名；国家索引无效时返回 `ind = {index} invalid`。样例 0、1、10000 分别输出 `Karnataka`、`Michigan`、无效提示。

Python 接口为 `await solution(index,getCountry,getStates)`，以参数注入平台函数，使工程可独立测试。

## 解析
依次等待国家名和州列表，用人口字段作为键取最大记录；任一国家查询异常按题目返回无效提示。

## 正确性与复杂度
`max` 比较每个州人口，返回值不小于列表中任何州，故为人口最大州；查询拒绝被转换为规定提示。设州数为 `s`，时间 `O(s)`、除返回数据外空间 `O(1)`。异步单测模拟原题三例。
