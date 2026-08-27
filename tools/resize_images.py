from PIL import Image
import os
src = r"C:\Users\USER\Downloads\adonai-farm-website\adonai-farm\images"
widths = [480,800,1200]
count=0
for fname in os.listdir(src):
    if not (fname.lower().endswith('.jpg') or fname.lower().endswith('.jpeg')): continue
    path = os.path.join(src,fname)
    name,ext = os.path.splitext(fname)
    try:
        img = Image.open(path)
    except Exception as e:
        print('skip',fname,str(e))
        continue
    for w in widths:
        if img.width <= w:
            # don't upscale; if exact already, copy to suffix
            dest = os.path.join(src, f"{name}-{w}{ext}")
            if not os.path.exists(dest):
                img.save(dest, quality=85)
                print('wrote',dest)
                count+=1
            else:
                print('exists',dest)
        else:
            ratio = w / float(img.width)
            h = int(round(img.height * ratio))
            dest = os.path.join(src, f"{name}-{w}{ext}")
            if not os.path.exists(dest):
                resized = img.resize((w,h), Image.LANCZOS)
                resized.save(dest, quality=85)
                print('wrote',dest)
                count+=1
            else:
                print('exists',dest)
    img.close()
print('done, created',count)
