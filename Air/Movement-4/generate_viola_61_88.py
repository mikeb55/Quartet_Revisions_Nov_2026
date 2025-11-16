# Generate Viola measures 61-88
# M61-64: G3-B3-D4 (G major)
# M65-68: B3-D4-F#4 (B minor)
# M69-72: C3-E3-G3 (C major)
# M73-76: F#3-A3-C#4 (F# minor)
# M77-80: B3-D4-F#4 (B minor)
# M81-84: B3-D4-F#4 (B minor)
# M85-88: C3-E3-G3 (C major)

triads = [
    (61, [('G', 3), ('B', 3), ('D', 4), ('G', 3)]),  # G major
    (65, [('B', 3), ('D', 4), ('F#', 4), ('B', 3)]),  # B minor
    (69, [('C', 3), ('E', 3), ('G', 3), ('C', 3)]),  # C major
    (73, [('F#', 3), ('A', 3), ('C#', 4), ('F#', 3)]),  # F# minor
    (77, [('B', 3), ('D', 4), ('F#', 4), ('B', 3)]),  # B minor
    (81, [('B', 3), ('D', 4), ('F#', 4), ('B', 3)]),  # B minor
    (85, [('C', 3), ('E', 3), ('G', 3), ('C', 3)]),  # C major
]

output = []
for start_measure, notes in triads:
    for i, (step, octave) in enumerate(notes):
        measure_num = start_measure + i
        alter = None
        if step == 'F#':
            step = 'F'
            alter = 1
        elif step == 'C#':
            step = 'C'
            alter = 1
        
        slur_type = "start" if i == 0 else "continue" if i < 3 else "stop"
        
        alter_xml = f"     <alter>{alter}</alter>\n" if alter is not None else ""
        
        measure_xml = f"""  <!--============== Part: P3, Measure: {measure_num} ==============-->
  <measure number="{measure_num}" width="217">
   <note color="#000000" default-x="15">
    <pitch>
     <step>{step}</step>
{alter_xml}     <octave>{octave}</octave>
    </pitch>
    <duration>1024</duration>
    <instrument id="P3-I1" />
    <voice>1</voice>
    <type>whole</type>
    <stem>up</stem>
    <staff>1</staff>
    <notations>
     <slur color="#000000" type="{slur_type}" orientation="over" />
    </notations>
   </note>
  </measure>
"""
        output.append(measure_xml)

print(''.join(output))

