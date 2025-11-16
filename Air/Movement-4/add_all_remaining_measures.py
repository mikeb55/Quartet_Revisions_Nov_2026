#!/usr/bin/env python3
"""
Add all remaining measures (9-90 for Violin I, 6-90 for Violin II, 5-90 for Viola, 5-90 for Cello)
as whole rest placeholders, then file can be filled with actual musical content
"""

def generate_whole_rest_measure(measure_num, part_id, instrument_id, width=217):
    """Generate a measure with a whole rest"""
    xml = []
    xml.append(f'  <!--============== Part: {part_id}, Measure: {measure_num} ==============-->')
    xml.append(f'  <measure number="{measure_num}" width="{width}">')
    xml.append('   <note default-x="15">')
    xml.append('    <rest />')
    xml.append('    <duration>1024</duration>')
    xml.append(f'    <instrument id="{instrument_id}" />')
    xml.append('    <voice>1</voice>')
    xml.append('    <type>whole</type>')
    xml.append('    <staff>1</staff>')
    xml.append('   </note>')
    if measure_num == 90:
        xml.append('   <barline>')
        xml.append('    <bar-style>light-heavy</bar-style>')
        xml.append('   </barline>')
    xml.append('  </measure>')
    return '\n'.join(xml)

# Generate all remaining measures
violin1_measures = []
for m in range(9, 91):
    violin1_measures.append(generate_whole_rest_measure(m, "P1", "P1-I1"))

violin2_measures = []
for m in range(6, 91):
    violin2_measures.append(generate_whole_rest_measure(m, "P2", "P2-I1"))

viola_measures = []
for m in range(5, 91):
    viola_measures.append(generate_whole_rest_measure(m, "P3", "P3-I1"))

cello_measures = []
for m in range(5, 91):
    cello_measures.append(generate_whole_rest_measure(m, "P4", "P4-I1"))

# Write to file
with open('remaining_measures_placeholders.txt', 'w', encoding='utf-8') as f:
    f.write("<!-- VIOLIN I Measures 9-90 -->\n")
    f.write('\n'.join(violin1_measures))
    f.write("\n\n<!-- VIOLIN II Measures 6-90 -->\n")
    f.write('\n'.join(violin2_measures))
    f.write("\n\n<!-- VIOLA Measures 5-90 -->\n")
    f.write('\n'.join(viola_measures))
    f.write("\n\n<!-- CELLO Measures 5-90 -->\n")
    f.write('\n'.join(cello_measures))

print("Generated remaining_measures_placeholders.txt")
print("This contains XML for all remaining measures as whole rest placeholders")
print("Total measures generated:")
print(f"  Violin I: 82 measures (9-90)")
print(f"  Violin II: 85 measures (6-90)")
print(f"  Viola: 86 measures (5-90)")
print(f"  Cello: 86 measures (5-90)")
print("These can be inserted into the MusicXML file, then replaced with actual musical content")

