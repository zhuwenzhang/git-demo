print('Hello, World!')

import torch
print(torch.__version__)              # 应显示版本号
print(torch.cuda.is_available())      # 应返回 True（GPU 可用）
print(torch.cuda.get_device_name(0))  # 应显示 "NVIDIA GeForce RTX 4070"