# persona_image.py
from PIL import Image, ImageDraw, ImageFont
import textwrap

def generate_persona_image(persona_text, output_path="persona_image.png"):
    width = 1280
    margin = 40
    col_gap = 40
    col_width = (width - 3 * margin) // 2
    background_color = (255, 255, 255)
    text_color = (40, 40, 40)
    header_color = (230, 120, 20)
    font_path = "/Library/Fonts/Arial.ttf"  # Change if needed

    title_font = ImageFont.truetype(font_path, 48)
    header_font = ImageFont.truetype(font_path, 32)
    text_font = ImageFont.truetype(font_path, 24)

    expected_sections = [
        "Name", "Age", "Occupation", "Status", "Location", "Tier", "Archetype",
        "Traits", "Motivations", "Personality", "Behaviour & Habits", "Frustrations", "Goals & Needs"
    ]

    # Parse persona text into sections
    lines = persona_text.splitlines()
    sections = {}
    current_section = None
    for line in lines:
        clean_line = line.strip().replace("**", "")
        if not clean_line:
            continue
        is_section = False
        for sec in expected_sections:
            if clean_line.lower().startswith(sec.lower()):
                current_section = sec
                sections[current_section] = []
                if ":" in clean_line:
                    after_colon = clean_line.split(":", 1)[1].strip()
                    if after_colon:
                        sections[current_section].append(after_colon)
                is_section = True
                break
        if not is_section and current_section:
            sections[current_section].append(clean_line)

    # Prepare all lines to draw, split into two columns
    draw_lines = []
    name = ""
    if "Name" in sections and sections["Name"]:
        name = sections["Name"][0]
        draw_lines.append(("title", name))
    for section in expected_sections:
        if section == "Name" or section not in sections:
            continue
        draw_lines.append(("header", section + ":"))
        for item in sections[section]:
            if item.startswith("-"):
                item = item[1:].strip()
                for wrapped in textwrap.wrap("• " + item, width=45):
                    draw_lines.append(("bullet", wrapped))
            else:
                for wrapped in textwrap.wrap(item, width=50):
                    draw_lines.append(("text", wrapped))
        draw_lines.append(("spacer", ""))

    # Calculate how many lines are needed
    line_height = 34  # Approximate for text_font
    total_lines = len(draw_lines)
    min_height = 720
    # Two columns: lines per col = ceil(total_lines / 2)
    lines_per_col = (total_lines + 1) // 2
    needed_height = max(min_height, lines_per_col * line_height + 2 * margin)

    # Create image with dynamic height
    img = Image.new("RGB", (width, needed_height), color=background_color)
    draw = ImageDraw.Draw(img)

    # Split lines into two columns
    col1_lines = draw_lines[:lines_per_col]
    col2_lines = draw_lines[lines_per_col:]

    # Draw first column
    y = margin
    x = margin
    for kind, text in col1_lines:
        if kind == "title":
            draw.text((x, y), text, font=title_font, fill=header_color)
            y += 60
        elif kind == "header":
            draw.text((x, y), text, font=header_font, fill=header_color)
            y += 38
        elif kind == "bullet":
            draw.text((x + 20, y), text, font=text_font, fill=text_color)
            y += 30
        elif kind == "text":
            draw.text((x + 10, y), text, font=text_font, fill=text_color)
            y += 30
        elif kind == "spacer":
            y += 12

    # Draw second column
    y = margin
    x = margin * 2 + col_width
    for kind, text in col2_lines:
        if kind == "title":
            draw.text((x, y), text, font=title_font, fill=header_color)
            y += 60
        elif kind == "header":
            draw.text((x, y), text, font=header_font, fill=header_color)
            y += 38
        elif kind == "bullet":
            draw.text((x + 20, y), text, font=text_font, fill=text_color)
            y += 30
        elif kind == "text":
            draw.text((x + 10, y), text, font=text_font, fill=text_color)
            y += 30
        elif kind == "spacer":
            y += 12

    img.save(output_path)
    return output_path