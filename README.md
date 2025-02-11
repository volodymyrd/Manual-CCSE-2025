# Manual-CCSE-2025
ffmpeg -loop 1 -i cover.jpg -i 0_title.ssml.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest 0_title.ssml.mp4
