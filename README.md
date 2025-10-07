
## ffmpeg

### 144p
ffmpeg -i bunny_30s.y4m -vf scale=256:144 -c:v libx264 -preset medium -crf 23 bunny_144p.mp4
```

### 240p
ffmpeg -i bunny_30s.y4m -vf scale=426:240 -c:v libx264 -preset medium -crf 23 bunny_240p.mp4


### 360p
ffmpeg -i bunny_30s.y4m -vf scale=640:360 -c:v libx264 -preset medium -crf 23 bunny_360p.mp4


### 480p

ffmpeg -i bunny_30s.y4m -vf scale=854:480 -c:v libx264 -preset medium -crf 23 bunny_480p.mp4


### 720p

ffmpeg -i bunny_30s.y4m -vf scale=1280:720 -c:v libx264 -preset medium -crf 23 bunny_720p.mp4


### 1080p
ffmpeg -i bunny_30s.y4m -vf scale=1920:1080 -c:v libx264 -preset medium -crf 23 bunny_1080p.mp4


##  VMAF

# VMAF для 144p
ffmpeg -i bunny_144p.mp4 -i bunny_30s.y4m -lavfi "[0:v]scale=1920:1080:flags=bicubic[dist];[dist][1:v]libvmaf=log_path=vmaf_144p.json:log_fmt=json" -f null -

# VMAF для 240p
ffmpeg -i bunny_240p.mp4 -i bunny_30s.y4m -lavfi "[0:v]scale=1920:1080:flags=bicubic[dist];[dist][1:v]libvmaf=log_path=vmaf_240p.json:log_fmt=json" -f null -

# VMAF для 360p
ffmpeg -i bunny_360p.mp4 -i bunny_30s.y4m -lavfi "[0:v]scale=1920:1080:flags=bicubic[dist];[dist][1:v]libvmaf=log_path=vmaf_360p.json:log_fmt=json" -f null -

# VMAF для 480p
ffmpeg -i bunny_480p.mp4 -i bunny_30s.y4m -lavfi "[0:v]scale=1920:1080:flags=bicubic[dist];[dist][1:v]libvmaf=log_path=vmaf_480p.json:log_fmt=json" -f null -

# VMAF для 720p
ffmpeg -i bunny_720p.mp4 -i bunny_30s.y4m -lavfi "[0:v]scale=1920:1080:flags=bicubic[dist];[dist][1:v]libvmaf=log_path=vmaf_720p.json:log_fmt=json" -f null -

# VMAF для 1080p
ffmpeg -i bunny_1080p.mp4 -i bunny_30s.y4m -lavfi "libvmaf=log_path=vmaf_1080p.json:log_fmt=json" -f null -
```

##

ffprobe -v error -show_entries format=bit_rate -of default=noprint_wrappers=1:nokey=1 bunny_144p.mp4
ffprobe -v error -show_entries format=bit_rate -of default=noprint_wrappers=1:nokey=1 bunny_240p.mp4
ffprobe -v error -show_entries format=bit_rate -of default=noprint_wrappers=1:nokey=1 bunny_360p.mp4
ffprobe -v error -show_entries format=bit_rate -of default=noprint_wrappers=1:nokey=1 bunny_480p.mp4
ffprobe -v error -show_entries format=bit_rate -of default=noprint_wrappers=1:nokey=1 bunny_720p.mp4
ffprobe -v error -show_entries format=bit_rate -of default=noprint_wrappers=1:nokey=1 bunny_1080p.mp4




python extract_vmaf.py


