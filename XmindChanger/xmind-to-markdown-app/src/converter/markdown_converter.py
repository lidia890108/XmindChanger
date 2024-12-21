class MarkdownConverter:
    def __init__(self, data):
        self.data = data

    def convert(self):
        markdown_content = {}
        for sheet in self.data:
            sheet_title = sheet['title']
            markdown_content[sheet_title] = self._convert_sheet_to_markdown(sheet)
        return markdown_content

    def _convert_sheet_to_markdown(self, sheet):
        markdown_lines = []
        self._add_topic_to_markdown(sheet['content'], markdown_lines, 1)
        return '\n'.join(markdown_lines)

    def _add_topic_to_markdown(self, topics, markdown_lines, level):
        for topic in topics:
            markdown_lines.append(f"{'#' * level} {topic['title']}")
            if 'children' in topic:
                self._add_topic_to_markdown(topic['children'], markdown_lines, level + 1)

def convert_xmind_to_markdown(sheets_data):
    # 在这里实现将 sheets_data 转换为 Markdown 的逻辑
    markdown_content = ""
    # ...转换逻辑...
    return markdown_content