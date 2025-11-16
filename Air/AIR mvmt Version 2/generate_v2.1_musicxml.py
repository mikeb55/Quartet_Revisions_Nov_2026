#!/usr/bin/env python3
"""
Generate V2.1 Air Movement MusicXML
- Preserves measures 1-8 exactly (core motif)
- Implements melodic rotation in measures 9-41
- Keeps V2 revisions for measures 41-90
- Rotates melodic interest among all instruments
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom
import sys
import os

def add_direction(measure, words_text, staff="1", voice="1"):
    """Add a direction with words to a measure."""
    direction = ET.SubElement(measure, "direction")
    direction_type = ET.SubElement(direction, "direction-type")
    words = ET.SubElement(direction_type, "words")
    words.text = words_text
    words.set("font-family", "Palatino")
    words.set("font-style", "italic")
    words.set("font-size", "9.7485")
    ET.SubElement(direction, "voice").text = voice
    ET.SubElement(direction, "staff").text = staff
    return direction

def add_dynamic(measure, dynamic_text, staff="1", voice="1"):
    """Add a dynamic marking to a measure."""
    direction = ET.SubElement(measure, "direction")
    direction_type = ET.SubElement(direction, "direction-type")
    dynamics = ET.SubElement(direction_type, "dynamics")
    dynamic_elem = ET.SubElement(dynamics, dynamic_text)
    ET.SubElement(direction, "voice").text = voice
    ET.SubElement(direction, "staff").text = staff
    return direction

def create_note(step, octave, duration=256, note_type="quarter", is_rest=False, 
                is_chord=False, stem="up", slur_start=False, slur_stop=False,
                tenuto=False, pizzicato=False, harmonics=False, accent=False,
                instrument_id="P1-I1", voice="1", staff="1", alter=None, beam=None):
    """Create a note element."""
    note = ET.Element("note")
    
    if is_rest:
        ET.SubElement(note, "rest")
    else:
        pitch = ET.SubElement(note, "pitch")
        ET.SubElement(pitch, "step").text = step
        if alter is not None:
            ET.SubElement(pitch, "alter").text = str(alter)
        ET.SubElement(pitch, "octave").text = str(octave)
    
    ET.SubElement(note, "duration").text = str(duration)
    ET.SubElement(note, "instrument", id=instrument_id)
    ET.SubElement(note, "voice").text = voice
    ET.SubElement(note, "type").text = note_type
    
    if not is_rest:
        stem_elem = ET.SubElement(note, "stem")
        stem_elem.text = stem
    
    ET.SubElement(note, "staff").text = staff
    
    if beam:
        beam_elem = ET.SubElement(note, "beam")
        beam_elem.set("number", "1")
        beam_elem.text = beam
    
    if slur_start or slur_stop:
        notations = ET.SubElement(note, "notations")
        slur = ET.SubElement(notations, "slur")
        slur.set("type", "start" if slur_start else "stop")
        slur.set("orientation", "over")
        slur.set("color", "#000000")
    
    if tenuto or pizzicato or accent:
        if not slur_start and not slur_stop:
            notations = ET.SubElement(note, "notations")
        else:
            notations = note.find("notations")
        if notations is None:
            notations = ET.SubElement(note, "notations")
        
        if tenuto or accent:
            articulations = ET.SubElement(notations, "articulations")
            if tenuto:
                ET.SubElement(articulations, "tenuto")
            if accent:
                ET.SubElement(articulations, "accent")
        
        if pizzicato:
            technical = ET.SubElement(notations, "technical")
            ET.SubElement(technical, "pluck")
    
    if harmonics:
        if not slur_start and not slur_stop:
            notations = ET.SubElement(note, "notations")
        else:
            notations = note.find("notations")
        if notations is None:
            notations = ET.SubElement(note, "notations")
        technical = ET.SubElement(notations, "technical")
        ET.SubElement(technical, "harmonic")
    
    return note

def clear_measure_notes(measure):
    """Remove all notes from a measure, keeping directions and attributes."""
    notes = measure.findall("note")
    for note in notes:
        measure.remove(note)

def implement_measures_9_16(measure, measure_num, part_id):
    """Implement measures 9-16: Violin II Countermelody Added"""
    if part_id == "P2":  # Violin II - Add independent countermelody
        # Add countermelody - flowing eighth notes, baroque-inflected
        # Pattern: Independent line, not doubling Violin I
        add_dynamic(measure, "mp", "1", "1")
        # Keep existing notes but ensure they're independent countermelody
        # If measure is empty or has rests, add countermelody
        notes = measure.findall("note")
        if len(notes) == 0 or all(n.find("rest") is not None for n in notes):
            clear_measure_notes(measure)
            # Add flowing countermelody: G4-B4-D5-G4-F#4-D4-B4-G4
            if measure_num == 9:
                measure.append(create_note("G", 4, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P2-I1", "1", "1", None, "begin"))
                measure.append(create_note("B", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P2-I1", "1", "1", None, "continue"))
                measure.append(create_note("D", 5, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P2-I1", "1", "1", None, "continue"))
                measure.append(create_note("G", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P2-I1", "1", "1", None, "continue"))
                measure.append(create_note("F", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P2-I1", "1", "1", None, "continue", 1))
                measure.append(create_note("D", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P2-I1", "1", "1", None, "continue"))
                measure.append(create_note("B", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P2-I1", "1", "1", None, "continue"))
                measure.append(create_note("G", 4, 128, "eighth", False, False, "down", False, True, False, False, False, False, "P2-I1", "1", "1", None, "end"))
            else:
                # Similar patterns for other measures
                measure.append(create_note("G", 4, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P2-I1", "1", "1", None, "begin"))
                measure.append(create_note("B", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P2-I1", "1", "1", None, "continue"))
                measure.append(create_note("D", 5, 256, "quarter", False, False, "down", False, False, False, False, False, False, "P2-I1", "1", "1"))
                measure.append(create_note("G", 4, 256, "quarter", False, False, "down", False, True, False, False, False, False, "P2-I1", "1", "1"))
    
    elif part_id == "P1":  # Violin I - Continue melody but lighter
        add_dynamic(measure, "mp", "1", "1")
    
    elif part_id == "P3":  # Viola - Light melodic material
        add_dynamic(measure, "mp", "1", "1")
    
    elif part_id == "P4":  # Cello - Continue bass foundation
        add_dynamic(measure, "mp", "1", "1")

def implement_measures_17_24(measure, measure_num, part_id):
    """Implement measures 17-24: Violin II Takes Primary Melody"""
    if part_id == "P2":  # Violin II - Primary melody
        clear_measure_notes(measure)
        add_dynamic(measure, "mp", "1", "1")
        add_direction(measure, "espressivo", "1", "1")
        # Motif 1 variation in Violin II register
        if measure_num == 17:
            measure.append(create_note("E", 4, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P2-I1", "1", "1", None, "begin"))
            measure.append(create_note("G", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P2-I1", "1", "1", None, "continue"))
            measure.append(create_note("B", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P2-I1", "1", "1", None, "continue"))
            measure.append(create_note("E", 5, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P2-I1", "1", "1", None, "continue"))
            measure.append(create_note("D", 5, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P2-I1", "1", "1", None, "continue"))
            measure.append(create_note("B", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P2-I1", "1", "1", None, "continue"))
            measure.append(create_note("G", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P2-I1", "1", "1", None, "continue"))
            measure.append(create_note("E", 4, 128, "eighth", False, False, "down", False, True, False, False, False, False, "P2-I1", "1", "1", None, "end"))
        else:
            measure.append(create_note("E", 4, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P2-I1", "1", "1", None, "begin"))
            measure.append(create_note("G", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P2-I1", "1", "1", None, "continue"))
            measure.append(create_note("B", 4, 256, "quarter", False, False, "down", False, False, False, False, False, False, "P2-I1", "1", "1"))
            measure.append(create_note("E", 5, 256, "quarter", False, False, "down", False, True, False, False, False, False, "P2-I1", "1", "1"))
    
    elif part_id == "P1":  # Violin I - Countermelody or supporting
        add_dynamic(measure, "mp", "1", "1")
        add_direction(measure, "sotto voce", "1", "1")
    
    elif part_id == "P3":  # Viola - Light counterpoint
        add_dynamic(measure, "mp", "1", "1")
    
    elif part_id == "P4":  # Cello - Bass foundation
        add_dynamic(measure, "mp", "1", "1")

def implement_measures_25_32(measure, measure_num, part_id):
    """Implement measures 25-32: Viola Featured Melodic Passage"""
    if part_id == "P3":  # Viola - Featured melodic passage
        clear_measure_notes(measure)
        add_direction(measure, "arco", "1", "1")
        add_direction(measure, "espressivo", "1", "1")
        add_direction(measure, "sul C", "1", "1")
        add_dynamic(measure, "mp", "1", "1")
        # C-string melody: C3-E3-G3-C4-B3-G3-E3-C3
        if measure_num == 25:
            measure.append(create_note("C", 3, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P3-I1", "1", "1", None, "begin"))
            measure.append(create_note("E", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P3-I1", "1", "1", None, "continue"))
            measure.append(create_note("G", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P3-I1", "1", "1", None, "continue"))
            measure.append(create_note("C", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P3-I1", "1", "1", None, "continue"))
            measure.append(create_note("B", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P3-I1", "1", "1", None, "continue"))
            measure.append(create_note("G", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P3-I1", "1", "1", None, "continue"))
            measure.append(create_note("E", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P3-I1", "1", "1", None, "continue"))
            measure.append(create_note("C", 3, 128, "eighth", False, False, "down", False, True, False, False, False, False, "P3-I1", "1", "1", None, "end"))
        else:
            measure.append(create_note("C", 3, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P3-I1", "1", "1", None, "begin"))
            measure.append(create_note("E", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P3-I1", "1", "1", None, "continue"))
            measure.append(create_note("G", 3, 256, "quarter", False, False, "down", False, False, False, False, False, False, "P3-I1", "1", "1"))
            measure.append(create_note("C", 4, 256, "quarter", False, False, "down", False, True, False, False, False, False, "P3-I1", "1", "1"))
    
    elif part_id == "P1":  # Violin I - Supporting role
        add_dynamic(measure, "mp", "1", "1")
        add_direction(measure, "sotto voce", "1", "1")
    
    elif part_id == "P2":  # Violin II - Supporting role
        add_dynamic(measure, "mp", "1", "1")
    
    elif part_id == "P4":  # Cello - Melodic bass or countermelody
        add_dynamic(measure, "mp", "1", "1")

def implement_measures_33_40(measure, measure_num, part_id):
    """Implement measures 33-40: Cello Featured Melodic Passage"""
    if part_id == "P4":  # Cello - Featured melodic passage in tenor register
        clear_measure_notes(measure)
        add_direction(measure, "arco", "1", "1")
        add_direction(measure, "espressivo", "1", "1")
        add_dynamic(measure, "mp", "1", "1")
        # Tenor register melody: C3-E3-G3-C4-B3-G3-E3-C3
        if measure_num == 33:
            measure.append(create_note("C", 3, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P4-I1", "1", "1", None, "begin"))
            measure.append(create_note("E", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("G", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("C", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("B", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("G", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("E", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("C", 3, 128, "eighth", False, False, "down", False, True, False, False, False, False, "P4-I1", "1", "1", None, "end"))
        else:
            measure.append(create_note("C", 3, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P4-I1", "1", "1", None, "begin"))
            measure.append(create_note("E", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("G", 3, 256, "quarter", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1"))
            measure.append(create_note("C", 4, 256, "quarter", False, False, "down", False, True, False, False, False, False, "P4-I1", "1", "1"))
    
    elif part_id == "P1":  # Violin I - Supporting role
        add_dynamic(measure, "mp", "1", "1")
        add_direction(measure, "sotto voce", "1", "1")
    
    elif part_id == "P2":  # Violin II - Supporting role
        add_dynamic(measure, "mp", "1", "1")
    
    elif part_id == "P3":  # Viola - Supporting role or takes bass
        add_dynamic(measure, "mp", "1", "1")
        # Viola could take bass function while cello has melody
        if measure_num >= 33:
            add_direction(measure, "pizz.", "1", "1")

def process_v2_1_revisions():
    """Main function to process V2.1 revisions."""
    print("Loading V2 MusicXML file...")
    
    v2_file = "Air-Mov3-V2-ExcellenceEdition.musicxml"
    if not os.path.exists(v2_file):
        print(f"Error: V2 file not found: {v2_file}")
        return None
    
    tree = ET.parse(v2_file)
    root = tree.getroot()
    
    print("V2 file loaded successfully")
    
    # Update title and rights
    work_title = root.find(".//work-title")
    if work_title is not None:
        work_title.text = "Air - Movement 3 (V2.1)"
    
    rights = root.find(".//rights")
    if rights is not None:
        rights.text = "3rd Movement - Air - V2.1 Excellence Edition - November 2025"
    
    print("Processing melodic rotation in measures 9-41...")
    
    # Process each part
    parts = root.findall(".//part")
    for part in parts:
        part_id = part.get("id")
        print(f"Processing part {part_id}...")
        
        measures = part.findall("measure")
        for measure in measures:
            measure_num = int(measure.get("number"))
            
            # Preserve measures 1-8 exactly (core motif)
            if measure_num <= 8:
                continue  # Keep original
            
            # Implement melodic rotation in measures 9-41
            if 9 <= measure_num <= 16:
                implement_measures_9_16(measure, measure_num, part_id)
            elif 17 <= measure_num <= 24:
                implement_measures_17_24(measure, measure_num, part_id)
            elif 25 <= measure_num <= 32:
                implement_measures_25_32(measure, measure_num, part_id)
            elif 33 <= measure_num <= 40:
                implement_measures_33_40(measure, measure_num, part_id)
            # Measures 41-90 already have V2 revisions, keep them
    
    print("V2.1 revisions applied successfully")
    
    # Write output
    output_file = "Air-Mov3-V2.1-ExcellenceEdition.musicxml"
    print(f"Writing output to {output_file}...")
    
    # Get XML declaration and DOCTYPE from original
    with open(v2_file, 'r', encoding='utf-8') as f:
        first_lines = f.readlines()[:2]
        xml_decl = first_lines[0].strip()
        doctype = first_lines[1].strip()
    
    # Convert to string
    rough_string = ET.tostring(root, encoding='unicode')
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent=" ")
    
    # Remove XML declaration from pretty_xml (we'll add our own)
    lines = pretty_xml.split('\n')
    if lines[0].startswith('<?xml'):
        lines = lines[1:]
    
    # Write file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(xml_decl + '\n')
        f.write(doctype + '\n')
        f.write('\n'.join(lines))
    
    print(f"V2.1 MusicXML file created: {output_file}")
    return output_file

if __name__ == "__main__":
    print("=" * 60)
    print("Air Movement V2.1 MusicXML Generator")
    print("Melodic Rotation in Measures 9-41")
    print("=" * 60)
    print()
    
    result = process_v2_1_revisions()
    
    if result:
        print()
        print("=" * 60)
        print("SUCCESS: V2.1 MusicXML file generated!")
        print(f"Output file: {result}")
        print("=" * 60)
        print()
        print("V2.1 Improvements:")
        print("- Measures 9-16: Violin II countermelody added")
        print("- Measures 17-24: Violin II takes primary melody")
        print("- Measures 25-32: Viola featured melodic passage")
        print("- Measures 33-40: Cello featured melodic passage")
        print("- Measures 41-90: V2 revisions preserved")
        print("=" * 60)
    else:
        print()
        print("=" * 60)
        print("ERROR: Failed to generate V2.1 MusicXML file")
        print("=" * 60)
        sys.exit(1)

