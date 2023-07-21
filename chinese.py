import json
from opencc import OpenCC

def convert_json_file(input_file, output_file, conversion_type='s2twp'):
    """
    將JSON檔案中的文字從簡體轉換成繁體。

    Parameters:
        input_file (str): 輸入的JSON檔案名稱（包含路徑）。
        output_file (str): 轉換後的JSON檔案名稱（包含路徑）。
        conversion_type (str): 轉換類型，預設為's2twp'（簡體到台灣繁體）。

    Returns:
        None
    """
    # 建立OpenCC物件
    cc = OpenCC(conversion_type)

    # 讀取JSON檔案
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 對JSON檔案中的所有文字進行轉換
    converted_data = recursive_convert(data, cc)

    # 寫入轉換後的JSON檔案
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(converted_data, f, ensure_ascii=False, indent=2)

def recursive_convert(data, cc):
    """
    遞迴函式，對JSON檔案中的所有文字進行轉換。

    Parameters:
        data: JSON資料。
        cc: OpenCC物件。

    Returns:
        轉換後的JSON資料。
    """
    if isinstance(data, dict):
        return {key: recursive_convert(value, cc) for key, value in data.items()}
    elif isinstance(data, list):
        return [recursive_convert(item, cc) for item in data]
    elif isinstance(data, str):
        return cc.convert(data)
    else:
        return data

# 執行轉換
input_file = 'a.json'  # 輸入的JSON檔案名稱（包含路徑）
output_file = 'output.json'  # 轉換後的JSON檔案名稱（包含路徑）

convert_json_file(input_file, output_file)
