import os

def save_markdown_files(sheet_data, output_directory):
    """
    将每个 sheet 的 Markdown 内容保存为 .md 文件。
    
    :param sheet_data: 包含每个 sheet 名称及其对应的 Markdown 内容的字典
    :param output_directory: 输出文件夹路径
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for sheet_name, markdown_content in sheet_data.items():
        file_name = f"{sheet_name}.md"
        file_path = os.path.join(output_directory, file_name)
        
        write_to_files(file_path, markdown_content)

def write_to_files(file_path, markdown_content):
    # 在这里实现将 markdown_content 写入文件的逻辑
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)

def save_markdown_to_file(markdown_content):
    # 在这里实现将 markdown_content 写入文件的逻辑
    with open("output.md", "w", encoding="utf-8") as f:
        f.write(markdown_content)