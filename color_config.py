from imgui_bundle import imgui
channel_colors = [
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
    imgui.ImVec4(0.0, 0.0, 0.0, 1.0),  # Black
    imgui.ImVec4(0.5, 0.5, 0.5, 1.0),  # Gray
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
    imgui.ImVec4(0.25, 0.75, 0.75, 1.0),  # Light Teal
    imgui.ImVec4(0.0, 0.5, 0.5, 1.0),  # Dark Teal
    imgui.ImVec4(0.75, 0.25, 0.75, 1.0),  # Light Plum
    imgui.ImVec4(0.5, 0.25, 0.5, 1.0),  # Dark Plum
    imgui.ImVec4(0.25, 0.75, 0.25, 1.0),  # Light Forest
    imgui.ImVec4(0.0, 0.5, 0.25, 1.0),  # Dark Forest
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
alt_bg1_color = imgui.ImVec4(0.2, 0.2, 0.2, 1.0)
alt_bg2_color = imgui.ImVec4(0.15, 0.15, 0.15, 1.0)
