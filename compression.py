import PIL.Image
import os.path
import sys

path = sys.path[0]
real_path = os.path.join(path, "real_img")
pill_img = os.path.join(path, "compression_img")
img_format = [".JPG", ".JPEG", ".CR2"]

if not os.path.exists(real_path):
    os.mkdir(real_path)

if not os.path.exists(pill_img):
    os.mkdir(pill_img)

for root, dirs, files in os.walk(real_path):
    for f in files:
        format_name = os.path.splitext(f)
        # 是图片文件
        if format_name[-1].upper() in img_format:
            fp = os.path.join(root, f)
            print(fp)
            img = PIL.Image.open(fp)
            w, h = img.size
            img.thumbnail((w / 2, h / 2))
            img.save(os.path.join(pill_img, f), "JPEG")
