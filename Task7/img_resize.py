import os
from PIL import Image

def resize_images(input_folder="images", output_folder="resized", size=(400, 300)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        try:
            img_path = os.path.join(input_folder, file_name)
            img = Image.open(img_path)

            # resize
            img_resized = img.resize(size)

            # save as JPG
            output_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.jpg")
            img_resized.save(output_path)

            print(f"✅ Resized & saved: {output_path}")
        except Exception as e:
            print(f"❌ Could not process {file_name}: {e}")

if __name__ == "__main__":
    resize_images()
