from pathlib import Path, PurePath
import tqdm
from typing import Union
from utils.datasets import addv7data


tainpath = Path("/home/ncst/YOU/pro/MHSO6/images/train")
valpath = Path("/home/ncst/YOU/pro/MHSO6/images/val")

txtpath = Path("/home/ncst/YOU/pro/MHSO6")

if __name__ == "__main__":
    # addv7data(valpath, PurePath.joinpath(txtpath, "val.txt"))
    pass


