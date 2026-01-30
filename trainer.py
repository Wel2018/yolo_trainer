import os
from ultralytics import YOLO  # type: ignore
from toolbox.core.log import printc
from toolbox.qt import qtbase


class DetectorTrainer(qtbase.QAsyncTask):
    """
    - 用于训练 YOLO 模型
    """
    def __init__(
        self,
        data_yaml: str,
        weights: str,
        epochs: int,
        batch_size: int,
        img_size: int,
        project: str,
        exp_name: str,
        exist_ok: bool = True,
    ):
        """
        训练 YOLO 模型

        Args:
            data_yaml: 数据集配置文件路径
            weights: 预训练权重路径
            epochs: 训练轮数
            batch_size: 批大小
            img_size: 输入图像尺寸
            project: 输出项目目录
            name: 输出实验名称
            exist_ok: 是否覆盖已存在的输出目录
        """
        super().__init__()
        self.data_yaml = data_yaml
        self.weights = weights
        self.epochs = epochs
        self.batch_size = batch_size
        self.img_size = img_size
        self.project = project
        self.exp_name = exp_name
        self.exist_ok = exist_ok

    def run(self):
        printc(f"[INFO] 开始训练 YOLO 模型，数据集：{self.data_yaml}")
        model = YOLO(self.weights)  # type: ignore

        model.train(
            data=self.data_yaml,
            epochs=self.epochs,
            # patience=20,
            batch=self.batch_size,
            imgsz=self.img_size,
            project=self.project,
            name=self.exp_name,
            exist_ok=self.exist_ok,
            # warmup_epochs=0,
        )

        printc(f"[INFO] YOLO 模型训练完成，输出目录：{os.path.join(self.project, self.exp_name)}")
        self.sig_msg.emit("ok")
