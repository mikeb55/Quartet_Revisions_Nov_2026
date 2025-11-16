#!/usr/bin/env python3
"""
Generate Cello measures 18-89 XML for insertion into MusicXML file
"""

def generate_pizzicato_measure(measure_num, notes):
    """Generate XML for a pizzicato measure with 4 quarter notes"""
    # notes: list of tuples (step, octave, alter) where alter is None or 1 for sharp
    positions = [15, 81, 147, 213]
    xml = []
    xml.append(f'  <!--============== Part: P4, Measure: {measure_num} ==============-->')
    xml.append(f'  <measure number="{measure_num}" width="217">')
    
    for i, (step, octave, alter) in enumerate(notes):
        alter_xml = f'     <alter>{alter}</alter>\n' if alter is not None else ''
        stem_dir = 'up' if octave >= 3 else 'down'
        
        xml.append(f'   <note color="#000000" default-x="{positions[i]}">')
        xml.append('    <pitch>')
        xml.append(f'     <step>{step}</step>')
        if alter_xml:
            xml.append(alter_xml.rstrip())
        xml.append(f'     <octave>{octave}</octave>')
        xml.append('    </pitch>')
        xml.append('    <duration>256</duration>')
        xml.append('    <instrument id="P4-I1" />')
        xml.append('    <voice>1</voice>')
        xml.append('    <type>quarter</type>')
        xml.append(f'    <stem>{stem_dir}</stem>')
        xml.append('    <staff>1</staff>')
        xml.append('    <notations>')
        xml.append('     <articulations>')
        xml.append('      <pizzicato />')
        xml.append('     </articulations>')
        xml.append('    </notations>')
        xml.append('   </note>')
    
    xml.append('  </measure>')
    return '\n'.join(xml)

def generate_arco_measure(measure_num, notes, tenor=False):
    """Generate XML for an arco measure with slurs"""
    positions = [15, 81, 147, 213]
    xml = []
    xml.append(f'  <!--============== Part: P4, Measure: {measure_num} ==============-->')
    xml.append(f'  <measure number="{measure_num}" width="217">')
    
    if tenor:
        xml.append('   <direction>')
        xml.append('    <direction-type>')
        xml.append('     <words default-y="-60" font-size="10" relative-x="0">tenor</words>')
        xml.append('    </direction-type>')
        xml.append('   </direction>')
    
    for i, (step, octave, alter) in enumerate(notes):
        alter_xml = f'     <alter>{alter}</alter>\n' if alter is not None else ''
        stem_dir = 'up' if octave >= 3 else 'down'
        
        # Slur types
        if i == 0:
            slur_type = 'start'
        elif i < 3:
            slur_type = 'continue'
        else:
            slur_type = 'stop'
        
        xml.append(f'   <note color="#000000" default-x="{positions[i]}">')
        xml.append('    <pitch>')
        xml.append(f'     <step>{step}</step>')
        if alter_xml:
            xml.append(alter_xml.rstrip())
        xml.append(f'     <octave>{octave}</octave>')
        xml.append('    </pitch>')
        xml.append('    <duration>256</duration>')
        xml.append('    <instrument id="P4-I1" />')
        xml.append('    <voice>1</voice>')
        xml.append('    <type>quarter</type>')
        xml.append(f'    <stem>{stem_dir}</stem>')
        xml.append('    <staff>1</staff>')
        xml.append('    <notations>')
        if i == 0:
            xml.append('     <articulations>')
            xml.append('      <tenuto />')
            xml.append('     </articulations>')
        xml.append(f'     <slur color="#000000" type="{slur_type}" orientation="over" />')
        xml.append('    </notations>')
        xml.append('   </note>')
    
    xml.append('  </measure>')
    return '\n'.join(xml)

def generate_half_note_measure(measure_num, step, octave):
    """Generate XML for measure 89 (half note, arco, tenuto)"""
    xml = []
    xml.append(f'  <!--============== Part: P4, Measure: {measure_num} ==============-->')
    xml.append(f'  <measure number="{measure_num}" width="217">')
    xml.append('   <note color="#000000" default-x="15">')
    xml.append('    <pitch>')
    xml.append(f'     <step>{step}</step>')
    xml.append(f'     <octave>{octave}</octave>')
    xml.append('    </pitch>')
    xml.append('    <duration>512</duration>')
    xml.append('    <instrument id="P4-I1" />')
    xml.append('    <voice>1</voice>')
    xml.append('    <type>half</type>')
    xml.append('    <stem>down</stem>')
    xml.append('    <staff>1</staff>')
    xml.append('    <notations>')
    xml.append('     <articulations>')
    xml.append('      <tenuto />')
    xml.append('     </articulations>')
    xml.append('    </notations>')
    xml.append('   </note>')
    xml.append('  </measure>')
    return '\n'.join(xml)

# Generate all measures
output = []

# M18-20: C3-E3-G3-C3 (C major, pizzicato)
for m in [18, 19, 20]:
    output.append(generate_pizzicato_measure(m, [('C', 3, None), ('E', 3, None), ('G', 3, None), ('C', 3, None)]))

# M21-24: E3-F#3-G3-A3, B3-C4-D4-E4 (arco, slurs, tenor marking on M21)
output.append(generate_arco_measure(21, [('E', 3, None), ('F', 3, 1), ('G', 3, None), ('A', 3, None)], tenor=True))
output.append(generate_arco_measure(22, [('B', 3, None), ('C', 4, None), ('D', 4, None), ('E', 4, None)]))
output.append(generate_arco_measure(23, [('E', 3, None), ('F', 3, 1), ('G', 3, None), ('A', 3, None)]))
output.append(generate_arco_measure(24, [('B', 3, None), ('C', 4, None), ('D', 4, None), ('E', 4, None)]))

# M25-28: A2-C3-E3-A3 (pizzicato)
for m in [25, 26, 27, 28]:
    output.append(generate_pizzicato_measure(m, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)]))

# M29-32: D3-F#3-A3-D3 (pizzicato)
for m in [29, 30, 31, 32]:
    output.append(generate_pizzicato_measure(m, [('D', 3, None), ('F', 3, 1), ('A', 3, None), ('D', 3, None)]))

# M33-36: G2-B2-D3-G3 (pizzicato)
for m in [33, 34, 35, 36]:
    output.append(generate_pizzicato_measure(m, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)]))

# M37-40: E3-G3-B3-E3 (pizzicato)
for m in [37, 38, 39, 40]:
    output.append(generate_pizzicato_measure(m, [('E', 3, None), ('G', 3, None), ('B', 3, None), ('E', 3, None)]))

# M41-44: G2-B2-D3-G3 (pizzicato)
for m in [41, 42, 43, 44]:
    output.append(generate_pizzicato_measure(m, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)]))

# M45-48: A2-C3-E3-A3 (pizzicato)
for m in [45, 46, 47, 48]:
    output.append(generate_pizzicato_measure(m, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)]))

# M49-52: D3-F#3-A3-D3 (pizzicato)
for m in [49, 50, 51, 52]:
    output.append(generate_pizzicato_measure(m, [('D', 3, None), ('F', 3, 1), ('A', 3, None), ('D', 3, None)]))

# M53-56: B2-D3-F3-B2 (pizzicato)
for m in [53, 54, 55, 56]:
    output.append(generate_pizzicato_measure(m, [('B', 2, None), ('D', 3, None), ('F', 3, None), ('B', 2, None)]))

# M57-60: C3-E3-G3-C3 (pizzicato)
for m in [57, 58, 59, 60]:
    output.append(generate_pizzicato_measure(m, [('C', 3, None), ('E', 3, None), ('G', 3, None), ('C', 3, None)]))

# M61-64: E3-G3-B3-E3 (pizzicato)
for m in [61, 62, 63, 64]:
    output.append(generate_pizzicato_measure(m, [('E', 3, None), ('G', 3, None), ('B', 3, None), ('E', 3, None)]))

# M65-68: G2-B2-D3-G3 (pizzicato)
for m in [65, 66, 67, 68]:
    output.append(generate_pizzicato_measure(m, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)]))

# M69-72: A2-C3-E3-A3 (pizzicato)
for m in [69, 70, 71, 72]:
    output.append(generate_pizzicato_measure(m, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)]))

# M73-76: D3-F#3-A3-D3 (pizzicato)
for m in [73, 74, 75, 76]:
    output.append(generate_pizzicato_measure(m, [('D', 3, None), ('F', 3, 1), ('A', 3, None), ('D', 3, None)]))

# M77-80: G2-B2-D3-G3 (pizzicato)
for m in [77, 78, 79, 80]:
    output.append(generate_pizzicato_measure(m, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)]))

# M81-84: G2-B2-D3-G3 (pizzicato)
for m in [81, 82, 83, 84]:
    output.append(generate_pizzicato_measure(m, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)]))

# M85-88: A2-C3-E3-A3 (pizzicato)
for m in [85, 86, 87, 88]:
    output.append(generate_pizzicato_measure(m, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)]))

# M89: G2 (half note, arco, tenuto)
output.append(generate_half_note_measure(89, 'G', 2))

# Print all measures
print('\n'.join(output))


