from imgui_bundle import imgui
channel_colors = [
    imgui.ImVec4(1.0, 1.0, 0.0, 1.0),       # Bright Yellow
    imgui.ImVec4(0.0, 1.0, 0.0, 1.0),       # Bright Green
    imgui.ImVec4(1.0, 0.0, 0.0, 1.0),       # Bright Red
    imgui.ImVec4(0.0, 1.0, 1.0, 1.0),       # Bright Cyan
    imgui.ImVec4(1.0, 0.0, 1.0, 1.0),       # Bright Magenta
    imgui.ImVec4(0.3, 0.7, 1.0, 1.0),       # Bright Blue
    imgui.ImVec4(1.0, 0.6, 0.0, 1.0),       # Bright Orange
    imgui.ImVec4(0.5, 1.0, 0.0, 1.0),       # Lime Green
    imgui.ImVec4(0.0, 0.5, 1.0, 1.0),       # Azure Blue
    imgui.ImVec4(1.0, 0.4, 0.7, 1.0),       # Hot Pink
    imgui.ImVec4(0.9, 0.9, 0.5, 1.0),       # Light Yellow
    imgui.ImVec4(0.0, 0.8, 0.8, 1.0),       # Turquoise
    imgui.ImVec4(0.8, 0.0, 0.8, 1.0),       # Violet
    imgui.ImVec4(0.6, 1.0, 0.6, 1.0),       # Mint Green
    imgui.ImVec4(1.0, 0.8, 0.8, 1.0),       # Light Pink
    imgui.ImVec4(0.8, 0.8, 1.0, 1.0),       # Lavender
    imgui.ImVec4(1.0, 0.8, 0.0, 1.0),       # Gold
    imgui.ImVec4(0.8, 1.0, 0.0, 1.0),       # Chartreuse
    imgui.ImVec4(0.0, 0.8, 0.4, 1.0),       # Spring Green
    imgui.ImVec4(0.4, 0.0, 0.8, 1.0),       # Indigo
    imgui.ImVec4(1.0, 0.4, 0.0, 1.0),       # Vermilion
    imgui.ImVec4(0.8, 0.4, 1.0, 1.0),       # Orchid
    imgui.ImVec4(0.4, 1.0, 0.8, 1.0),       # Aquamarine
    imgui.ImVec4(1.0, 0.0, 0.4, 1.0),       # Crimson
    imgui.ImVec4(0.6, 0.8, 0.2, 1.0),       # Olive Green
    imgui.ImVec4(0.2, 0.6, 1.0, 1.0),       # Cornflower Blue
    imgui.ImVec4(1.0, 0.6, 0.4, 1.0),       # Coral
    imgui.ImVec4(0.6, 0.4, 1.0, 1.0),       # Periwinkle
    imgui.ImVec4(0.4, 1.0, 0.4, 1.0),       # Bright Lime
    imgui.ImVec4(1.0, 0.3, 0.6, 1.0),       # Rose
    imgui.ImVec4(0.6, 1.0, 1.0, 1.0),       # Light Cyan
    imgui.ImVec4(1.0, 1.0, 0.6, 1.0),       # Cream
    imgui.ImVec4(0.0, 1.0, 0.5, 1.0),       # Sea Green
    imgui.ImVec4(0.9, 0.5, 0.0, 1.0),       # Amber
]
cursor_colors = [
    imgui.ImVec4(1.0, 1.0, 0.0, 1.0),  # Yellow
    imgui.ImVec4(0.0, 1.0, 0.0, 1.0),  # Green
    imgui.ImVec4(1.0, 0.0, 0.0, 1.0),  # Red
    imgui.ImVec4(0.0, 1.0, 1.0, 1.0),  # Cyan
    imgui.ImVec4(1.0, 0.0, 1.0, 1.0),  # Magenta
    imgui.ImVec4(0.0, 0.5, 1.0, 1.0),  # Blue
    imgui.ImVec4(1.0, 0.5, 0.0, 1.0),  # Orange
    imgui.ImVec4(0.5, 1.0, 0.5, 1.0),  # Light Green
    imgui.ImVec4(0.5, 0.5, 1.0, 1.0),  # Light Blue
    imgui.ImVec4(1.0, 0.5, 0.5, 1.0),  # Light Magenta
    imgui.ImVec4(0.5, 1.0, 0.0, 1.0),  # Light Yellow
    imgui.ImVec4(0.0, 0.5, 0.5, 1.0),  # Dark Cyan
    imgui.ImVec4(0.5, 0.0, 0.5, 1.0),  # Dark Magenta
    imgui.ImVec4(0.0, 0.5, 0.0, 1.0),  # Dark Green
    imgui.ImVec4(0.5, 0.0, 0.0, 1.0),  # Dark Red
    imgui.ImVec4(0.0, 0.0, 0.5, 1.0),  # Dark Blue
    imgui.ImVec4(0.75, 0.75, 0.75, 1.0),  # Light Gray
    imgui.ImVec4(0.25, 0.25, 0.25, 1.0),  # Dark Gray
    imgui.ImVec4(0.75, 0.5, 0.5, 1.0),  # Light Brown
    imgui.ImVec4(0.5, 0.25, 0.25, 1.0),  # Dark Brown
    imgui.ImVec4(0.5, 0.75, 0.5, 1.0),  # Light Olive
    imgui.ImVec4(0.25, 0.5, 0.25, 1.0),  # Dark Olive
    imgui.ImVec4(0.5, 0.5, 0.75, 1.0),  # Light Slate
    imgui.ImVec4(0.25, 0.25, 0.5, 1.0),  # Dark Slate
    imgui.ImVec4(0.75, 0.75, 0.25, 1.0),  # Light Tan
    imgui.ImVec4(0.5, 0.5, 0.25, 1.0),  # Dark Tan
]
separator_color = imgui.ImVec4(0.3, 0.3, 0.3, 1.0)
label_bg_color = imgui.ImVec4(0.2, 0.2, 0.2, 0.5)
bubble_bg_color = imgui.ImVec4(1.0, 1.0, 1.0, 1.0)
bubble_text_color = imgui.ImVec4(0.0, 0.0, 0.0, 1.0)
rule_bg_color = imgui.ImVec4(0.15, 0.15, 0.15, 1.0)
rule_minor_tick_color = imgui.ImVec4(0.5, 0.5, 0.5, 1.0)
rule_major_tick_color = imgui.ImVec4(0.8, 0.8, 0.8, 1.0)
rule_label_color = imgui.ImVec4(1.0, 1.0, 1.0, 1.0)
rule_bg_color = imgui.ImVec4(0.15, 0.15, 0.15, 1.0)
grid_color = imgui.ImVec4(0.2, 0.2, 0.2, 1.0)
minor_grid_color = imgui.ImVec4(0.15, 0.15, 0.15, 1.0)
zoom_text_color = imgui.ImVec4(1, 1, 1, 1.0)
frame_text_color = imgui.ImVec4(0, 0, 0, 1.0)
frame_bg_color = imgui.ImVec4(1, 1, 1, 1.0)
alt_bg1_color = imgui.ImVec4(0.025, 0.025, 0.025, 1.0)
alt_bg2_color = imgui.ImVec4(0.05, 0.05, 0.05, 1.0)
highlight_color=imgui.ImVec4(1, 1, 0, 0.5)