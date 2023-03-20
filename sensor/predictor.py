import os
from sensor.entity.config_entity import TRANSFORMER_OBJECT_FILE_NAME, MODEL_FILE_NAME, TARGET_ENCODER_OBJECT_FILE_NAME
from glob import glob
from typing import Optional
import os

class ModelResolver:

    def __init__(self,model_registry:str = "saved_models",
                transformer_dir_name = "transformer",
                target_encoder_dir_name = "target_encoder",
                model_dir_name = "model"):

        self.model_registry = model_registry
        os.makedirs(self.model_registry, exist_ok=True)
        self.transformer_dir_name = transformer_dir_name
        self.target_encoder_dir_name = target_encoder_dir_name
        self.model_dir_name=model_dir_name

    def get_latest_dir_path(self)->Optional[str]:
        try:
            dir_names = os.listdir(self.model_registry)
            if len(dir_names) == 0:
                return None
            dir_names = list(map(int,dir_names))
            latest_dir_name = max(dir_names)
            return os.path.join(self.model_registry,f"{latest_dir_name}")
        except Exception as e:
            raise e

    def det_latest_model_path(self):
        try:
            dir_names = os.lisrdir(self.model_registry)
            if len(dir_names) == 0:
                return None
            dir_names = list(map(int, dir_names))
            latest_dir_name = max(dir_names)
            return os.path.join(self.model_registry,f"{latest_dir_name}")
        except Exception as e:
            raise e
