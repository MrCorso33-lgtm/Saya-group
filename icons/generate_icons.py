#!/usr/bin/env python3
"""
Saya Group Icon Set Generator
Generates all SVG icons needed for the website.
Style: Clean, modern, 2px stroke, rounded caps/joins, 24x24 viewBox
Colors: Dark navy #1a1a2e (default), accent #c8a96e (gold)
"""

import os

SVG_DIR = '/home/ubuntu/saya_icons/svg'

# SVG template wrapper
def svg(name, paths, viewbox="0 0 24 24", stroke="#1a1a2e", fill="none", stroke_width="1.8"):
    content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}" width="24" height="24" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round">
  {paths}
</svg>'''
    filepath = os.path.join(SVG_DIR, f'{name}.svg')
    with open(filepath, 'w') as f:
        f.write(content)
    print(f'  ✓ {name}.svg')

# ─────────────────────────────────────────────
# HEADER / UI ICONS
# ─────────────────────────────────────────────

# 1. Phone
svg('phone', '''
  <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.07 11.5a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3 .82h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L7.09 8.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 21 16z"/>
''')

# 2. Email / Envelope
svg('email', '''
  <rect x="2" y="4" width="20" height="16" rx="2"/>
  <polyline points="2,4 12,13 22,4"/>
''')

# 3. Location / Map Pin
svg('location', '''
  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
  <circle cx="12" cy="10" r="3"/>
''')

# 4. Search / Magnifier
svg('search', '''
  <circle cx="11" cy="11" r="8"/>
  <line x1="21" y1="21" x2="16.65" y2="16.65"/>
''')

# 5. Wishlist / Heart
svg('wishlist', '''
  <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
''')

# 6. Shopping Cart
svg('cart', '''
  <circle cx="9" cy="21" r="1"/>
  <circle cx="20" cy="21" r="1"/>
  <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/>
''')

# 7. User / Account
svg('user', '''
  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
  <circle cx="12" cy="7" r="4"/>
''')

# 8. Language / Globe
svg('language', '''
  <circle cx="12" cy="12" r="10"/>
  <line x1="2" y1="12" x2="22" y2="12"/>
  <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
''')

# 9. Menu / Hamburger
svg('menu', '''
  <line x1="3" y1="6" x2="21" y2="6"/>
  <line x1="3" y1="12" x2="21" y2="12"/>
  <line x1="3" y1="18" x2="21" y2="18"/>
''')

# 10. Close / X
svg('close', '''
  <line x1="18" y1="6" x2="6" y2="18"/>
  <line x1="6" y1="6" x2="18" y2="18"/>
''')

# 11. Chevron Down (dropdown arrow)
svg('chevron-down', '''
  <polyline points="6 9 12 15 18 9"/>
''')

# 12. Chevron Right
svg('chevron-right', '''
  <polyline points="9 18 15 12 9 6"/>
''')

# 13. Arrow Right (CTA)
svg('arrow-right', '''
  <line x1="5" y1="12" x2="19" y2="12"/>
  <polyline points="12 5 19 12 12 19"/>
''')

# ─────────────────────────────────────────────
# PRODUCT / CATEGORY ICONS
# ─────────────────────────────────────────────

# 14. Tile / Pločice
svg('tiles', '''
  <rect x="2" y="2" width="9" height="9" rx="1"/>
  <rect x="13" y="2" width="9" height="9" rx="1"/>
  <rect x="2" y="13" width="9" height="9" rx="1"/>
  <rect x="13" y="13" width="9" height="9" rx="1"/>
''')

# 15. Sanitaryware / Toilet
svg('sanitaryware', '''
  <path d="M7 4h10a1 1 0 0 1 1 1v2H6V5a1 1 0 0 1 1-1z"/>
  <path d="M6 7c0 6 2 10 6 11s6-5 6-11"/>
  <line x1="12" y1="18" x2="12" y2="21"/>
  <line x1="9" y1="21" x2="15" y2="21"/>
''')

# 16. Bathroom Furniture / Cabinet
svg('furniture', '''
  <rect x="3" y="3" width="18" height="18" rx="2"/>
  <line x1="3" y1="12" x2="21" y2="12"/>
  <line x1="12" y1="3" x2="12" y2="21"/>
  <circle cx="7.5" cy="7.5" r="1" fill="#1a1a2e" stroke="none"/>
  <circle cx="7.5" cy="16.5" r="1" fill="#1a1a2e" stroke="none"/>
  <circle cx="16.5" cy="7.5" r="1" fill="#1a1a2e" stroke="none"/>
  <circle cx="16.5" cy="16.5" r="1" fill="#1a1a2e" stroke="none"/>
''')

# 17. Faucet / Baterije
svg('faucet', '''
  <path d="M5 12h6"/>
  <path d="M11 8v8"/>
  <path d="M11 8a4 4 0 0 1 8 0v1h2v2h-2v1a4 4 0 0 1-4 4"/>
  <path d="M5 10a2 2 0 1 0 0 4"/>
  <line x1="2" y1="12" x2="5" y2="12"/>
''')

# 18. Bathtub / Kade
svg('bathtub', '''
  <path d="M4 12h16v3a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5v-3z"/>
  <path d="M6 12V6a2 2 0 0 1 2-2h1a2 2 0 0 1 2 2v1"/>
  <line x1="7" y1="20" x2="7" y2="22"/>
  <line x1="17" y1="20" x2="17" y2="22"/>
''')

# 19. Shower / Tus
svg('shower', '''
  <path d="M4 4l4 4"/>
  <path d="M4 8l4-4"/>
  <path d="M8 4a6 6 0 0 1 6 6"/>
  <path d="M14 10l-4 10"/>
  <circle cx="11" cy="17" r="0.5" fill="#1a1a2e" stroke="none"/>
  <circle cx="13" cy="19" r="0.5" fill="#1a1a2e" stroke="none"/>
  <circle cx="9" cy="19" r="0.5" fill="#1a1a2e" stroke="none"/>
  <circle cx="11" cy="21" r="0.5" fill="#1a1a2e" stroke="none"/>
''')

# 20. Accessories / Oprema
svg('accessories', '''
  <circle cx="12" cy="12" r="3"/>
  <path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"/>
''')

# 21. Brands / Star
svg('brands', '''
  <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
''')

# 22. News / Article
svg('news', '''
  <path d="M4 22h16a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v16a2 2 0 0 0-2 2zm0 0a2 2 0 0 1-2-2v-9c0-1.1.9-2 2-2h2"/>
  <path d="M18 14h-8"/>
  <path d="M15 18h-5"/>
  <path d="M10 6h8v4h-8V6z"/>
''')

# ─────────────────────────────────────────────
# TRUST / FEATURE ICONS
# ─────────────────────────────────────────────

# 23. Free Shipping / Truck
svg('shipping', '''
  <rect x="1" y="3" width="15" height="13" rx="1"/>
  <path d="M16 8h4l3 3v5h-7V8z"/>
  <circle cx="5.5" cy="18.5" r="2.5"/>
  <circle cx="18.5" cy="18.5" r="2.5"/>
''')

# 24. Secure Payment / Lock
svg('secure', '''
  <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
  <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
  <circle cx="12" cy="16" r="1" fill="#1a1a2e" stroke="none"/>
''')

# 25. Returns / Undo arrow
svg('returns', '''
  <polyline points="1 4 1 10 7 10"/>
  <path d="M3.51 15a9 9 0 1 0 .49-3.51"/>
''')

# 26. Quality / Award / Trophy
svg('quality', '''
  <circle cx="12" cy="8" r="6"/>
  <path d="M15.477 12.89L17 22l-5-3-5 3 1.523-9.11"/>
''')

# 27. Support / Headset
svg('support', '''
  <path d="M3 18v-6a9 9 0 0 1 18 0v6"/>
  <path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"/>
''')

# 28. Warranty / Shield Check
svg('warranty', '''
  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
  <polyline points="9 12 11 14 15 10"/>
''')

# 29. Checkmark / Success
svg('check', '''
  <polyline points="20 6 9 17 4 12"/>
''')

# 30. Package / Box
svg('package', '''
  <path d="M16.5 9.4l-9-5.19"/>
  <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
  <polyline points="3.27 6.96 12 12.01 20.73 6.96"/>
  <line x1="12" y1="22.08" x2="12" y2="12"/>
''')

# 31. Sale / Tag
svg('sale', '''
  <path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/>
  <line x1="7" y1="7" x2="7.01" y2="7"/>
''')

# 32. Compare / Scales
svg('compare', '''
  <line x1="12" y1="3" x2="12" y2="21"/>
  <path d="M3 9l9-7 9 7"/>
  <path d="M5 20h14"/>
  <path d="M5 20a2 2 0 0 1-2-2V9"/>
  <path d="M19 20a2 2 0 0 0 2-2V9"/>
''')

# 33. Filter / Sliders
svg('filter', '''
  <line x1="4" y1="6" x2="20" y2="6"/>
  <line x1="8" y1="12" x2="20" y2="12"/>
  <line x1="12" y1="18" x2="20" y2="18"/>
  <circle cx="4" cy="6" r="2" fill="white" stroke="#1a1a2e"/>
  <circle cx="8" cy="12" r="2" fill="white" stroke="#1a1a2e"/>
  <circle cx="12" cy="18" r="2" fill="white" stroke="#1a1a2e"/>
''')

# 34. Grid View
svg('grid-view', '''
  <rect x="3" y="3" width="7" height="7" rx="1"/>
  <rect x="14" y="3" width="7" height="7" rx="1"/>
  <rect x="3" y="14" width="7" height="7" rx="1"/>
  <rect x="14" y="14" width="7" height="7" rx="1"/>
''')

# 35. List View
svg('list-view', '''
  <rect x="3" y="4" width="18" height="4" rx="1"/>
  <rect x="3" y="10" width="18" height="4" rx="1"/>
  <rect x="3" y="16" width="18" height="4" rx="1"/>
''')

# 36. Zoom In (image gallery)
svg('zoom-in', '''
  <circle cx="11" cy="11" r="8"/>
  <line x1="21" y1="21" x2="16.65" y2="16.65"/>
  <line x1="11" y1="8" x2="11" y2="14"/>
  <line x1="8" y1="11" x2="14" y2="11"/>
''')

# 37. Share
svg('share', '''
  <circle cx="18" cy="5" r="3"/>
  <circle cx="6" cy="12" r="3"/>
  <circle cx="18" cy="19" r="3"/>
  <line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/>
  <line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/>
''')

# 38. Download / PDF
svg('download', '''
  <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
  <polyline points="7 10 12 15 17 10"/>
  <line x1="12" y1="15" x2="12" y2="3"/>
''')

# 39. Notification / Bell
svg('notification', '''
  <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/>
  <path d="M13.73 21a2 2 0 0 1-3.46 0"/>
''')

# 40. Info
svg('info', '''
  <circle cx="12" cy="12" r="10"/>
  <line x1="12" y1="8" x2="12" y2="12"/>
  <line x1="12" y1="16" x2="12.01" y2="16"/>
''')

# 41. Home / Početna
svg('home', '''
  <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
  <polyline points="9 22 9 12 15 12 15 22"/>
''')

# 42. Calculator (tile calculator)
svg('calculator', '''
  <rect x="4" y="2" width="16" height="20" rx="2"/>
  <rect x="8" y="6" width="8" height="4" rx="1"/>
  <line x1="8" y1="14" x2="8" y2="14"/>
  <line x1="12" y1="14" x2="12" y2="14"/>
  <line x1="16" y1="14" x2="16" y2="14"/>
  <line x1="8" y1="18" x2="8" y2="18"/>
  <line x1="12" y1="18" x2="12" y2="18"/>
  <line x1="16" y1="18" x2="16" y2="18"/>
  <circle cx="8" cy="14" r="1" fill="#1a1a2e" stroke="none"/>
  <circle cx="12" cy="14" r="1" fill="#1a1a2e" stroke="none"/>
  <circle cx="16" cy="14" r="1" fill="#1a1a2e" stroke="none"/>
  <circle cx="8" cy="18" r="1" fill="#1a1a2e" stroke="none"/>
  <circle cx="12" cy="18" r="1" fill="#1a1a2e" stroke="none"/>
  <circle cx="16" cy="18" r="1" fill="#1a1a2e" stroke="none"/>
''')

# 43. Ruler / Dimensions
svg('ruler', '''
  <path d="M21.3 8.7l-8.6 8.6a1 1 0 0 1-1.4 0L2.7 8.7a1 1 0 0 1 0-1.4l8.6-8.6a1 1 0 0 1 1.4 0l8.6 8.6a1 1 0 0 1 0 1.4z"/>
  <line x1="7.5" y1="7.5" x2="7.5" y2="11.5"/>
  <line x1="11" y1="4" x2="11" y2="7"/>
  <line x1="14.5" y1="7.5" x2="14.5" y2="11.5"/>
''')

# 44. Palette / Color
svg('palette', '''
  <circle cx="12" cy="12" r="10"/>
  <circle cx="8.5" cy="9" r="1.5" fill="#1a1a2e" stroke="none"/>
  <circle cx="15.5" cy="9" r="1.5" fill="#1a1a2e" stroke="none"/>
  <circle cx="12" cy="15" r="1.5" fill="#1a1a2e" stroke="none"/>
  <path d="M8 15s1.5 2 4 2 4-2 4-2"/>
''')

# 45. Star Rating (half filled)
svg('star-rating', '''
  <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" fill="#c8a96e" stroke="#c8a96e"/>
''')

print("\nAll icons generated successfully!")
print(f"Total icons: 45")
