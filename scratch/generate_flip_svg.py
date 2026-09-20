import os

text = "Available for end-to-end projects & contract work"
font_size = 17
# Let's use monospace "Fira Code", monospace or sans-serif where each char has fixed/predictable spacing
# With monospace, character spacing is uniform (approx 10.2px at 17px)
char_w = 10.4
total_w = len(text) * char_w
svg_w = 680
start_x = (svg_w - total_w) / 2

svg_lines = []
svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} 48" width="{svg_w}" height="48">')
svg_lines.append("""  <defs>
    <style>
      .char-flip {
        font-family: 'Fira Code', -apple-system, BlinkMacSystemFont, "Segoe UI", monospace;
        font-size: 17px;
        font-weight: 600;
        fill: #38bdf8;
        transform-box: fill-box;
        transform-origin: 50% 50%;
        display: inline-block;
        animation: flipVert 4.5s ease-in-out infinite;
      }
      .sparkle {
        font-size: 18px;
        animation: pulseTwinkle 3s ease-in-out infinite;
      }
      @keyframes flipVert {
        0%, 15% {
          transform: rotateX(0deg);
        }
        8% {
          transform: rotateX(360deg);
        }
        100% {
          transform: rotateX(360deg);
        }
      }
      @keyframes pulseTwinkle {
        0%, 100% { opacity: 0.8; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.15); filter: drop-shadow(0 0 3px #fbbf24); }
      }
    </style>
  </defs>
""")

# Left Sparkle
sparkle_left_x = start_x - 30
svg_lines.append(f'  <text class="sparkle" x="{sparkle_left_x:.1f}" y="29" text-anchor="middle">✨</text>')

# Each character with its own x coordinate and staggered delay
for i, ch in enumerate(text):
    if ch == ' ':
        continue
    x = start_x + (i * char_w) + (char_w / 2)
    # Stagger delay across the letters (total wave takes ~1.2s, then rest stays idle for 3.3s)
    delay = i * 0.035
    esc_ch = '&amp;' if ch == '&' else ch
    svg_lines.append(f'  <text class="char-flip" x="{x:.1f}" y="29" text-anchor="middle" style="animation-delay: {delay:.3f}s;">{esc_ch}</text>')

# Right Sparkle
sparkle_right_x = start_x + total_w + 30
svg_lines.append(f'  <text class="sparkle" x="{sparkle_right_x:.1f}" y="29" text-anchor="middle" style="animation-delay: 1.5s;">✨</text>')
svg_lines.append('</svg>')

os.makedirs('assets', exist_ok=True)
with open('assets/option2_flip.svg', 'w', encoding='utf-8') as f:
    f.write('\n'.join(svg_lines))

print('Successfully generated option2_flip.svg')
