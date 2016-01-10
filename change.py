import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for fname in files:
	filename, ext = os.path.splitext(fname)
	if ext == ".png":
		 os.system("convert "+fname+" "+filename+".xbm")
