from PIL import Image, ImageSequence

# Load the newly uploaded GIF file
input_gif_path = '/mnt/data/Alura.gif'
output_gif_path = '/mnt/data/Alura_compressed.gif'

# Open the original GIF
original_gif = Image.open(input_gif_path)

# Set target size in bytes (15 MB)
target_size_bytes = 15 * 1024 * 1024

# Function to save the GIF with a target size
def save_compressed_gif(original_gif, output_path, max_size_bytes):
    frames = [frame.copy() for frame in ImageSequence.Iterator(original_gif)]
    
    # Reduce frame size
    new_frames = []
    for frame in frames:
        frame = frame.resize((frame.width // 2, frame.height // 2), Image.ANTIALIAS)
        new_frames.append(frame.convert('P', palette=Image.ADAPTIVE))
    
    # Save GIF with reduced quality and frame size
    new_frames[0].save(output_path, save_all=True, append_images=new_frames[1:], optimize=True, duration=original_gif.info['duration'], loop=0)

# Save the compressed GIF
save_compressed_gif(original_gif, output_gif_path, target_size_bytes)

# Check the file size of the compressed GIF
import os
compressed_size = os.path.getsize(output_gif_path)
compressed_size_mb = compressed_size / (1024 * 1024)

compressed_size_mb, output_gif_path
