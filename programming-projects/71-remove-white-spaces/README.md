# 71. Remove White Spaces

## 题目
不使用内置去空格函数，删除字符串中的所有普通空格字符。接口 `solution(text)`。

样例：`Rise and shine` 变为 `Riseandshine`；`Visual Studio Code` 变为 `VisualStudioCode`。

## 解析
逐字符扫描，把不等于普通空格 `" "` 的字符加入结果，最后连接。题目样例和表述中的 spaces 均指普通空格。

## 正确性与复杂度
每个非空格字符按原顺序加入且每个空格均被跳过，所以结果恰为删除所有空格后的字符串。时间、空间均为 `O(n)`。测试覆盖原题两例。
