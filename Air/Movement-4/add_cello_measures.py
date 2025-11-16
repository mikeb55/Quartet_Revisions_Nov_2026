# Quick script to generate Cello measures 7-89 XML
# Output will be inserted into MusicXML file

def cello_measure(measure_num, notes_list, pizzicato=True, arco=False, slurs=False, tenor=False):
    """Generate XML for a Cello measure with 4 quarter notes"""
    # notes_list: [(step, octave, alter), ...] where alter is None or 1 for sharp
    positions = [15, 81, 147, 213]
    
    xml = f'  <!--============== Part: P4, Measure: {measure_num} ==============-->\n'
    xml += '  <measure number="' + str(measure_num) + '" width="217">\n'
    
    if tenor:
        xml += '   <direction>\n'
        xml += '    <direction-type>\n'
        xml += '     <words default-y="-60" font-size="10" relative-x="0">tenor</words>\n'
        xml += '    </direction-type>\n'
        xml += '   </direction>\n'
    
    for i, (step, octave, alter) in enumerate(notes_list):
        alter_str = f'     <alter>{alter}</alter>\n' if alter is not None else ''
        stem_dir = 'up' if octave >= 3 else 'down'
        
        articulations = []
        if pizzicato:
            articulations.append('      <pizzicato />')
        if i == 0 and not pizzicato:  # tenuto for arco first note
            articulations.append('      <tenuto />')
        
        artic_xml = ''
        if articulations:
            artic_xml = '     <articulations>\n' + '\n'.join(articulations) + '\n     </articulations>'
        
        slur_xml = ''
        if slurs:
            if i == 0:
                slur_xml = '     <slur color="#000000" type="start" orientation="over" />'
            elif i < 3:
                slur_xml = '     <slur color="#000000" type="continue" orientation="over" />'
            else:
                slur_xml = '     <slur color="#000000" type="stop" orientation="over" />'
        
        notations_parts = []
        if artic_xml:
            notations_parts.append(artic_xml)
        if slur_xml:
            notations_parts.append(slur_xml)
        
        notations_xml = ''
        if notations_parts:
            notations_xml = '    <notations>\n' + '\n'.join(notations_parts) + '\n    </notations>'
        
        xml += f'   <note color="#000000" default-x="{positions[i]}">\n'
        xml += '    <pitch>\n'
        xml += f'     <step>{step}</step>\n'
        xml += alter_str
        xml += f'     <octave>{octave}</octave>\n'
        xml += '    </pitch>\n'
        xml += '    <duration>256</duration>\n'
        xml += '    <instrument id="P4-I1" />\n'
        xml += '    <voice>1</voice>\n'
        xml += '    <type>quarter</type>\n'
        xml += f'    <stem>{stem_dir}</stem>\n'
        xml += '    <staff>1</staff>\n'
        if notations_xml:
            xml += notations_xml + '\n'
        xml += '   </note>\n'
    
    xml += '  </measure>\n'
    return xml

# Generate all measures
output = []

# M7-8: A2-C3-D3-F#3
for m in [7, 8]:
    output.append(cello_measure(m, [('A', 2, None), ('C', 3, None), ('D', 3, None), ('F#', 3, 1)]))

# M9-12: D3-F#3-A3
for m in [9, 10, 11, 12]:
    output.append(cello_measure(m, [('D', 3, None), ('F#', 3, 1), ('A', 3, None), ('D', 3, None)]))

# M13-16: B2-D3-F3
for m in [13, 14, 15, 16]:
    output.append(cello_measure(m, [('B', 2, None), ('D', 3, None), ('F', 3, None), ('B', 2, None)]))

# M17-20: C3-E3-G3
for m in [17, 18, 19, 20]:
    output.append(cello_measure(m, [('C', 3, None), ('E', 3, None), ('G', 3, None), ('C', 3, None)]))

# M21-24: E3-F#3-G3-A3, B3-C4-D4-E4 (arco, slurs, tenor)
output.append(cello_measure(21, [('E', 3, None), ('F#', 3, 1), ('G', 3, None), ('A', 3, None)], pizzicato=False, arco=True, slurs=True, tenor=True))
output.append(cello_measure(22, [('B', 3, None), ('C', 4, None), ('D', 4, None), ('E', 4, None)], pizzicato=False, arco=True, slurs=True))
output.append(cello_measure(23, [('E', 3, None), ('F#', 3, 1), ('G', 3, None), ('A', 3, None)], pizzicato=False, arco=True, slurs=True))
output.append(cello_measure(24, [('B', 3, None), ('C', 4, None), ('D', 4, None), ('E', 4, None)], pizzicato=False, arco=True, slurs=True))

# M25-28: A2-C3-E3-A3
for m in [25, 26, 27, 28]:
    output.append(cello_measure(m, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)]))

# M29-32: D3-F#3-A3
for m in [29, 30, 31, 32]:
    output.append(cello_measure(m, [('D', 3, None), ('F#', 3, 1), ('A', 3, None), ('D', 3, None)]))

# M33-36: G2-B2-D3-G3
for m in [33, 34, 35, 36]:
    output.append(cello_measure(m, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)]))

# M37-40: E3-G3-B3
for m in [37, 38, 39, 40]:
    output.append(cello_measure(m, [('E', 3, None), ('G', 3, None), ('B', 3, None), ('E', 3, None)]))

# M41-44: G2-B2-D3-G3
for m in [41, 42, 43, 44]:
    output.append(cello_measure(m, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)]))

# M45-48: A2-C3-E3-A3
for m in [45, 46, 47, 48]:
    output.append(cello_measure(m, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)]))

# M49-52: D3-F#3-A3
for m in [49, 50, 51, 52]:
    output.append(cello_measure(m, [('D', 3, None), ('F#', 3, 1), ('A', 3, None), ('D', 3, None)]))

# M53-56: B2-D3-F3
for m in [53, 54, 55, 56]:
    output.append(cello_measure(m, [('B', 2, None), ('D', 3, None), ('F', 3, None), ('B', 2, None)]))

# M57-60: C3-E3-G3
for m in [57, 58, 59, 60]:
    output.append(cello_measure(m, [('C', 3, None), ('E', 3, None), ('G', 3, None), ('C', 3, None)]))

# M61-64: E3-G3-B3
for m in [61, 62, 63, 64]:
    output.append(cello_measure(m, [('E', 3, None), ('G', 3, None), ('B', 3, None), ('E', 3, None)]))

# M65-68: G2-B2-D3-G3
for m in [65, 66, 67, 68]:
    output.append(cello_measure(m, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)]))

# M69-72: A2-C3-E3-A3
for m in [69, 70, 71, 72]:
    output.append(cello_measure(m, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)]))

# M73-76: D3-F#3-A3
for m in [73, 74, 75, 76]:
    output.append(cello_measure(m, [('D', 3, None), ('F#', 3, 1), ('A', 3, None), ('D', 3, None)]))

# M77-80: G2-B2-D3-G3
for m in [77, 78, 79, 80]:
    output.append(cello_measure(m, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)]))

# M81-84: G2-B2-D3-G3
for m in [81, 82, 83, 84]:
    output.append(cello_measure(m, [('G', 2, None), ('B', 2, None), ('D', 3, None), ('G', 3, None)]))

# M85-88: A2-C3-E3-A3
for m in [85, 86, 87, 88]:
    output.append(cello_measure(m, [('A', 2, None), ('C', 3, None), ('E', 3, None), ('A', 3, None)]))

# M89: G2 (half note, tenuto, arco)
output.append('''  <!--============== Part: P4, Measure: 89 ==============-->
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
  </measure>
''')

# M90: G2 (whole note, tenuto, arco, fermata)
output.append('''  <!--============== Part: P4, Measure: 90 ==============-->
  <measure number="90" width="217">
   <note color="#000000" default-x="15">
    <pitch>
     <step>G</step>
     <octave>2</octave>
    </pitch>
    <duration>1024</duration>
    <instrument id="P4-I1" />
    <voice>1</voice>
    <type>whole</type>
    <stem>down</stem>
    <staff>1</staff>
    <notations>
     <articulations>
      <tenuto />
      <fermata type="normal" />
     </articulations>
    </notations>
   </note>
   <barline>
    <bar-style>light-heavy</bar-style>
   </barline>
  </measure>
''')

print(''.join(output))

