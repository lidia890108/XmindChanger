import xmindparser

def parse_xmind(file_path):
    return xmindparser.xmind_to_dict(file_path)