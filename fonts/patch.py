#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import sys

def copy_attributes(source, target_file, id_range_start, id_range_end, new_id_range_start):
    root = source.getroot()
    
    chars_element = root.find('chars')
    
    for char_element in chars_element.findall('char'):
        char_id = int(char_element.get('id'))
        
        if not (id_range_start <= char_id <= id_range_end):
            continue
        
        target_char_id = char_id - id_range_start + new_id_range_start
        target_char_element = chars_element.find(f'char[@id="{target_char_id}"]')
        
        if target_char_element is None:
            continue
        
        for attr, value in char_element.attrib.items():
            if attr == 'id':
                continue
            target_char_element.set(attr, value)

    tree = ET.ElementTree(root)
    tree.write(target_file, xml_declaration=True)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("You should provide the arguments: source_file, target_file")
        exit(1)

    source_file = sys.argv[1]
    target_file = sys.argv[2]

    # Parse the source XML file
    source_tree = ET.parse(source_file)

    # Copy attributes from Latin range (65-90) to new range (97-122)
    copy_attributes(source_tree, target_file, 65, 90, 97)

    # Copy attributes from Latin-1 Supplement & Latin Extended A range (192-214, 216-222, 338, 352, 376)
    # to new range (224-246, 248-254, 339, 353, 255)
    copy_attributes(source_tree, target_file, 192, 214, 224)
    copy_attributes(source_tree, target_file, 216, 222, 248)
    copy_attributes(source_tree, target_file, 338, 338, 339)
    copy_attributes(source_tree, target_file, 352, 352, 353)
    copy_attributes(source_tree, target_file, 376, 376, 255)

    # Copy attributes from Cyrillic range (1024-1039, 1040-1071) to new range (1104-1119, 1072-1103)
    copy_attributes(source_tree, target_file, 1024, 1039, 1104)
    copy_attributes(source_tree, target_file, 1040, 1071, 1072)
