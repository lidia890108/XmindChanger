# xmind-to-markdown-app

该项目是一个将 Xmind 文件中的每个 sheet 批量导出为 Markdown 格式的应用程序。它提供了用户友好的界面，支持文件上传、解析和转换功能。

## 功能

- 支持上传 Xmind 文件
- 解析 Xmind 文件中的每个 sheet
- 将解析后的数据转换为 Markdown 格式
- 批量导出为以 sheet 名称命名的 .md 文件

## 文件结构

```
xmind-to-markdown-app
├── src
│   ├── main.py               # 应用程序入口点
│   ├── ui
│   │   └── interface.py      # 用户界面实现
│   ├── parser
│   │   └── xmind_parser.py   # Xmind 文件解析
│   ├── converter
│   │   └── markdown_converter.py # Markdown 格式转换
│   └── output
│       └── file_writer.py    # 文件输出
├── requirements.txt          # 项目依赖
└── README.md                 # 项目文档
```

## 安装步骤

1. 克隆该项目到本地：
   ```
   git clone <repository-url>
   ```

2. 进入项目目录：
   ```
   cd xmind-to-markdown-app
   ```

3. 安装所需的依赖：
   ```
   pip install -r requirements.txt
   ```

## 使用方法

1. 运行应用程序：
   ```
   python src/main.py
   ```

2. 在用户界面中上传需要转换的 Xmind 文件。

3. 点击转换按钮，等待转换完成。

4. 转换后的 Markdown 文件将保存在指定的输出目录中。