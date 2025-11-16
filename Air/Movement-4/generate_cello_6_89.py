# Generate Cello measures 6-89
# This script generates all remaining Cello measures per Air-Mov4-COMPLETE-COMPOSITION.md

def generate_quarter_note_measure(measure_num, notes, pizzicato=True, arco=False, slurs=False, tenuto=False, tenor_marking=False):
    """Generate a measure with 4 quarter notes"""
    output = []
    
    if tenor_marking:
        output.append(f"""  <!--============== Part: P4, Measure: {measure_num} ==============-->
  <measure number="{measure_num}" width="217">
   <direction>
    <direction-type>
     <words default-y="-60" font-size="10" relative-x="0">tenor</words>
    </direction-type>
   </direction>""")
    else:
        output.append(f"""  <!--============== Part: P4, Measure: {measure_num} ==============-->
  <measure number="{measure_num}" width="217">""")
    
    positions = [15, 81, 147, 213]
    for i, (step, octave, alter) in enumerate(notes):
        alter_xml = f"     <alter>{alter}</alter>\n" if alter is not None else ""
        
        articulations = []
        if pizzicato:
            articulations.append("      <pizzicato />")
        if tenuto and i == 0:  # Only first note gets tenuto
            articulations.append("      <tenuto />")
        
        articulations_xml = ""
        if articulations:
            articulations_xml = f"""     <articulations>
{chr(10).join(articulations)}
     </articulations>"""
        
        slur_xml = ""
        if slurs:
            if i == 0:
                slur_xml = """     <slur color="#000000" type="start" orientation="over" />"""
            elif i < 3:
                slur_xml = """     <slur color="#000000" type="continue" orientation="over" />"""
            else:
                slur_xml = """     <slur color="#000000" type="stop" orientation="over" />"""
        
        notations_parts = []
        if articulations_xml:
            notations_parts.append(articulations_xml)
        if slur_xml:
            notations_parts.append(slur_xml)
        
        notations_xml = ""
        if notations_parts:
            notations_xml = f"""    <notations>
{chr(10).join(notations_parts)}
    </notations>"""
        
        note_xml = f"""   <note color="#000000" default-x="{positions[i]}">
    <pitch>
     <step>{step}</step>
{alter_xml}     <octave>{octave}</octave>
    </pitch>
    <duration>256</duration>
    <instrument id="P4-I1" />
    <voice>1</voice>
    <type>quarter</type>
    <stem>{"up" if octave >= 3 else "down"}</stem>
    <staff>1</staff>
{notations_xml}
   </note>"""
        output.append(note_xml)
    
    output.append("  </measure>")
    return "\n".join(output)

# Define all measures
measures_data = [
    # M6-8: A2-C3-D3-F#3 (quarter notes, pizzicato)
    (6, [('A', 2, None), ('C', 3, None), ('D', 3, None), ('F#', 3, 1)], True, False, False, False, False),
    (7, [('A', 2, None), ('C', 3, None), ('D', 3, None), ('F#', 3, 1)], True, False, False, False, False),
    (8, [('A', 2, None), ('C', 3, None), ('D', 3, None), ('F#', 3, 1)], True, False, False, False, False),
    # M9-12: D3-F#3-A3 (D major triad, quarter notes, pizzicato)
    (9, [('D', 3, None), ('F#', 3, 1), ('A', 3, None), ('D', 3, None)], True, False, False, False, False),
    (10, [('D', 3, None), ('F#', 3, 1), ('A', 3, None), ('D', 3, None)], True, False, False, False, False),
    (11, [('D', 3, None), ('F#', 3, 1), ('A', 3, None), ('D', 3, None)], True, False, False, False, False),
    (12, [('D', 3, None), ('F#', 3, 1), ('A', 3, None), ('D', 3, None)], True, False, False, False, False),
    # M13-16: B2-D3-F3 (B diminished triad, quarter notes, pizzicato)
    (13, [('B', 2, None), ('D', 3, None), ('F', 3, None), ('B', 2, None)], True, False, False, False, False),
    (14, [('B', 2, None), ('D', 3, None), ('F', 3, None), ('B', 2, None)], True, False, False, False, False),
    (15, [('B', 2, None), ('D', 3, None), ('F', 3, None), ('B', 2, None)], True, False, False, False, False),
    (16, [('B', 2, None), ('D', 3, None), ('F', 3, None), ('B', 2, None)], True, False, False, False, False),
    # M17-20: C3-E3-G3 (C major triad, quarter notes, pizzicato)
    (17, [('C', 3, None), ('E', 3, None), ('G', 3, None), ('C', 3, None)], True, False, False, False, False),
    (18, [('C', 3, None), ('E', 3, None), ('G', 3, None), ('C', 3, None)], True, False, False, False, False),
    (19, [('C', 3, None), ('E', 3, None), ('G', 3, None), ('C', 3, None)], True, False, False, False, False),
    (20, [('C', 3, None), ('E', 3, None), ('G', 3, None), ('C', 3, None)], True, False, False, False, False),
    # M21-24: E3-F#3-G3-A3, B3-C4-D4-E4 (quarter notes, arco, slurs, tenuto, "tenor" marking)
    (21, [('E', 3, None), ('F#', 3, 1), ('G', 3, None), ('A', 3, None)], False, True, True, True, True),
    (22, [('B', 3, None), ('C', 4, None), ('D', 4, None), ('E', 4, None)], False, True, True, False, False),
    (23, [('E', 3, None), ('F#', 3, 1), ('G', 3, None), ('A', 3, None)], False, True, True, False, False),
    (24, [('B', 3, None), ('C', 4, None), ('D', 4, None), ('E', 4, None)], False, True, True, False, False),
    # M25-28: A2-C3-E3-A3 (quarter notes, pizzicato, walking bass)
    (25, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)], True, False, False, False, False),
    (26, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)], True, False, False, False, False),
    (27, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)], True, False, False, False, False),
    (28, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)], True, False, False, False, False),
    # M29-32: D3-F#3-A3 (D major triad, quarter notes, pizzicato)
    (29, [('D', 3, None), ('F#', 3, 1), ('A', 3, None), ('D', 3, None)], True, False, False, False, False),
    (30, [('D', 3, None), ('F#', 3, 1), ('A', 3, None), ('D', 3, None)], True, False, False, False, False),
    (31, [('D', 3, None), ('F#', 3, 1), ('A', 3, None), ('D', 3, None)], True, False, False, False, False),
    (32, [('D', 3, None), ('F#', 3, 1), ('A', 3, None), ('D', 3, None)], True, False, False, False, False),
    # M33-36: G2-B2-D3-G3 (quarter notes, pizzicato)
    (33, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)], True, False, False, False, False),
    (34, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)], True, False, False, False, False),
    (35, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)], True, False, False, False, False),
    (36, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)], True, False, False, False, False),
    # M37-40: E3-G3-B3 (E minor triad, quarter notes, pizzicato)
    (37, [('E', 3, None), ('G', 3, None), ('B', 3, None), ('E', 3, None)], True, False, False, False, False),
    (38, [('E', 3, None), ('G', 3, None), ('B', 3, None), ('E', 3, None)], True, False, False, False, False),
    (39, [('E', 3, None), ('G', 3, None), ('B', 3, None), ('E', 3, None)], True, False, False, False, False),
    (40, [('E', 3, None), ('G', 3, None), ('B', 3, None), ('E', 3, None)], True, False, False, False, False),
    # M41-44: G2-B2-D3-G3 (quarter notes, pizzicato, duplets)
    (41, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)], True, False, False, False, False),
    (42, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)], True, False, False, False, False),
    (43, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)], True, False, False, False, False),
    (44, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)], True, False, False, False, False),
    # M45-48: A2-C3-E3-A3 (quarter notes, pizzicato, triplets)
    (45, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)], True, False, False, False, False),
    (46, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)], True, False, False, False, False),
    (47, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)], True, False, False, False, False),
    (48, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)], True, False, False, False, False),
    # M49-52: D3-F#3-A3 (D major triad, quarter notes, pizzicato, 16th notes)
    (49, [('D', 3, None), ('F#', 3, 1), ('A', 3, None), ('D', 3, None)], True, False, False, False, False),
    (50, [('D', 3, None), ('F#', 3, 1), ('A', 3, None), ('D', 3, None)], True, False, False, False, False),
    (51, [('D', 3, None), ('F#', 3, 1), ('A', 3, None), ('D', 3, None)], True, False, False, False, False),
    (52, [('D', 3, None), ('F#', 3, 1), ('A', 3, None), ('D', 3, None)], True, False, False, False, False),
    # M53-56: B2-D3-F3 (B diminished triad, quarter notes, pizzicato)
    (53, [('B', 2, None), ('D', 3, None), ('F', 3, None), ('B', 2, None)], True, False, False, False, False),
    (54, [('B', 2, None), ('D', 3, None), ('F', 3, None), ('B', 2, None)], True, False, False, False, False),
    (55, [('B', 2, None), ('D', 3, None), ('F', 3, None), ('B', 2, None)], True, False, False, False, False),
    (56, [('B', 2, None), ('D', 3, None), ('F', 3, None), ('B', 2, None)], True, False, False, False, False),
    # M57-60: C3-E3-G3 (C major triad, quarter notes, pizzicato)
    (57, [('C', 3, None), ('E', 3, None), ('G', 3, None), ('C', 3, None)], True, False, False, False, False),
    (58, [('C', 3, None), ('E', 3, None), ('G', 3, None), ('C', 3, None)], True, False, False, False, False),
    (59, [('C', 3, None), ('E', 3, None), ('G', 3, None), ('C', 3, None)], True, False, False, False, False),
    (60, [('C', 3, None), ('E', 3, None), ('G', 3, None), ('C', 3, None)], True, False, False, False, False),
    # M61-64: E3-G3-B3 (E minor triad, quarter notes, pizzicato, duplets)
    (61, [('E', 3, None), ('G', 3, None), ('B', 3, None), ('E', 3, None)], True, False, False, False, False),
    (62, [('E', 3, None), ('G', 3, None), ('B', 3, None), ('E', 3, None)], True, False, False, False, False),
    (63, [('E', 3, None), ('G', 3, None), ('B', 3, None), ('E', 3, None)], True, False, False, False, False),
    (64, [('E', 3, None), ('G', 3, None), ('B', 3, None), ('E', 3, None)], True, False, False, False, False),
    # M65-68: G2-B2-D3-G3 (quarter notes, pizzicato)
    (65, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)], True, False, False, False, False),
    (66, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)], True, False, False, False, False),
    (67, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)], True, False, False, False, False),
    (68, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)], True, False, False, False, False),
    # M69-72: A2-C3-E3-A3 (quarter notes, pizzicato)
    (69, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)], True, False, False, False, False),
    (70, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)], True, False, False, False, False),
    (71, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)], True, False, False, False, False),
    (72, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)], True, False, False, False, False),
    # M73-76: D3-F#3-A3 (D major triad, quarter notes, pizzicato, triplets)
    (73, [('D', 3, None), ('F#', 3, 1), ('A', 3, None), ('D', 3, None)], True, False, False, False, False),
    (74, [('D', 3, None), ('F#', 3, 1), ('A', 3, None), ('D', 3, None)], True, False, False, False, False),
    (75, [('D', 3, None), ('F#', 3, 1), ('A', 3, None), ('D', 3, None)], True, False, False, False, False),
    (76, [('D', 3, None), ('F#', 3, 1), ('A', 3, None), ('D', 3, None)], True, False, False, False, False),
    # M77-80: G2-B2-D3-G3 (quarter notes, pizzicato)
    (77, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)], True, False, False, False, False),
    (78, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)], True, False, False, False, False),
    (79, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)], True, False, False, False, False),
    (80, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)], True, False, False, False, False),
    # M81-84: G2-B2-D3-G3 (quarter notes, pizzicato)
    (81, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)], True, False, False, False, False),
    (82, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)], True, False, False, False, False),
    (83, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)], True, False, False, False, False),
    (84, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)], True, False, False, False, False),
    # M85-88: A2-C3-E3-A3 (quarter notes, pizzicato)
    (85, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)], True, False, False, False, False),
    (86, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)], True, False, False, False, False),
    (87, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)], True, False, False, False, False),
    (88, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)], True, False, False, False, False),
    # M89: G2 (half note, tenuto, arco, legato) - special measure
]

# Generate all measures
output = []
for measure_num, notes, pizzicato, arco, slurs, tenuto, tenor_marking in measures_data:
    output.append(generate_quarter_note_measure(measure_num, notes, pizzicato, arco, slurs, tenuto, tenor_marking))

# M89: G2 (half note, tenuto, arco, legato) - special measure
output.append("""  <!--============== Part: P4, Measure: 89 ==============-->
  <measure number="89" width="217">
   <note color="#000000" default-x="15">
    <pitch>
     <step>G</step>
     <octave>2</octave>
    </pitch>
    <duration>512</duration>
    <instrument id="P4-I1" />
    <voice>1</voice>
    <type>half</type>
    <stem>down</stem>
    <staff>1</staff>
    <notations>
     <articulations>
      <tenuto />
     </articulations>
    </notations>
   </note>
  </measure>""")

print('\n'.join(output))

