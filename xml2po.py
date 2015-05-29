#!/usr/bin/python
"""
    xml2po
    Copyright (C) 2015 tknorris

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import xml.etree.ElementTree as ET
import sys

def get_translations(trans_xml):
    translations = {}
    tree = ET.parse(trans_xml)
    root = tree.getroot()
    for string in root:
        translations[string.attrib['id']] = string.text
    return translations

def main(argv=None):
    if sys.argv: argv = sys.argv
    
    out_file = 'strings.po'
    lang = 'en'
    if len(argv) > 2:
        in_file = argv[2]
        if len(argv) > 3:
            lang = argv[3]
            if len(argv) > 4:
                out_file = argv[4]
    else:
        print 'need english xml'

    eng_file = argv[1]
    trans = get_translations(in_file)
    
    print 'Converting: %s to %s (in %s) using %s as english reference' % (in_file, out_file, lang, eng_file)
    tree = ET.parse(eng_file)
    root = tree.getroot()
    with open(out_file, 'w') as f:
        f.write('msgid ""\n')
        f.write('msgstr ""\n')
        f.write('"Project-Id-Version: TV Addons Addons\\n"\n')
        f.write('"POT-Creation-Date: YEAR-MO-DA HO:MI+ZONE\\n"\n')
        f.write('"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n"\n')
        f.write('"Language-Team: \\n"\n')
        f.write('"MIME-Version: 1.0\\n"\n')
        f.write('"Content-Type: text/plain; charset=UTF-8\\n"\n')
        f.write('"Content-Transfer-Encoding: 8bit\\n"\n')
        f.write('"Language: %s\\n"\n' % (lang))
        f.write('"Plural-Forms: nplurals=2; plural=(n != 1);\\n"\n\n')
        for string in root:
            msgctxt = string.attrib['id']
            msgid = string.text
            if msgid is None: msgid = ''
            if eng_file == in_file:
                translation = ''
            else:
                if msgctxt in trans:
                    if trans[msgctxt] is None:
                        translation = ''
                    else:
                        translation = trans[msgctxt]
                else:
                    continue  # skip untranslated entries

            #print '%s - %s --> %s' % (msgctxt, msgid, translation)
            f.write('msgctxt "#%s"\n' % (msgctxt))
            f.write('msgid "%s"\n' % (msgid))
            f.write('msgstr "%s"\n\n' % (translation.encode('utf-8')))
        

if __name__ == '__main__':
    sys.exit(main())
