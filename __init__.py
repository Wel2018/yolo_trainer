"""YOLO 训练程序"""

from toolbox.qt import qtbase
from .version import __version__
from .version import __update_timestamp__


q_appcfg = qtbase.QAppConfig(
    name = "YOLO 训练程序",
    name_en = "YOLO Trainer Client",
    date = __update_timestamp__,
    version = __version__,
    fontsize = 14,
    slot="yolo_trainer",
    APPCFG_DICT=qtbase.get_appcfg(__file__),
)

ROOT = q_appcfg.ROOT
