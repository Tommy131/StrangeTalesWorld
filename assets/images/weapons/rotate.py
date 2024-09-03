from PIL import Image

def rotate_image(image_path, output_path, angle):
    # 打开图像文件
    with Image.open(image_path) as img:
        # 旋转图像, 使用高质量的插值方法
        rotated_img = img.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)
        # 保存旋转后的图像, 选择适当的格式和质量
        rotated_img.save(output_path, format='PNG', quality=100)  # 可以改为 'JPEG' 并设置 quality 参数

# 示例数据
input_image_path = './default_weapon.png'  # 替换为你的图像路径
output_image_path = './weapon.png'  # 保存旋转后的图像路径
rotation_angle = 20  # 旋转角度

# 调用函数
rotate_image(input_image_path, output_image_path, rotation_angle)
