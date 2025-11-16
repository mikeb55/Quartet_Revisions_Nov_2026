#!/usr/bin/env python3
"""
Generate measures 58-90 for P1, P2, P3 based on composition guide
"""

def create_note_xml(pitch_step, octave, duration, alter=None, rest=False, 
                    tie_start=False, tie_stop=False, slur_start=False, slur_stop=False,
                    tenuto=False, staccato=False, accent=False, chord=False,
                    default_x=15, stem="up", voice=1, part_id="P1"):
    """Create a note XML element"""
    if rest:
        return f'''   <note default-x="{default_x}">
    <rest />
    <duration>{duration}</duration>
    <instrument id="{part_id}-I1" />
    <voice>{voice}</voice>
    <type>{get_note_type(duration)}</type>
    <staff>1</staff>
   </note>'''
    
    alter_str = f"\n     <alter>{alter}</alter>" if alter is not None else ""
    chord_str = "\n    <chord />" if chord else ""
    tie_start_str = f"\n    <tie type=\"start\" />" if tie_start else ""
    tie_stop_str = f"\n    <tie type=\"stop\" />" if tie_stop else ""
    
    notations = []
    if slur_start:
        notations.append('     <slur color="#000000" type="start" orientation="over" />')
    if slur_stop:
        notations.append('     <slur color="#000000" type="stop" orientation="over" />')
    if tenuto:
        notations.append('     <articulations>\n      <tenuto />\n     </articulations>')
    if staccato:
        notations.append('     <articulations>\n      <staccato />\n     </articulations>')
    if accent:
        notations.append('     <articulations>\n      <accent />\n     </articulations>')
    
    notations_str = ""
    if notations:
        notations_str = f"\n    <notations>\n" + "\n".join(notations) + "\n    </notations>"
    
    return f'''   <note color="#000000" default-x="{default_x}">{chord_str}
    <pitch>
     <step>{pitch_step}</step>{alter_str}
     <octave>{octave}</octave>
    </pitch>{tie_start_str}{tie_stop_str}
    <duration>{duration}</duration>
    <instrument id="{part_id}-I1" />
    <voice>{voice}</voice>
    <type>{get_note_type(duration)}</type>
    <stem>{stem}</stem>
    <staff>1</staff>{notations_str}
   </note>'''

def get_note_type(duration):
    """Convert duration to note type"""
    if duration == 1024:
        return "whole"
    elif duration == 512:
        return "half"
    elif duration == 256:
        return "quarter"
    elif duration == 128:
        return "eighth"
    elif duration == 64:
        return "16th"
    return "quarter"

def create_measure_xml(measure_num, part_id, notes_xml, dynamics=None, words=None, 
                       new_system=False, new_page=False, width=227):
    """Create a measure XML element"""
    print_str = ""
    if new_page:
        print_str = '''   <print new-page="yes">
    <system-layout>
     <system-margins>
      <left-margin>81</left-margin>
      <right-margin>0</right-margin>
     </system-margins>
    </system-layout>
    <staff-layout number="1">
     <staff-distance>75</staff-distance>
    </staff-layout>
   </print>
   <attributes>
    <staff-details number="1" print-object="yes">
     <staff-size>75</staff-size>
    </staff-details>
   </attributes>'''
    elif new_system:
        print_str = '''   <print new-system="yes">
    <system-layout>
     <system-margins>
      <left-margin>81</left-margin>
      <right-margin>0</right-margin>
     </system-margins>
    </system-layout>
    <staff-layout number="1">
     <staff-distance>75</staff-distance>
    </staff-layout>
   </print>
   <attributes>
    <staff-details number="1" print-object="yes">
     <staff-size>75</staff-size>
    </staff-details>
   </attributes>'''
    
    direction_str = ""
    if dynamics:
        direction_str += f'''   <direction>
    <direction-type>
     <dynamics default-x="75" default-y="-70" color="#000000" font-family="Opus Text Std" font-style="normal" font-size="10.5784" font-weight="normal">
      <{dynamics} />
     </dynamics>
    </direction-type>
    <voice>1</voice>
    <staff>1</staff>
   </direction>
'''
    if words:
        direction_str += f'''   <direction>
    <direction-type>
     <words default-x="75" default-y="15" justify="left" valign="middle" font-family="Palatino Linotype" font-style="normal" font-size="9.7541" font-weight="normal">{words}</words>
    </direction-type>
    <voice>1</voice>
    <staff>1</staff>
   </direction>
'''
    
    barline = ""
    if measure_num == 90:
        barline = '''   <barline>
    <bar-style>light-heavy</bar-style>
   </barline>'''
    
    return f'''  <!--============== Part: {part_id}, Measure: {measure_num} ==============-->
  <measure number="{measure_num}" width="{width}">
{print_str}{direction_str}{notes_xml}{barline}
  </measure>
'''

# Generate measures 58-90 for P1 (Violin I)
def generate_p1_measures_58_90():
    """Generate measures 58-90 for Violin I"""
    measures = []
    
    # Measure 58: C6-B5 (tenuto), rest, A5 (quarter note, legato)
    measures.append(create_measure_xml(58, "P1", 
        create_note_xml("C", 6, 256, tenuto=True, slur_start=True) +
        create_note_xml("B", 5, 256, tenuto=True) +
        create_note_xml("", 0, 256, rest=True) +
        create_note_xml("A", 5, 256, slur_stop=True),
        dynamics="mf"))
    
    # Measure 59: C5-E5-G5 (quarter notes, legato)
    measures.append(create_measure_xml(59, "P1",
        create_note_xml("C", 5, 256, slur_start=True) +
        create_note_xml("E", 5, 256) +
        create_note_xml("G", 5, 256, slur_stop=True)))
    
    # Measure 60: C6-B5-A5-G5 (quarter notes, legato)
    measures.append(create_measure_xml(60, "P1",
        create_note_xml("C", 6, 256, slur_start=True) +
        create_note_xml("B", 5, 256) +
        create_note_xml("A", 5, 256) +
        create_note_xml("G", 5, 256, slur_stop=True),
        dynamics="mp"))
    
    # Measures 61-64: E5-G5-B5-E6 (triplets, legato) - Motifs Integrate
    for m in range(61, 65):
        if m == 61:
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("E", 5, 256, slur_start=True) +
                create_note_xml("G", 5, 256) +
                create_note_xml("B", 5, 256) +
                create_note_xml("E", 6, 256, slur_stop=True),
                dynamics="mp"))
        elif m == 62:
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("D", 6, 256, slur_start=True) +
                create_note_xml("B", 5, 256) +
                create_note_xml("G", 5, 256) +
                create_note_xml("E", 5, 256, slur_stop=True)))
        elif m == 63:
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("E", 5, 256, slur_start=True) +
                create_note_xml("G", 5, 256) +
                create_note_xml("B", 5, 256) +
                create_note_xml("E", 6, 256, slur_stop=True)))
        else:  # 64
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("D", 6, 256, slur_start=True) +
                create_note_xml("B", 5, 256) +
                create_note_xml("G", 5, 256) +
                create_note_xml("E", 5, 256, slur_stop=True)))
    
    # Measures 65-68: G4-B4-D5-G5 (eighth notes, legato) - Motif Combination
    for m in range(65, 69):
        if m == 65:
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("G", 4, 128, slur_start=True) +
                create_note_xml("B", 4, 128) +
                create_note_xml("D", 5, 128) +
                create_note_xml("G", 5, 128, slur_stop=True)))
        elif m == 66:
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("A", 5, 512, slur_start=True, tenuto=True) +
                create_note_xml("G", 5, 256, slur_stop=True) +
                create_note_xml("F", 5, 256, alter=1)))
        elif m == 67:
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("G", 4, 256, slur_start=True) +
                create_note_xml("B", 4, 256) +
                create_note_xml("D", 5, 256) +
                create_note_xml("G", 5, 256, slur_stop=True)))
        else:  # 68
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("A", 5, 256, slur_start=True) +
                create_note_xml("G", 5, 256) +
                create_note_xml("F", 5, 256, alter=1) +
                create_note_xml("E", 5, 256, slur_stop=True)))
    
    # Measures 69-72: A4-C5-E5-A5 (eighth notes, legato) - Motif Development
    for m in range(69, 73):
        if m == 69:
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("A", 4, 128, slur_start=True) +
                create_note_xml("C", 5, 128) +
                create_note_xml("E", 5, 128) +
                create_note_xml("A", 5, 128, slur_stop=True)))
        elif m == 70:
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("G", 5, 512, slur_start=True, tenuto=True) +
                create_note_xml("E", 5, 256, slur_stop=True) +
                create_note_xml("C", 5, 256)))
        elif m == 71:
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("A", 4, 256, slur_start=True) +
                create_note_xml("C", 5, 256) +
                create_note_xml("E", 5, 256) +
                create_note_xml("A", 5, 256, slur_stop=True)))
        else:  # 72
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("G", 5, 256, slur_start=True) +
                create_note_xml("E", 5, 256) +
                create_note_xml("C", 5, 256) +
                create_note_xml("A", 4, 256, slur_stop=True)))
    
    # Measures 73-76: D5-F#5-A5-D6 (16th notes, legato) - Motif Variation
    for m in range(73, 77):
        if m == 73:
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("D", 5, 64, slur_start=True) +
                create_note_xml("F", 5, 64, alter=1) +
                create_note_xml("A", 5, 64) +
                create_note_xml("D", 6, 64, slur_stop=True) +
                create_note_xml("C", 6, 64, slur_start=True) +
                create_note_xml("A", 5, 64) +
                create_note_xml("F", 5, 64, alter=1) +
                create_note_xml("D", 5, 64, slur_stop=True),
                dynamics="mp"))
        elif m == 74:
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("C", 6, 64, slur_start=True) +
                create_note_xml("A", 5, 64) +
                create_note_xml("F", 5, 64, alter=1) +
                create_note_xml("D", 5, 64, slur_stop=True) +
                create_note_xml("D", 5, 64, slur_start=True) +
                create_note_xml("F", 5, 64, alter=1) +
                create_note_xml("A", 5, 64) +
                create_note_xml("D", 6, 64, slur_stop=True)))
        elif m == 75:
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("D", 5, 256, slur_start=True) +
                create_note_xml("F", 5, 256, alter=1) +
                create_note_xml("A", 5, 256) +
                create_note_xml("D", 6, 256, slur_stop=True)))
        else:  # 76
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("C", 6, 256, slur_start=True) +
                create_note_xml("A", 5, 256) +
                create_note_xml("F", 5, 256, alter=1) +
                create_note_xml("D", 5, 256, slur_stop=True),
                dynamics="p"))
    
    # Measures 77-80: G4-B4-D5-G5 (eighth notes, legato) - Motif Resolution
    for m in range(77, 81):
        if m == 77:
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("G", 4, 128, slur_start=True) +
                create_note_xml("B", 4, 128) +
                create_note_xml("D", 5, 128) +
                create_note_xml("G", 5, 128, slur_stop=True),
                dynamics="p"))
        elif m == 78:
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("A", 5, 512, slur_start=True, tenuto=True) +
                create_note_xml("G", 5, 256, slur_stop=True) +
                create_note_xml("F", 5, 256, alter=1)))
        elif m == 79:
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("G", 4, 256, slur_start=True) +
                create_note_xml("B", 4, 256) +
                create_note_xml("D", 5, 256) +
                create_note_xml("G", 5, 256, slur_stop=True)))
        else:  # 80
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("A", 5, 256, slur_start=True) +
                create_note_xml("G", 5, 256) +
                create_note_xml("F", 5, 256, alter=1) +
                create_note_xml("E", 5, 256, slur_stop=True)))
    
    # Measures 81-84: G4-B4-D5-G5 (eighth notes, legato) - Motif 1 Returns
    for m in range(81, 85):
        if m == 81:
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("G", 4, 128, slur_start=True) +
                create_note_xml("B", 4, 128) +
                create_note_xml("D", 5, 128) +
                create_note_xml("G", 5, 128, slur_stop=True),
                dynamics="p"))
        elif m == 82:
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("A", 5, 512, slur_start=True, tenuto=True) +
                create_note_xml("G", 5, 256, slur_stop=True) +
                create_note_xml("F", 5, 256, alter=1)))
        elif m == 83:
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("G", 4, 256, slur_start=True) +
                create_note_xml("B", 4, 256) +
                create_note_xml("D", 5, 256) +
                create_note_xml("G", 5, 256, slur_stop=True)))
        else:  # 84
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("A", 5, 256, slur_start=True) +
                create_note_xml("G", 5, 256) +
                create_note_xml("F", 5, 256, alter=1) +
                create_note_xml("E", 5, 256, slur_stop=True)))
    
    # Measures 85-88: A4-C5-E5-A5 (eighth notes, legato) - Final Development
    for m in range(85, 89):
        if m == 85:
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("A", 4, 128, slur_start=True) +
                create_note_xml("C", 5, 128) +
                create_note_xml("E", 5, 128) +
                create_note_xml("A", 5, 128, slur_stop=True),
                dynamics="p"))
        elif m == 86:
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("G", 5, 512, slur_start=True, tenuto=True) +
                create_note_xml("E", 5, 256, slur_stop=True) +
                create_note_xml("C", 5, 256),
                dynamics="pp"))
        elif m == 87:
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("A", 4, 256, slur_start=True) +
                create_note_xml("C", 5, 256) +
                create_note_xml("E", 5, 256) +
                create_note_xml("A", 5, 256, slur_stop=True)))
        else:  # 88
            measures.append(create_measure_xml(m, "P1",
                create_note_xml("G", 5, 256, slur_start=True) +
                create_note_xml("E", 5, 256) +
                create_note_xml("C", 5, 256) +
                create_note_xml("A", 4, 256, slur_stop=True)))
    
    # Measures 89-90: Final Resolution
    measures.append(create_measure_xml(89, "P1",
        create_note_xml("G", 4, 512, tenuto=True, slur_start=True) +
        create_note_xml("B", 4, 256, tenuto=True) +
        create_note_xml("D", 5, 256, tenuto=True, slur_stop=True),
        dynamics="pp", words="morendo"))
    
    measures.append(create_measure_xml(90, "P1",
        create_note_xml("A", 5, 1024, tenuto=True, slur_start=True),
        dynamics="pp", words="morendo"))
    
    return "\n".join(measures)

# Generate measures 58-90 for P2 (Violin II)
def generate_p2_measures_58_90():
    """Generate measures 58-90 for Violin II"""
    measures = []
    
    # Measures 58-60: E4-G4-B4 (E minor triad, whole notes, legato)
    for m in range(58, 61):
        measures.append(create_measure_xml(m, "P2",
            create_note_xml("E", 4, 1024, slur_start=True) +
            create_note_xml("G", 4, 1024, chord=True) +
            create_note_xml("B", 4, 1024, chord=True, slur_stop=True)))
    
    # Measures 61-64: G4-B4-D5 (G major triad, whole notes, legato, duplets)
    for m in range(61, 65):
        measures.append(create_measure_xml(m, "P2",
            create_note_xml("G", 4, 1024, slur_start=True) +
            create_note_xml("B", 4, 1024, chord=True) +
            create_note_xml("D", 5, 1024, chord=True, slur_stop=True)))
    
    # Measures 65-68: B3-D4-F#4 (B minor triad, whole notes, legato)
    for m in range(65, 69):
        measures.append(create_measure_xml(m, "P2",
            create_note_xml("B", 3, 1024, slur_start=True) +
            create_note_xml("D", 4, 1024, chord=True) +
            create_note_xml("F", 4, 1024, alter=1, chord=True, slur_stop=True)))
    
    # Measures 69-72: C4-E4-G4 (C major triad, whole notes, legato)
    for m in range(69, 73):
        measures.append(create_measure_xml(m, "P2",
            create_note_xml("C", 4, 1024, slur_start=True) +
            create_note_xml("E", 4, 1024, chord=True) +
            create_note_xml("G", 4, 1024, chord=True, slur_stop=True)))
    
    # Measures 73-76: F#4-A4-C#5 (F# minor triad, whole notes, legato, triplets)
    for m in range(73, 77):
        measures.append(create_measure_xml(m, "P2",
            create_note_xml("F", 4, 1024, alter=1, slur_start=True) +
            create_note_xml("A", 4, 1024, chord=True) +
            create_note_xml("C", 5, 1024, alter=1, chord=True, slur_stop=True)))
    
    # Measures 77-80: B3-D4-F#4 (B minor triad, whole notes, legato)
    for m in range(77, 81):
        measures.append(create_measure_xml(m, "P2",
            create_note_xml("B", 3, 1024, slur_start=True) +
            create_note_xml("D", 4, 1024, chord=True) +
            create_note_xml("F", 4, 1024, alter=1, chord=True, slur_stop=True)))
    
    # Measures 81-84: B3-D4-F#4 (B minor triad, whole notes, legato)
    for m in range(81, 85):
        measures.append(create_measure_xml(m, "P2",
            create_note_xml("B", 3, 1024, slur_start=True) +
            create_note_xml("D", 4, 1024, chord=True) +
            create_note_xml("F", 4, 1024, alter=1, chord=True, slur_stop=True)))
    
    # Measures 85-88: C4-E4-G4 (C major triad, whole notes, legato)
    for m in range(85, 89):
        measures.append(create_measure_xml(m, "P2",
            create_note_xml("C", 4, 1024, slur_start=True) +
            create_note_xml("E", 4, 1024, chord=True) +
            create_note_xml("G", 4, 1024, chord=True, slur_stop=True)))
    
    # Measures 89-90: E4-G4-B4-E5 (half note, tenuto, harmonics, legato) then Rest
    measures.append(create_measure_xml(89, "P2",
        create_note_xml("E", 4, 512, tenuto=True, slur_start=True) +
        create_note_xml("G", 4, 256, tenuto=True, chord=True) +
        create_note_xml("B", 4, 256, tenuto=True, chord=True, slur_stop=True) +
        create_note_xml("E", 5, 256, tenuto=True, chord=True),
        dynamics="pp"))
    
    measures.append(create_measure_xml(90, "P2",
        create_note_xml("", 0, 1024, rest=True),
        dynamics="pp"))
    
    return "\n".join(measures)

# Generate measures 58-90 for P3 (Viola)
def generate_p3_measures_58_90():
    """Generate measures 58-90 for Viola"""
    measures = []
    
    # Measures 58-60: E3-G3-B3 (E minor triad, whole notes, legato)
    for m in range(58, 61):
        measures.append(create_measure_xml(m, "P3",
            create_note_xml("E", 3, 1024, slur_start=True) +
            create_note_xml("G", 3, 1024, chord=True) +
            create_note_xml("B", 3, 1024, chord=True, slur_stop=True)))
    
    # Measures 61-64: G3-B3-D4 (G major triad, whole notes, legato, duplets)
    for m in range(61, 65):
        measures.append(create_measure_xml(m, "P3",
            create_note_xml("G", 3, 1024, slur_start=True) +
            create_note_xml("B", 3, 1024, chord=True) +
            create_note_xml("D", 4, 1024, chord=True, slur_stop=True)))
    
    # Measures 65-68: B3-D4-F#4 (B minor triad, whole notes, legato)
    for m in range(65, 69):
        measures.append(create_measure_xml(m, "P3",
            create_note_xml("B", 3, 1024, slur_start=True) +
            create_note_xml("D", 4, 1024, chord=True) +
            create_note_xml("F", 4, 1024, alter=1, chord=True, slur_stop=True)))
    
    # Measures 69-72: C3-E3-G3 (C major triad, whole notes, legato)
    for m in range(69, 73):
        measures.append(create_measure_xml(m, "P3",
            create_note_xml("C", 3, 1024, slur_start=True) +
            create_note_xml("E", 3, 1024, chord=True) +
            create_note_xml("G", 3, 1024, chord=True, slur_stop=True)))
    
    # Measures 73-76: F#3-A3-C#4 (F# minor triad, whole notes, legato, triplets)
    for m in range(73, 77):
        measures.append(create_measure_xml(m, "P3",
            create_note_xml("F", 3, 1024, alter=1, slur_start=True) +
            create_note_xml("A", 3, 1024, chord=True) +
            create_note_xml("C", 4, 1024, alter=1, chord=True, slur_stop=True)))
    
    # Measures 77-80: B3-D4-F#4 (B minor triad, whole notes, legato)
    for m in range(77, 81):
        measures.append(create_measure_xml(m, "P3",
            create_note_xml("B", 3, 1024, slur_start=True) +
            create_note_xml("D", 4, 1024, chord=True) +
            create_note_xml("F", 4, 1024, alter=1, chord=True, slur_stop=True)))
    
    # Measures 81-84: B3-D4-F#4 (B minor triad, whole notes, legato)
    for m in range(81, 85):
        measures.append(create_measure_xml(m, "P3",
            create_note_xml("B", 3, 1024, slur_start=True) +
            create_note_xml("D", 4, 1024, chord=True) +
            create_note_xml("F", 4, 1024, alter=1, chord=True, slur_stop=True)))
    
    # Measures 85-88: C3-E3-G3 (C major triad, whole notes, legato)
    for m in range(85, 89):
        measures.append(create_measure_xml(m, "P3",
            create_note_xml("C", 3, 1024, slur_start=True) +
            create_note_xml("E", 3, 1024, chord=True) +
            create_note_xml("G", 3, 1024, chord=True, slur_stop=True)))
    
    # Measures 89-90: Rest
    measures.append(create_measure_xml(89, "P3",
        create_note_xml("", 0, 1024, rest=True)))
    
    measures.append(create_measure_xml(90, "P3",
        create_note_xml("", 0, 1024, rest=True)))
    
    return "\n".join(measures)

if __name__ == "__main__":
    p1_measures = generate_p1_measures_58_90()
    p2_measures = generate_p2_measures_58_90()
    p3_measures = generate_p3_measures_58_90()
    
    print("P1 measures 58-90:")
    print(p1_measures)
    print("\nP2 measures 58-90:")
    print(p2_measures)
    print("\nP3 measures 58-90:")
    print(p3_measures)
    
    # Write to file for inspection
    with open("measures_58_90_output.txt", "w") as f:
        f.write("P1:\n" + p1_measures + "\n\nP2:\n" + p2_measures + "\n\nP3:\n" + p3_measures)

