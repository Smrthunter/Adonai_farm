from PIL import Image
import os
src = r"C:\Users\USER\Downloads\adonai-farm-website\adonai-farm\images"
widths = [480,800,1200]
created = []
for fname in os.listdir(src):
    if not (fname.lower().endswith('.jpg') or fname.lower().endswith('.jpeg') or fname.lower().endswith('.png')):
        continue
    path = os.path.join(src,fname)
    name,ext = os.path.splitext(fname)
    try:
        img = Image.open(path)
    except Exception as e:
        print('skip',fname,str(e))
        continue
    for w in widths:
        dest = os.path.join(src, f"{name}-{w}{ext}")
        if os.path.exists(dest):
            print('exists', os.path.basename(dest))
            continue
        if img.width <= w:
            img.save(dest, quality=85)
            print('copied', os.path.basename(dest))
            created.append(dest)
        else:
            ratio = w / float(img.width)
            h = int(round(img.height * ratio))
            resized = img.resize((w,h), Image.LANCZOS)
            resized.save(dest, quality=85)
            print('wrote', os.path.basename(dest))
            created.append(dest)
    img.close()
print('done, created', len(created))
