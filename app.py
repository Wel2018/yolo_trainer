from .trainer import DetectorTrainer
from .ui_trainer import Ui_MainWindow
from . import q_appcfg
from loguru import logger
from toolbox.core.log import LogHelper, printc
from toolbox.qt import qtbase_future as qtbase
from .util import *


class TrainerApp(qtbase.QApp):
    is_quit_confirm = 0
    
    def __init__(self, parent = None):
        super().__init__(Ui_MainWindow(), parent=parent)
        self.ui: Ui_MainWindow   # 新增类型注解

    def init_after(self):
        self.set_main_app(appcfg=q_appcfg)
        self.set_logger(logger=logger)
        # ✅ 让窗口本身获得焦点（接收键盘事件）
        self.setFocusPolicy(qtbase.Qt.FocusPolicy.StrongFocus)
        self.setFocus()

        ui = self.ui
        qtbase.bind_clicked(ui.btn_train, self.on_train)
        qtbase.bind_clicked(ui.btn_pause, self.on_pause)
        qtbase.bind_clicked(ui.btn_stop, self.on_stop)
        qtbase.bind_clicked(ui.dataset_zip_path_unzip, self.on_dataset_zip_path_unzip)
        qtbase.bind_clicked(ui.dataset_zip_path_select, self.on_dataset_zip_path_select)
        qtbase.bind_clicked(ui.model_weight_dir_select, self.on_model_weight_dir_select)

    def on_stop(self):
        if hasattr(self, "trainer"):
            if self.trainer.isRunning():
                self.trainer.stop()
                self.print("[INFO] 已停止训练任务")
        else:
            self.print("[WARN] 当前没有运行中的训练任务")

    def on_pause(self):
        if hasattr(self, "trainer"):
            if self.trainer.isRunning():
                self.trainer.pause()
                self.print("[INFO] 已暂停训练任务")
        else:
            self.print("[WARN] 当前没有运行中的训练任务")

    def on_train(self):
        # 模型信息
        model_path = self.ui.model_weight_dir.text().strip()
        model_prefix = self.ui.model_prefix.text().strip()
        model_gen = self.ui.model_gen.currentText().strip()
        model_size = self.ui.model_size.currentText().strip()
        model_suffix = self.ui.model_suffix.text().strip()
        model_name = f"{model_prefix}{model_gen}{model_size}"
        if model_suffix:
            model_name += f"-{model_suffix}"

        model_full_path = f"{model_path}/{model_name}.pt"
        self.print(f"模型路径：{model_path}")
        self.print(f"模型名称：{model_name}")
        self.print(f"模型全路径：{model_full_path}")

        # 训练参数
        epochs = int(self.ui.epochs.text().strip())
        batch_size = int(self.ui.batch_size.text().strip())
        img_size = int(self.ui.img_size.text().strip())
        dataset_zip_path = self.ui.dataset_zip_path.text().strip()
        project = self.ui.project.text().strip()
        project = "runs/" + project if not project.startswith("runs/") else project
        exp_name = f"{model_name}"
        data_yaml = self.ui.dataset_data_yaml_path.text().strip()

        self.print(f"训练参数：epochs={epochs}, batch_size={batch_size}, img_size={img_size}")
        self.print(f"数据集压缩包路径：{dataset_zip_path}")
        self.print(f"项目保存路径：{project}")
        self.print(f"模型保存路径：{project}/{exp_name}")
        self.print(f"data_yaml: {data_yaml}")

        isok = self.msgbox((
            f"训练参数：epochs={epochs}, batch_size={batch_size}, img_size={img_size}\n"
            f"数据集压缩包路径：{dataset_zip_path}\n"
            f"项目保存路径：{project}\n"
            f"模型保存路径：{project}/{exp_name}\n"
        ), title="训练 YOLO 模型")

        if not isok:
            self.print("[WARN] 用户取消了训练任务")
            return
        
        self.trainer = DetectorTrainer(
            data_yaml=data_yaml,
            weights=model_full_path,
            epochs=epochs,
            batch_size=batch_size,
            img_size=img_size,
            project=project,
            exp_name=exp_name
        )
        self.trainer.sig_msg.connect(self.on_trainer_msg)
        self.trainer.start()
    

    def on_trainer_msg(self, msg: str):
        self.print(f"[INFO] 训练任务完成，状态：{msg}")
        self.msgbox(f"训练任务完成，状态：{msg}")

    def on_dataset_zip_path_unzip(self):
        zip_path = self.ui.dataset_zip_path.text().strip()
        unzip_to_same_named_folder(zip_path)
        self.print(f"[INFO] 数据集解压完成，输出目录：{os.path.dirname(zip_path)}")
        self.msgbox(f"数据集解压完成，输出目录：{os.path.dirname(zip_path)}")
        data_yaml_path = zip_path.replace(".zip", "") + "/data.yaml"
        self.ui.dataset_data_yaml_path.setText(data_yaml_path)
        update_first_three_lines(data_yaml_path)


    def select_files(self):
        files, _ = qtbase.QtWidgets.QFileDialog.getOpenFileNames(
            self,
            "选择多个文件",
            "",
            "图片文件 (*.png *.jpg *.jpeg)"
        )
        self.print(f"选中文件 {files}")
        return files

    def select_file(self, caption="选择文件", filetype="所有文件 (*.*)"):
        # "所有文件 (*.*);;图片文件 (*.png *.jpg *.jpeg);;文本文件 (*.txt)"
        file_path, _ = qtbase.QtWidgets.QFileDialog.getOpenFileName(
            self,
            caption,
            ".cache",
            filetype
        )
        # if file_path:
        self.print(f"选择的文件：{file_path}")
        return file_path

    def select_folder(self, caption="选择文件夹"):
        folder_path = qtbase.QtWidgets.QFileDialog.getExistingDirectory(
            self,
            caption,
            ""
        )
        # if folder_path:
        self.print(f"选择的文件夹：{folder_path}")
        return folder_path

    def save_file(self):
        save_path, _ = qtbase.QtWidgets.QFileDialog.getSaveFileName(
            self,
            "保存文件",
            "",
            "所有文件 (*.*);;文本文件 (*.txt);;图片文件 (*.png *.jpg *.jpeg)"
        )
        # if save_path:
        self.print(f"保存的文件：{save_path}")
        return save_path


    def on_dataset_zip_path_select(self):
        path = self.select_file(caption="选择数据集压缩包", filetype="ZIP Files (*.zip);;All Files (*)")
        if path:
            self.ui.dataset_zip_path.setText(path)
    
    def on_model_weight_dir_select(self):
        path = self.select_folder("选择模型权重保存目录")
        if path:
            self.ui.model_weight_dir.setText(path)


def main():
    LogHelper.init(q_appcfg.slot)
    printc(f"q_appcfg={q_appcfg}")
    
    import sys
    qapp = qtbase.QApplication(sys.argv)
    # 设置全局默认字体
    qapp.setFont(qtbase.QFont("微软雅黑", 11))
    mapp = TrainerApp()
    mapp.show()
    # 不生效，会被抢占焦点
    # mapp.raise_()          # 提升窗口到最上层
    # mapp.activateWindow()  # 请求激活该窗口
    sys.exit(qapp.exec())
