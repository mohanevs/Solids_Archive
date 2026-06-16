# import os
# import json

# ROOT = r"E:\SolidsArchive\resources"

# def build_tree(path):
#     tree = {}
#     for entry in sorted(os.listdir(path)):
#         full = os.path.join(path, entry)
#         if os.path.isdir(full):
#             tree[entry] = build_tree(full)
#         else:
#             tree.setdefault("_files", []).append(entry)
#     return tree

# if __name__ == "__main__":
#     result = build_tree(ROOT)
#     with open("folder_structure.json", "w") as f:
#         json.dump(result, f, indent=2)
#     print(json.dumps(result, indent=2))


# import json

# data = []

# # --- 3D Models ---
# for i in range(1, 58):  # 001 to 057
#     num = f"{i:03d}"
#     name = f"3DM{num}"
#     data.append({
#         "name": name,
#         "category": "3D Model",
#         "image": f"resources/3D Model/{name}.png",
#         "url": f"https://github.com/mohanevs/solid-modeling-catia-v6/blob/main/3D%20Models/{name}.CATPart"
#     })

# # --- Assemblies ---
# assemblies = {
#     "1. Screw Jack": ["body.png", "cup.png", "nut.png", "screw jack assmbled.png", "screw.png", "screwSpindle.png", "tommyBar.png", "washer.png"],
#     "2. Knuckle Joint": ["collar.png", "eye end.png", "fork end.png", "knuckle joint assembled.png", "pin.png", "taper pin.png"],
#     "3. Pipe Vice": ["base.png", "handle screw.png", "handle.png", "movable jaw.png", "pipe vice assembled.png", "screw.png"],
#     "4. Plummer Block": ["bolt.png", "brasses.png", "cap.png", "casting.png", "lock nut.png", "nut.png", "plummer block assembled.png"],
#     "5. Press Tool": ["@press tool assembled.png", "bottom plate.png", "guide bush.png", "guide pillar.png", "top Plate.png"],
#     "6. Tool Head of Shaper": ["@tool head of shaper assembled.png", "back plate.png", "bush washer.png", "clamping screw.png", "drag plate.png", "handle br.png", "handle.png", "nut.png", "pivot pin.png", "small washer.png", "space bush.png", "swivel plate.png", "swivel screw pin.png", "tool fixing screw.png", "tool holder.png", "vertical slide.png", "washer.png"],
#     "7. Motor Blower": ["@motor blower assemled.png", "blower.png", "cover.png", "lower housing.png", "motor.png", "shaft.png", "upper housing.png"]
# }

# from urllib.parse import quote

# for folder, files in assemblies.items():
#     for f in files:
#         part_name = f.rsplit(".", 1)[0]
#         data.append({
#             "name": f"{folder} - {part_name}",
#             "category": "Assembly",
#             "image": f"resources/Assembly/{folder}/{f}",
#             "url": f"https://github.com/mohanevs/solid-modeling-catia-v6/tree/main/Assembly/{quote(folder)}"
#         })

# with open("data.json", "w") as out:
#     json.dump(data, out, indent=4)

# print(f"Wrote {len(data)} entries to data.json")


# from pathlib import Path
# from PIL import Image, ImageOps

# RESOURCE_DIR = Path("E:/SolidsArchive/resources")  # adjust to your actual resources folder path
# TARGET_SIZE = (500, 500)          # width, height in pixels — adjust as needed
# BG_COLOR = (255, 255, 255)        # white background padding

# IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg"}

# def resize_with_padding(img: Image.Image, size: tuple, bg_color: tuple) -> Image.Image:
#     img = img.convert("RGBA") if img.mode in ("P", "RGBA") else img.convert("RGB")

#     # Resize while keeping aspect ratio, fit inside target size
#     img_resized = ImageOps.contain(img, size)

#     # Create new background canvas
#     background = Image.new("RGB", size, bg_color)

#     # Paste resized image centered
#     offset = (
#         (size[0] - img_resized.width) // 2,
#         (size[1] - img_resized.height) // 2,
#     )

#     if img_resized.mode == "RGBA":
#         background.paste(img_resized, offset, img_resized)
#     else:
#         background.paste(img_resized, offset)

#     return background

# def process_folder(folder: Path):
#     for file in folder.rglob("*"):
#         if file.suffix.lower() in IMAGE_EXTENSIONS:
#             try:
#                 img = Image.open(file)
#                 processed = resize_with_padding(img, TARGET_SIZE, BG_COLOR)
#                 processed.save(file)  # overwrites original
#                 print(f"Resized: {file}")
#             except Exception as e:
#                 print(f"Skipped {file} (error: {e})")

# if __name__ == "__main__":
#     process_folder(RESOURCE_DIR)
