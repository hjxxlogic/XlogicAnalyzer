# XLogic Analyzer SDK User Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Main Interface](#main-interface)
4. [Working with Channels](#working-with-channels)
5. [Navigation and Zooming](#navigation-and-zooming)
6. [Working with Cursors](#working-with-cursors)
7. [Analyzers and Protocols](#analyzers-and-protocols)
8. [Channel Groups](#channel-groups)
9. [Waveform Analysis](#waveform-analysis)
10. [Keyboard Shortcuts](#keyboard-shortcuts)

## Introduction

XLogic Analyzer SDK is a powerful logic analyzer software designed for analyzing digital signals and protocols. It provides a comprehensive set of tools for visualizing, navigating, and analyzing waveform data from various sources. This user guide will help you understand the features and functionality of the XLogic Analyzer SDK.

## Getting Started

### Loading a File

1. Launch the XLogic Analyzer application.
2. Click on the folder icon (📂) in the top toolbar to open a file.
3. Select a supported file format (.sr, .dsl, .atkdl) from the file dialog.
4. The waveform data will be loaded and displayed in the main window.

## Main Interface

The XLogic Analyzer interface consists of several key components:

- **Top Toolbar**: Contains buttons for file operations and other actions.
- **Channel Panel**: Located on the left side, displays the list of channels and their properties.
- **Waveform Area**: The main display area showing the signal waveforms.
- **Time Ruler**: Located at the top of the waveform area, shows time measurements.
- **Status Bar**: Displays information about the current state of the analyzer.

## Working with Channels

### Channel Display

- Each channel is displayed with its name and signal waveform.
- Channels are color-coded for easy identification.
- The height of each channel can be adjusted by dragging the separator between channels.

### Channel Operations

- **Selecting a Channel**: Click on a channel name to select it.
- **Reordering Channels**: Drag and drop a channel to change its position in the list.
- **Hiding/Showing Channels**: Right-click on a channel and select the appropriate option from the context menu.

## Navigation and Zooming

### Zooming

- **Mouse Wheel**: Scroll up to zoom in, scroll down to zoom out.
- **Keyboard**: Press Up Arrow to zoom in, Down Arrow to zoom out.
- **Double-Click**: Double-click on a point to zoom in centered on that point.

### Panning

- **Mouse Drag**: Click and drag in the waveform area to pan horizontally.
- **Keyboard**: Press Left Arrow to pan left, Right Arrow to pan right.
- **Edge Navigation**: When the mouse is near the left or right edge of a channel, arrow buttons (<<, >>) appear to navigate to the previous or next edge of the signal.

## Working with Cursors

Cursors are vertical markers that help measure time and analyze signals at specific points.

### Adding Cursors

- **Right-Click**: Right-click in the waveform area to add a cursor at that position.
- **Keyboard**: Press a letter key (A-Z) while the mouse is over the waveform area to add a cursor at that position.

### Manipulating Cursors

- **Moving Cursors**: Click and drag a cursor to move it.
- **Cursor Context Menu**: Right-click on a cursor to open a context menu with options:
  - Delete the cursor
  - View time and sample information
  - Jump to other cursors

### Cursor Measurements

- The time and sample position of each cursor is displayed when selected.
- Time differences between cursors can be viewed for precise measurements.

## Analyzers and Protocols

XLogic Analyzer SDK supports protocol analysis through analyzer plugins.

### Using Protocol Analyzers

1. Click the "P" button in the right toolbar to open the Analyzers window.
2. Select a protocol analyzer from the list.
3. Configure the analyzer settings, including channel assignments.
4. Apply the settings to start the analysis.

### Analyzer Results

- Protocol decode results are displayed as bubbles above the relevant channels.
- Frames and packets are highlighted in the waveform area.
- Detailed protocol information can be viewed by clicking on decode bubbles.

## Channel Groups

Channel groups help organize related channels together for better visualization and analysis.

### Creating Groups

1. Select multiple channels you want to group.
2. Right-click and select "Create Group" from the context menu.
3. Enter a name for the group.

### Managing Groups

- **Expanding/Collapsing**: Click the arrow next to the group name to expand or collapse the group.
- **Adding Channels**: Drag a channel onto a group header to add it to the group.
- **Removing Channels**: Drag a channel out of a group or right-click and select "Remove from Group".
- **Deleting Groups**: Click the "..." button next to the group name and select "Delete Group".

## Waveform Analysis

### Signal Measurements

- Hover over a signal to see its value at that point.
- Use cursors to measure time intervals between events.
- The mouse info panel shows detailed information about the signal under the cursor.

### Frame Analysis

- For protocol analyzers, frames are highlighted in the waveform.
- Navigate between frames using the edge navigation buttons.
- View detailed frame information by right-clicking on a frame.

## Keyboard Shortcuts

| Key | Function |
|-----|----------|
| A-Z | Add or jump to cursor |
| Up Arrow | Zoom in |
| Down Arrow | Zoom out |
| Left Arrow | Pan left |
| Right Arrow | Pan right |
| Mouse Wheel | Zoom in/out |
| Left Mouse Button | Select, drag |
| Right Mouse Button | Context menu, add cursor |

## Troubleshooting

### Common Issues

- **File Loading Problems**: Ensure the file format is supported (.sr, .dsl, .atkdl).
- **Performance Issues**: For large captures, try reducing the visible time window.
- **Protocol Decode Errors**: Check channel assignments and analyzer settings.

### Getting Help

For additional assistance, please contact support or refer to the online documentation.
