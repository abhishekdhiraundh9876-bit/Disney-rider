import os
from PIL import Image
import pillow_heif

# Register HEIF opener with PIL
pillow_heif.register_heif_opener()

images_dir = r"d:\Ashik new project\public\images"
converted_files = []

for filename in os.listdir(images_dir):
    if filename.lower().endswith('.heic'):
        heic_path = os.path.join(images_dir, filename)
        jpg_name = os.path.splitext(filename)[0] + ".jpg"
        jpg_path = os.path.join(images_dir, jpg_name)
        
        try:
            image = Image.open(heic_path)
            image = image.convert('RGB')
            # Resize if extremely large to optimize web load speed
            if image.width > 2400 or image.height > 2400:
                image.thumbnail((2400, 2400), Image.Resampling.LANCZOS)
            image.save(jpg_path, 'JPEG', quality=88, optimize=True)
            converted_files.append((filename, jpg_name, image.width, image.height))
            print(f"Converted {filename} -> {jpg_name}")
        except Exception as e:
            print(f"Error converting {filename}: {e}")

print(f"Total converted: {len(converted_files)}")
