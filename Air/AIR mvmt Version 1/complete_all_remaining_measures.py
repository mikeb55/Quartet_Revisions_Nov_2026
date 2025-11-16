#!/usr/bin/env python3
"""
Complete all remaining measures for Violin II, Viola, and Cello
Based on Air-Mov4-COMPLETE-COMPOSITION.md
"""

import xml.etree.ElementTree as ET
import re

# Read the MusicXML file
xml_file = "Air-Mov4-ExcellenceEdition.musicxml"
tree = ET.parse(xml_file)
root = tree.getroot()

# Define triad mappings per measure ranges for Violin II
violin2_triads = {
    (9, 12): ("F#", 4, "A", 4, "C#", 5),  # F# minor
    (13, 16): ("D", 4, "F#", 4, "A", 4),  # D major
    (17, 20): ("E", 4, "G", 4, "B", 4),  # E minor
    (21, 24): ("G", 4, "B", 4, "D", 5),  # G major
    (25, 28): ("C", 4, "E", 4, "G", 4),  # C major
    (29, 32): ("F#", 4, "A", 4, "C#", 5),  # F# minor
    (33, 36): ("B", 3, "D", 4, "F#", 4),  # B minor
    (37, 40): ("G", 4, "B", 4, "D", 5),  # G major
    (41, 44): ("B", 3, "D", 4, "F#", 4),  # B minor
    (45, 48): ("C", 4, "E", 4, "G", 4),  # C major
    (49, 52): ("F#", 4, "A", 4, "C#", 5),  # F# minor
    (53, 56): ("D", 4, "F#", 4, "A", 4),  # D major
    (57, 60): ("E", 4, "G", 4, "B", 4),  # E minor
    (61, 64): ("G", 4, "B", 4, "D", 5),  # G major
    (65, 68): ("B", 3, "D", 4, "F#", 4),  # B minor
    (69, 72): ("C", 4, "E", 4, "G", 4),  # C major
    (73, 76): ("F#", 4, "A", 4, "C#", 5),  # F# minor
    (77, 80): ("B", 3, "D", 4, "F#", 4),  # B minor
    (81, 84): ("B", 3, "D", 4, "F#", 4),  # B minor
    (85, 88): ("C", 4, "E", 4, "G", 4),  # C major
}

# Define triad mappings for Viola
viola_triads = {
    (9, 12): ("F#", 3, "A", 3, "C#", 4),  # F# minor
    (13, 16): ("D", 3, "F#", 3, "A", 3),  # D major
    (17, 20): ("E", 3, "G", 3, "B", 3),  # E minor
    (21, 24): ("G", 3, "B", 3, "D", 4),  # G major
    (25, 28): ("C", 3, "E", 3, "G", 3),  # C major
    (29, 32): ("F#", 3, "A", 3, "C#", 4),  # F# minor
    (33, 36): ("B", 3, "D", 4, "F#", 4),  # B minor
    (37, 40): ("G", 3, "B", 3, "D", 4),  # G major
    (41, 44): ("B", 3, "D", 4, "F#", 4),  # B minor
    (45, 48): ("C", 3, "E", 3, "G", 3),  # C major
    (49, 52): ("F#", 3, "A", 3, "C#", 4),  # F# minor
    (53, 56): ("D", 3, "F#", 3, "A", 3),  # D major
    (57, 60): ("E", 3, "G", 3, "B", 3),  # E minor
    (61, 64): ("G", 3, "B", 3, "D", 4),  # G major
    (65, 68): ("B", 3, "D", 4, "F#", 4),  # B minor
    (69, 72): ("C", 3, "E", 3, "G", 3),  # C major
    (73, 76): ("F#", 3, "A", 3, "C#", 4),  # F# minor
    (77, 80): ("B", 3, "D", 4, "F#", 4),  # B minor
    (81, 84): ("B", 3, "D", 4, "F#", 4),  # B minor
    (85, 88): ("C", 3, "E", 3, "G", 3),  # C major
}

# Define cello patterns (quarter notes, pizzicato)
cello_patterns = {
    (9, 12): [("D", 3), ("F#", 3), ("A", 3), ("D", 3)],  # D major
    (13, 16): [("B", 2), ("D", 3), ("F", 3), ("B", 2)],  # B diminished
    (17, 20): [("C", 3), ("E", 3), ("G", 3), ("C", 3)],  # C major
    (21, 24): [("E", 3), ("F#", 3), ("G", 3), ("A", 3)],  # E minor (tenor register)
    (25, 28): [("A", 2), ("C", 3), ("E", 3), ("A", 3)],  # A minor
    (29, 32): [("D", 3), ("F#", 3), ("A", 3), ("D", 3)],  # D major
    (33, 36): [("G", 2), ("B", 2), ("D", 3), ("G", 3)],  # G major
    (37, 40): [("E", 3), ("G", 3), ("B", 3), ("E", 3)],  # E minor
    (41, 44): [("G", 2), ("B", 2), ("D", 3), ("G", 3)],  # G major
    (45, 48): [("A", 2), ("C", 3), ("E", 3), ("A", 3)],  # A minor
    (49, 52): [("D", 3), ("F#", 3), ("A", 3), ("D", 3)],  # D major
    (53, 56): [("B", 2), ("D", 3), ("F", 3), ("B", 2)],  # B diminished
    (57, 60): [("C", 3), ("E", 3), ("G", 3), ("C", 3)],  # C major
    (61, 64): [("E", 3), ("G", 3), ("B", 3), ("E", 3)],  # E minor
    (65, 68): [("G", 2), ("B", 2), ("D", 3), ("G", 3)],  # G major
    (69, 72): [("A", 2), ("C", 3), ("E", 3), ("A", 3)],  # A minor
    (73, 76): [("D", 3), ("F#", 3), ("A", 3), ("D", 3)],  # D major
    (77, 80): [("G", 2), ("B", 2), ("D", 3), ("G", 3)],  # G major
    (81, 84): [("G", 2), ("B", 2), ("D", 3), ("G", 3)],  # G major
    (85, 88): [("A", 2), ("C", 3), ("E", 3), ("A", 3)],  # A minor
}

print("Script created. Due to complexity, completing remaining measures directly in XML...")
print("This script outlines the pattern. Implementing directly in XML for efficiency.")

