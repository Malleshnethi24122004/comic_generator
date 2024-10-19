import os
import json
from generate_panels import generate_panels
from stability_ai import text_to_image
from add_text import add_text_to_panel
from create_strip import create_strip

# Define the scenario
SCENARIO = """
Characters: Peter is a tall guy with blond hair. Steven is a small guy with black hair.
Peter and Steven walk together in new york when aliens attack the city. They are afraid and try to run for their lives. The army arrives and saves them.
"""
STYLE = "american comic, colored"

# Ensure 'output' directory exists
output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print(f"Generate panels with style '{STYLE}' for this scenario: \n {SCENARIO}")

# Generate panel descriptions
panels = generate_panels(SCENARIO)

# Save the generated panel descriptions to a file
with open(f'{output_dir}/panels.json', 'w') as outfile:
    json.dump(panels, outfile)

# Generate images from the descriptions and add text
panel_images = []
for panel in panels:
    panel_prompt = panel["description"] + ", cartoon box, " + STYLE
    print(f"Generate panel {panel['number']} with prompt: {panel_prompt}")
    panel_image = text_to_image(panel_prompt)
    panel_image_with_text = add_text_to_panel(panel["text"], panel_image)
    panel_image_with_text.save(f"{output_dir}/panel-{panel['number']}.png")
    panel_images.append(panel_image_with_text)

# Combine the individual panels into a comic strip
create_strip(panel_images).save(f"{output_dir}/strip.png")
