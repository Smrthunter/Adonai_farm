from PIL import Image
import os
src = r"C:\Users\USER\Downloads\adonai-farm-website\adonai-farm\images\logo-v2.jpeg"
outdir = r"C:\Users\USER\Downloads\adonai-farm-website\adonai-farm\images"
img = Image.open(src).convert('RGBA')
# PNG 32x32
png32 = img.resize((32,32), Image.LANCZOS)
png32.save(os.path.join(outdir,'favicon-32x32.png'), format='PNG')
# Apple touch 180
apple = img.resize((180,180), Image.LANCZOS)
apple.save(os.path.join(outdir,'apple-touch-icon-180.png'), format='PNG')
# ICO (16,32,48)
ico_sizes = [(16,16),(32,32),(48,48)]
ico_imgs = [img.resize(s, Image.LANCZOS) for s in ico_sizes]
ico_path = os.path.join(outdir,'favicon.ico')
# Pillow can save multi-size ico by passing sizes
img.save(ico_path, format='ICO', sizes=[(16,16),(32,32),(48,48)])
print('wrote', os.path.join(outdir,'favicon-32x32.png'))
print('wrote', os.path.join(outdir,'apple-touch-icon-180.png'))
print('wrote', ico_path)
