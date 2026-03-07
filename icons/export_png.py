#!/usr/bin/env python3
"""Export all SVGs to PNG at 24px, 48px, and 96px sizes"""

import cairosvg
import os

SVG_DIR = '/home/ubuntu/saya_icons/svg'
PNG_DIR = '/home/ubuntu/saya_icons/png'

sizes = [24, 48, 96]

svg_files = [f for f in os.listdir(SVG_DIR) if f.endswith('.svg')]
svg_files.sort()

for size in sizes:
    size_dir = os.path.join(PNG_DIR, f'{size}px')
    os.makedirs(size_dir, exist_ok=True)

total = 0
for svg_file in svg_files:
    name = svg_file.replace('.svg', '')
    svg_path = os.path.join(SVG_DIR, svg_file)
    
    for size in sizes:
        png_path = os.path.join(PNG_DIR, f'{size}px', f'{name}.png')
        cairosvg.svg2png(
            url=svg_path,
            write_to=png_path,
            output_width=size,
            output_height=size
        )
        total += 1

print(f'Exported {total} PNG files ({len(svg_files)} icons × {len(sizes)} sizes)')
