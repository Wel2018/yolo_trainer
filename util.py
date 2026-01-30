
import zipfile
import os
from toolbox.core.log import printc


def update_first_three_lines(yaml_path):
    """将数据集描述文件 data.yaml 的前3行f"""
    new_lines = [
        "train: ./train/images\n",
        "val: ./valid/images\n",
        "test: ./test/images\n"
    ]

    # 读取原文件
    with open(yaml_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # 替换前 3 行
    lines[:3] = new_lines

    # 写回文件
    with open(yaml_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

    printc("已修改 data.yaml 前 3 行！")


def unzip_to_same_named_folder(zip_path):
    # 压缩包所在目录
    base_dir = os.path.dirname(zip_path)

    # 压缩包名称（不带扩展名）
    folder_name = os.path.splitext(os.path.basename(zip_path))[0]

    # 目标文件夹
    target_dir = os.path.join(base_dir, folder_name)

    # 创建文件夹（存在也不报错）
    os.makedirs(target_dir, exist_ok=True)

    # 解压
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(target_dir)

    printc(f"解压完成：{target_dir}")
