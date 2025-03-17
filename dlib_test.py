import torch
print(torch.cuda.is_available())  # Nếu trả về True, CUDA đang hoạt động
print(torch.cuda.device_count())  # Số GPU khả dụng
print(torch.cuda.get_device_name(0))  # Tên GPU đầu tiên
