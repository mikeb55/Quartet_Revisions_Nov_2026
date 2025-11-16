#!/usr/bin/env python3
"""
Complete V2 Air Movement MusicXML Generator
- Preserves measures 1-8 exactly (core motif)
- Fixes problematic notes (m11, m30)
- Implements ALL note-by-note changes from Implementation Guide
- Adds Air module expressive markings
- Ensures Excellence Criteria compliance
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

def implement_measures_41_44(measure, measure_num, part_id):
    """Implement measures 41-44: Variation Begins"""
    if part_id == "P4":  # Cello - Arco tenor melody
        clear_measure_notes(measure)
        add_direction(measure, "arco", "1", "1")
        add_dynamic(measure, "mp", "1", "1")
        add_direction(measure, "breezy, floating", "1", "1")
        
        if measure_num == 41:
            measure.append(create_note("G", 3, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P4-I1", "1", "1", None, "begin"))
            measure.append(create_note("B", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("D", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("G", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("A", 4, 128, "eighth", False, False, "down", False, True, False, False, False, False, "P4-I1", "1", "1", None, "end"))
            measure.append(create_note(None, None, 256, "quarter", True, False, "up", False, False, False, False, False, False, "P4-I1", "1", "1"))
        elif measure_num == 42:
            measure.append(create_note("G", 4, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P4-I1", "1", "1", None, "begin"))
            measure.append(create_note("A", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("B", 3, 256, "quarter", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1"))
            measure.append(create_note("D", 4, 256, "quarter", False, False, "down", False, True, False, False, False, False, "P4-I1", "1", "1"))
        elif measure_num == 43:
            measure.append(create_note("G", 3, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P4-I1", "1", "1", None, "begin"))
            measure.append(create_note("B", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("D", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("G", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "end"))
            measure.append(create_note("A", 4, 256, "quarter", False, False, "down", False, True, False, False, False, False, "P4-I1", "1", "1"))
        elif measure_num == 44:
            measure.append(create_note("G", 4, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P4-I1", "1", "1", None, "begin"))
            measure.append(create_note("A", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("G", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("B", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "end"))
            measure.append(create_note("D", 4, 256, "quarter", False, False, "down", False, True, False, False, False, False, "P4-I1", "1", "1"))
    
    elif part_id == "P3":  # Viola - Pizzicato bass
        clear_measure_notes(measure)
        add_direction(measure, "pizz.", "1", "1")
        add_dynamic(measure, "mp", "1", "1")
        
        # Walking bass: G2-B2-D3-G3 (quarter notes)
        measure.append(create_note("G", 2, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P3-I1", "1", "1"))
        measure.append(create_note("B", 2, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P3-I1", "1", "1"))
        measure.append(create_note("D", 3, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P3-I1", "1", "1"))
        measure.append(create_note("G", 3, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P3-I1", "1", "1"))
    
    elif part_id == "P1":  # Violin I - 3:2 polyrhythm
        add_dynamic(measure, "mp", "1", "1")
        add_direction(measure, "luminous", "1", "1")
    
    elif part_id == "P2":  # Violin II - Sustained harmonies
        add_dynamic(measure, "mp", "1", "1")

def implement_measures_45_48(measure, measure_num, part_id):
    """Implement measures 45-48: Further Development - Double Stops"""
    if part_id == "P4":  # Cello - Double stops
        clear_measure_notes(measure)
        add_direction(measure, "espressivo", "1", "1")
        add_dynamic(measure, "mf", "1", "1")
        add_direction(measure, "shimmering", "1", "1")
        
        if measure_num == 45:
            # G3-B3 double stop (half notes)
            note1 = create_note("G", 3, 512, "half", False, False, "down", True, False, False, False, False, False, "P4-I1", "1", "1")
            note2 = create_note("B", 3, 512, "half", False, True, "down", True, False, False, False, False, False, "P4-I1", "1", "1")
            measure.append(note1)
            measure.append(note2)
        elif measure_num == 46:
            # A3-C4 double stop
            note1 = create_note("A", 3, 512, "half", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1")
            note2 = create_note("C", 4, 512, "half", False, True, "down", False, False, False, False, False, False, "P4-I1", "1", "1")
            measure.append(note1)
            measure.append(note2)
        elif measure_num == 47:
            # D4-F#4 double stop
            note1 = create_note("D", 4, 512, "half", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1")
            note2 = create_note("F", 4, 512, "half", False, True, "down", False, False, False, False, False, False, "P4-I1", "1", "1", 1)
            measure.append(note1)
            measure.append(note2)
        elif measure_num == 48:
            # G3-B3 double stop
            note1 = create_note("G", 3, 512, "half", False, False, "down", False, True, False, False, False, False, "P4-I1", "1", "1")
            note2 = create_note("B", 3, 512, "half", False, True, "down", False, True, False, False, False, False, "P4-I1", "1", "1")
            measure.append(note1)
            measure.append(note2)
    
    elif part_id == "P3":  # Viola - Continue pizzicato bass
        clear_measure_notes(measure)
        # A2-C3-E3-A3 (quarter notes)
        measure.append(create_note("A", 2, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P3-I1", "1", "1"))
        measure.append(create_note("C", 3, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P3-I1", "1", "1"))
        measure.append(create_note("E", 3, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P3-I1", "1", "1"))
        measure.append(create_note("A", 3, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P3-I1", "1", "1"))
    
    elif part_id == "P1":  # Violin I - 4:3 polyrhythm
        add_dynamic(measure, "mf", "1", "1")
    
    elif part_id == "P2":  # Violin II - Countermelody
        add_dynamic(measure, "mf", "1", "1")

def implement_measures_49_52(measure, measure_num, part_id):
    """Implement measures 49-52: Major Breakpoint - Syncopated Pizzicato"""
    if part_id == "P4":  # Cello - Syncopated pizzicato
        clear_measure_notes(measure)
        add_direction(measure, "pizz.", "1", "1")
        add_dynamic(measure, "f", "1", "1")
        add_direction(measure, "mercurial, scintillating", "1", "1")
        
        if measure_num == 49:
            measure.append(create_note("D", 3, 128, "eighth", False, False, "up", False, False, False, True, False, True, "P4-I1", "1", "1"))
            measure.append(create_note(None, None, 128, "eighth", True, False, "up", False, False, False, False, False, False, "P4-I1", "1", "1"))
            measure.append(create_note("F", 3, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P4-I1", "1", "1", 1))
            measure.append(create_note("A", 3, 384, "dotted-quarter", False, False, "up", False, False, False, True, False, True, "P4-I1", "1", "1"))
        elif measure_num == 50:
            measure.append(create_note("D", 3, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P4-I1", "1", "1"))
            measure.append(create_note("F", 3, 128, "eighth", False, False, "up", False, False, False, True, False, True, "P4-I1", "1", "1", 1))
            measure.append(create_note("A", 3, 128, "eighth", False, False, "up", False, False, False, True, False, False, "P4-I1", "1", "1"))
            measure.append(create_note("D", 3, 512, "half", False, False, "up", False, False, False, True, False, False, "P4-I1", "1", "1"))
        elif measure_num == 51:
            measure.append(create_note("D", 3, 128, "eighth", False, False, "up", False, False, False, True, False, True, "P4-I1", "1", "1"))
            measure.append(create_note("F", 3, 128, "eighth", False, False, "up", False, False, False, True, False, False, "P4-I1", "1", "1", 1))
            measure.append(create_note("A", 3, 256, "quarter", False, False, "up", False, False, False, True, False, True, "P4-I1", "1", "1"))
            measure.append(create_note("D", 3, 512, "half", False, False, "up", False, False, False, True, False, False, "P4-I1", "1", "1"))
        elif measure_num == 52:
            measure.append(create_note("D", 3, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P4-I1", "1", "1"))
            measure.append(create_note("F", 3, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P4-I1", "1", "1", 1))
            measure.append(create_note("A", 3, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P4-I1", "1", "1"))
            measure.append(create_note("D", 3, 256, "quarter", False, False, "up", False, False, False, True, False, True, "P4-I1", "1", "1"))
    
    else:  # Other parts - Tutti
        add_dynamic(measure, "f", "1", "1")

def implement_measures_53_56(measure, measure_num, part_id):
    """Implement measures 53-56: Sparse Duet"""
    if part_id == "P4":  # Cello - Arco Motif 2 variation
        clear_measure_notes(measure)
        add_direction(measure, "arco", "1", "1")
        add_direction(measure, "espressivo, dolce", "1", "1")
        add_dynamic(measure, "mp", "1", "1")
        add_direction(measure, "diaphanous, gliding", "1", "1")
        
        # Flowing Motif 2: E3-G3-B3-E4-D4-B3-G3
        if measure_num == 53:
            measure.append(create_note("E", 3, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P4-I1", "1", "1", None, "begin"))
            measure.append(create_note("G", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("B", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("E", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("D", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("B", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("G", 3, 128, "eighth", False, False, "down", False, True, False, False, False, False, "P4-I1", "1", "1", None, "end"))
            measure.append(create_note(None, None, 128, "eighth", True, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1"))
        elif measure_num == 54:
            measure.append(create_note("E", 3, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P4-I1", "1", "1", None, "begin"))
            measure.append(create_note("G", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("B", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("E", 4, 256, "quarter", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1"))
            measure.append(create_note("D", 4, 256, "quarter", False, False, "down", False, True, False, False, False, False, "P4-I1", "1", "1"))
        elif measure_num == 55:
            measure.append(create_note("E", 3, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P4-I1", "1", "1", None, "begin"))
            measure.append(create_note("G", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("B", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("E", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "end"))
            measure.append(create_note("D", 4, 256, "quarter", False, False, "down", False, True, False, False, False, False, "P4-I1", "1", "1"))
        elif measure_num == 56:
            measure.append(create_note("E", 3, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P4-I1", "1", "1", None, "begin"))
            measure.append(create_note("G", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("B", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("E", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "end"))
            measure.append(create_note("D", 4, 256, "quarter", False, False, "down", False, True, False, False, False, False, "P4-I1", "1", "1"))
    
    elif part_id == "P2":  # Violin II - Pizzicato bass
        clear_measure_notes(measure)
        add_direction(measure, "pizz.", "1", "1")
        add_dynamic(measure, "p", "1", "1")
        # B2-D3-F3-B2 (quarter notes)
        measure.append(create_note("B", 2, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P2-I1", "1", "1"))
        measure.append(create_note("D", 3, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P2-I1", "1", "1"))
        measure.append(create_note("F", 3, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P2-I1", "1", "1"))
        measure.append(create_note("B", 2, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P2-I1", "1", "1"))
    
    else:  # Violin I, Viola - Rest or sustained
        clear_measure_notes(measure)
        add_dynamic(measure, "p", "1", "1")
        measure.append(create_note(None, None, 1024, "whole", True, False, "up", False, False, False, False, False, False, f"{part_id}-I1", "1", "1"))

def implement_measures_57_60(measure, measure_num, part_id):
    """Implement measures 57-60: Lighter Transition"""
    if part_id == "P4":  # Cello - Pizzicato with slower harmonic rhythm
        clear_measure_notes(measure)
        add_direction(measure, "pizz.", "1", "1")
        add_dynamic(measure, "mp", "1", "1")
        # C3-E3-G3-C3 (half notes)
        measure.append(create_note("C", 3, 512, "half", False, False, "up", False, False, False, True, False, False, "P4-I1", "1", "1"))
        measure.append(create_note("E", 3, 512, "half", False, False, "up", False, False, False, True, False, False, "P4-I1", "1", "1"))
    
    elif part_id == "P3":  # Viola - Sustained harmonies
        add_dynamic(measure, "mp", "1", "1")
    
    else:
        add_dynamic(measure, "mp", "1", "1")

def implement_measures_61_64(measure, measure_num, part_id):
    """Implement measures 61-64: Cello-Viola Arco Duet"""
    if part_id == "P4":  # Cello - Motif 1 + 2 integrated
        clear_measure_notes(measure)
        add_direction(measure, "arco", "1", "1")
        add_direction(measure, "espressivo", "1", "1")
        add_dynamic(measure, "mp", "1", "1")
        add_direction(measure, "conversational, mirrored", "1", "1")
        
        # E3-G3-B3-E4-D4-B3-G3-E3 (eighth notes)
        if measure_num == 61:
            measure.append(create_note("E", 3, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P4-I1", "1", "1", None, "begin"))
            measure.append(create_note("G", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("B", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("E", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("D", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("B", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("G", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("E", 3, 128, "eighth", False, False, "down", False, True, False, False, False, False, "P4-I1", "1", "1", None, "end"))
        else:
            # Similar patterns for measures 62-64
            measure.append(create_note("E", 3, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P4-I1", "1", "1", None, "begin"))
            measure.append(create_note("G", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("B", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("E", 4, 256, "quarter", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1"))
            measure.append(create_note("D", 4, 256, "quarter", False, False, "down", False, True, False, False, False, False, "P4-I1", "1", "1"))
    
    elif part_id == "P3":  # Viola - Countermelody on C-string
        clear_measure_notes(measure)
        add_direction(measure, "arco", "1", "1")
        add_direction(measure, "sul C", "1", "1")
        add_dynamic(measure, "mp", "1", "1")
        # G3-B3-D4-G3-F#3-D3-B3-G3 (eighth notes)
        measure.append(create_note("G", 3, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P3-I1", "1", "1", None, "begin"))
        measure.append(create_note("B", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P3-I1", "1", "1", None, "continue"))
        measure.append(create_note("D", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P3-I1", "1", "1", None, "continue"))
        measure.append(create_note("G", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P3-I1", "1", "1", None, "continue"))
        measure.append(create_note("F", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P3-I1", "1", "1", 1, "continue"))
        measure.append(create_note("D", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P3-I1", "1", "1", None, "continue"))
        measure.append(create_note("B", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P3-I1", "1", "1", None, "continue"))
        measure.append(create_note("G", 3, 128, "eighth", False, False, "down", False, True, False, False, False, False, "P3-I1", "1", "1", None, "end"))
    
    else:  # Violin I, Violin II - Rest or sustained
        clear_measure_notes(measure)
        add_dynamic(measure, "p", "1", "1")
        measure.append(create_note(None, None, 1024, "whole", True, False, "up", False, False, False, False, False, False, f"{part_id}-I1", "1", "1"))

def implement_measures_65_68(measure, measure_num, part_id):
    """Implement measures 65-68: Role Exchange"""
    if part_id == "P4":  # Cello - Melodic pizzicato bass
        clear_measure_notes(measure)
        add_direction(measure, "pizz.", "1", "1")
        add_dynamic(measure, "mf", "1", "1")
        # G2-B2-D3-G3 (quarter notes with melodic contour)
        measure.append(create_note("G", 2, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P4-I1", "1", "1"))
        measure.append(create_note("B", 2, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P4-I1", "1", "1"))
        measure.append(create_note("D", 3, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P4-I1", "1", "1"))
        measure.append(create_note("G", 3, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P4-I1", "1", "1"))
    
    elif part_id == "P3":  # Viola - Melody
        add_direction(measure, "arco", "1", "1")
        add_direction(measure, "espressivo", "1", "1")
        add_dynamic(measure, "mf", "1", "1")
    
    else:
        add_dynamic(measure, "mf", "1", "1")

def implement_measures_69_72(measure, measure_num, part_id):
    """Implement measures 69-72: Expressive Cello Solo"""
    if part_id == "P4":  # Cello - Featured solo
        clear_measure_notes(measure)
        add_direction(measure, "arco", "1", "1")
        add_direction(measure, "espressivo, solo", "1", "1")
        add_dynamic(measure, "mp", "1", "1")
        add_direction(measure, "luminous, radiant, prismatic", "1", "1")
        
        # A3-C4-E4-A4-G4-E4-C4-A3 (eighth notes)
        if measure_num == 69:
            measure.append(create_note("A", 3, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P4-I1", "1", "1", None, "begin"))
            measure.append(create_note("C", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("E", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("A", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("G", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("E", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("C", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("A", 3, 128, "eighth", False, False, "down", False, True, False, False, False, False, "P4-I1", "1", "1", None, "end"))
        else:
            measure.append(create_note("A", 3, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P4-I1", "1", "1", None, "begin"))
            measure.append(create_note("C", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
            measure.append(create_note("E", 4, 256, "quarter", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1"))
            measure.append(create_note("A", 4, 256, "quarter", False, False, "down", False, True, False, False, False, False, "P4-I1", "1", "1"))
    
    else:  # Other parts - Sustained harmonies
        clear_measure_notes(measure)
        add_dynamic(measure, "p", "1", "1")
        # A-C-E chord tones (whole notes)
        if part_id == "P3":
            measure.append(create_note("A", 3, 1024, "whole", False, False, "up", False, False, False, False, False, False, "P3-I1", "1", "1"))
        elif part_id == "P1":
            measure.append(create_note("A", 4, 1024, "whole", False, False, "down", False, False, False, False, False, False, "P1-I1", "1", "1"))
        elif part_id == "P2":
            measure.append(create_note("C", 5, 1024, "whole", False, False, "down", False, False, False, False, False, False, "P2-I1", "1", "1"))

def implement_measures_73_76(measure, measure_num, part_id):
    """Implement measures 73-76: Syncopated Pizz Bass, Tutti"""
    if part_id == "P4":  # Cello - Syncopated pizzicato
        clear_measure_notes(measure)
        add_direction(measure, "pizz.", "1", "1")
        add_dynamic(measure, "f", "1", "1")
        # D3-F#3-A3-D3 (quarter notes with off-beat accents)
        measure.append(create_note("D", 3, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P4-I1", "1", "1"))
        measure.append(create_note("F", 3, 256, "quarter", False, False, "up", False, False, False, True, False, True, "P4-I1", "1", "1", 1))
        measure.append(create_note("A", 3, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P4-I1", "1", "1"))
        measure.append(create_note("D", 3, 256, "quarter", False, False, "up", False, False, False, True, False, True, "P4-I1", "1", "1"))
    
    else:
        add_dynamic(measure, "f", "1", "1")

def implement_measures_77_80(measure, measure_num, part_id):
    """Implement measures 77-80: Cello Arco Sustained"""
    if part_id == "P4":  # Cello - Sustained foundation
        clear_measure_notes(measure)
        add_direction(measure, "arco", "1", "1")
        add_direction(measure, "tenuto", "1", "1")
        add_dynamic(measure, "mf", "1", "1")
        measure.append(create_note("G", 2, 1024, "whole", False, False, "up", False, False, True, False, False, False, "P4-I1", "1", "1"))
    
    elif part_id == "P3":  # Viola - Pizzicato bass
        clear_measure_notes(measure)
        add_direction(measure, "pizz.", "1", "1")
        add_dynamic(measure, "mp", "1", "1")
        # G2-B2-D3-G3 (quarter notes)
        measure.append(create_note("G", 2, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P3-I1", "1", "1"))
        measure.append(create_note("B", 2, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P3-I1", "1", "1"))
        measure.append(create_note("D", 3, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P3-I1", "1", "1"))
        measure.append(create_note("G", 3, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P3-I1", "1", "1"))
    
    else:
        add_dynamic(measure, "mp", "1", "1")

def implement_measures_81_84(measure, measure_num, part_id):
    """Implement measures 81-84: Transformed Recapitulation"""
    if part_id == "P4":  # Cello - Arco melody
        clear_measure_notes(measure)
        add_direction(measure, "arco", "1", "1")
        add_direction(measure, "espressivo", "1", "1")
        add_dynamic(measure, "mp", "1", "1")
        add_direction(measure, "elegant, refined, circulating", "1", "1")
        
        # G3-B3-D4-G4-A4-G4 (eighth notes)
        measure.append(create_note("G", 3, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P4-I1", "1", "1", None, "begin"))
        measure.append(create_note("B", 3, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
        measure.append(create_note("D", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
        measure.append(create_note("G", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
        measure.append(create_note("A", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
        measure.append(create_note("G", 4, 128, "eighth", False, False, "down", False, True, False, False, False, False, "P4-I1", "1", "1", None, "end"))
        measure.append(create_note(None, None, 512, "half", True, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1"))
    
    elif part_id == "P3":  # Viola - Pizzicato bass
        clear_measure_notes(measure)
        add_direction(measure, "pizz.", "1", "1")
        add_dynamic(measure, "mp", "1", "1")
        # G2-B2-D3-G3 (quarter notes)
        measure.append(create_note("G", 2, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P3-I1", "1", "1"))
        measure.append(create_note("B", 2, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P3-I1", "1", "1"))
        measure.append(create_note("D", 3, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P3-I1", "1", "1"))
        measure.append(create_note("G", 3, 256, "quarter", False, False, "up", False, False, False, True, False, False, "P3-I1", "1", "1"))
    
    else:
        add_dynamic(measure, "mp", "1", "1")

def implement_measures_85_88(measure, measure_num, part_id):
    """Implement measures 85-88: Lyrical Cello-Violin I Duet"""
    if part_id == "P4":  # Cello - Countermelody
        clear_measure_notes(measure)
        add_direction(measure, "arco", "1", "1")
        add_direction(measure, "dolce", "1", "1")
        add_dynamic(measure, "mp", "1", "1")
        
        # A3-C4-E4-A4-G4-E4-C4-A3 (eighth notes)
        measure.append(create_note("A", 3, 128, "eighth", False, False, "down", True, False, False, False, False, False, "P4-I1", "1", "1", None, "begin"))
        measure.append(create_note("C", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
        measure.append(create_note("E", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
        measure.append(create_note("A", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
        measure.append(create_note("G", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
        measure.append(create_note("E", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
        measure.append(create_note("C", 4, 128, "eighth", False, False, "down", False, False, False, False, False, False, "P4-I1", "1", "1", None, "continue"))
        measure.append(create_note("A", 3, 128, "eighth", False, False, "down", False, True, False, False, False, False, "P4-I1", "1", "1", None, "end"))
    
    elif part_id == "P1":  # Violin I - Melody
        add_direction(measure, "dolce", "1", "1")
        add_dynamic(measure, "mp", "1", "1")
    
    else:
        clear_measure_notes(measure)
        add_dynamic(measure, "p", "1", "1")
        measure.append(create_note(None, None, 1024, "whole", True, False, "up", False, False, False, False, False, False, f"{part_id}-I1", "1", "1"))

def implement_measures_89_90(measure, measure_num, part_id):
    """Implement measures 89-90: Airy Harmonic Resolution"""
    if part_id == "P4":  # Cello - Sustained with harmonic
        clear_measure_notes(measure)
        add_direction(measure, "arco", "1", "1")
        add_direction(measure, "harm.", "1", "1")
        add_direction(measure, "tenuto", "1", "1")
        add_dynamic(measure, "p", "1", "1")
        add_direction(measure, "weightless, translucent, airy", "1", "1")
        measure.append(create_note("G", 2, 1024, "whole", False, False, "up", False, False, True, False, False, True, "P4-I1", "1", "1"))
    
    else:
        clear_measure_notes(measure)
        add_dynamic(measure, "pp", "1", "1")
        if measure_num == 90:
            add_direction(measure, "harm.", "1", "1")
        # Sustained harmonies
        if part_id == "P3":
            measure.append(create_note("G", 3, 1024, "whole", False, False, "up", False, False, False, False, False, False, "P3-I1", "1", "1"))
        elif part_id == "P1":
            measure.append(create_note("B", 4, 1024, "whole", False, False, "down", False, False, False, False, False, False, "P1-I1", "1", "1"))
        elif part_id == "P2":
            measure.append(create_note("D", 5, 1024, "whole", False, False, "down", False, False, False, False, False, False, "P2-I1", "1", "1"))

def process_v2_revisions():
    """Main function to process V2 revisions."""
    print("Loading original MusicXML file...")
    
    original_file = "../AIR mvmt Version 1/Air-Mov4-ExcellenceEdition.musicxml"
    if not os.path.exists(original_file):
        print(f"Error: Original file not found: {original_file}")
        return None
    
    tree = ET.parse(original_file)
    root = tree.getroot()
    
    print("File loaded successfully")
    
    # Update title and rights
    work_title = root.find(".//work-title")
    if work_title is not None:
        work_title.text = "Air - Movement 3 (V2)"
    
    rights = root.find(".//rights")
    if rights is not None:
        rights.text = "3rd Movement - Air - V2 Excellence Edition - November 2025"
    
    # Update credits
    for credit in root.findall(".//credit"):
        for words in credit.findall(".//credit-words"):
            if "Movement 4" in words.text:
                words.text = words.text.replace("Movement 4", "Movement 3 (V2)")
    
    print("Processing parts...")
    
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
            
            # Fix problematic notes
            if measure_num == 11 and part_id == "P1":
                # Replace D6 with F#5
                for note in measure.findall("note"):
                    pitch = note.find("pitch")
                    if pitch is not None:
                        step = pitch.find("step")
                        octave = pitch.find("octave")
                        if step is not None and octave is not None:
                            if step.text == "D" and octave.text == "6":
                                step.text = "F"
                                alter = ET.SubElement(pitch, "alter")
                                alter.text = "1"
                                octave.text = "5"
                                print(f"  Fixed m11: D6 -> F#5")
            
            if measure_num == 30 and part_id == "P1":
                # Replace C6 with A5
                for note in measure.findall("note"):
                    pitch = note.find("pitch")
                    if pitch is not None:
                        step = pitch.find("step")
                        octave = pitch.find("octave")
                        if step is not None and octave is not None:
                            if step.text == "C" and octave.text == "6":
                                step.text = "A"
                                octave.text = "5"
                                print(f"  Fixed m30: C6 -> A5")
            
            # Apply V2 revisions starting at measure 41
            if 41 <= measure_num <= 44:
                implement_measures_41_44(measure, measure_num, part_id)
            elif 45 <= measure_num <= 48:
                implement_measures_45_48(measure, measure_num, part_id)
            elif 49 <= measure_num <= 52:
                implement_measures_49_52(measure, measure_num, part_id)
            elif 53 <= measure_num <= 56:
                implement_measures_53_56(measure, measure_num, part_id)
            elif 57 <= measure_num <= 60:
                implement_measures_57_60(measure, measure_num, part_id)
            elif 61 <= measure_num <= 64:
                implement_measures_61_64(measure, measure_num, part_id)
            elif 65 <= measure_num <= 68:
                implement_measures_65_68(measure, measure_num, part_id)
            elif 69 <= measure_num <= 72:
                implement_measures_69_72(measure, measure_num, part_id)
            elif 73 <= measure_num <= 76:
                implement_measures_73_76(measure, measure_num, part_id)
            elif 77 <= measure_num <= 80:
                implement_measures_77_80(measure, measure_num, part_id)
            elif 81 <= measure_num <= 84:
                implement_measures_81_84(measure, measure_num, part_id)
            elif 85 <= measure_num <= 88:
                implement_measures_85_88(measure, measure_num, part_id)
            elif 89 <= measure_num <= 90:
                implement_measures_89_90(measure, measure_num, part_id)
    
    print("V2 revisions applied successfully")
    
    # Write output
    output_file = "Air-Mov3-V2-ExcellenceEdition.musicxml"
    print(f"Writing output to {output_file}...")
    
    # Get XML declaration and DOCTYPE from original
    with open(original_file, 'r', encoding='utf-8') as f:
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
    
    print(f"V2 MusicXML file created: {output_file}")
    return output_file

if __name__ == "__main__":
    print("=" * 60)
    print("Air Movement V2 Complete MusicXML Generator")
    print("=" * 60)
    print()
    
    result = process_v2_revisions()
    
    if result:
        print()
        print("=" * 60)
        print("SUCCESS: Complete V2 MusicXML file generated!")
        print(f"Output file: {result}")
        print("=" * 60)
    else:
        print()
        print("=" * 60)
        print("ERROR: Failed to generate V2 MusicXML file")
        print("=" * 60)
        sys.exit(1)

