# Python 面试题独立工程集

本目录包含从 `programming.md` 导出的 85 个独立 Python 工程，目录名前两位是题号。

每个题目工程均包含：

- `README.md`：整理后的题目、详细解题思路、正确性说明、复杂度分析及样例测试说明；
- `solution.py`：可独立使用的 Python 实现，关键步骤包含中文注释；
- `test_solution.py`：使用 Python 标准库 `unittest` 编写的题内样例测试。

## 运行单题测试

进入对应题目目录后运行：

```bash
python3 -m unittest -v test_solution.py
```

例如：

```bash
cd 01-largest-word-length
python3 -m unittest -v test_solution.py
```

## 运行全量验收

在仓库根目录运行：

```bash
python3 tools/verify_programming_projects.py
```

该命令会检查 1–85 编号是否连续、每个工程的必需文件是否完整、Python 文件能否编译，以及所有单元测试能否在各自工程目录中独立通过。

## 原题数据问题

少量原始题目存在样例输入数量、旋转步数、输出或排版不一致。相关工程的 `README.md` 已逐项说明，并按明确题意及可复算结果编写测试，没有静默迎合错误样例。
