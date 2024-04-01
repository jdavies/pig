# svg.py
#
# A module to create SVG files
import os

class svg:
    """A class for creating SVG files"""

    header_template = [
        '<?xml version="1.0" encoding="UTF-8" standalone="no"?>',
        '<!-- Created with Inkscape (http://www.inkscape.org/) -->',
        '',
        '<svg',
        '   width="4096"',
        '   height="4096"',
        '   viewBox="0 0 4096 4096"',
        '   version="1.1"',
        '   id="svg1"'
        '   inkscape:version="1.3.2 (091e20e, 2023-11-25, custom)"',
        '   sodipodi:docname="cannister_type_a_ids.svg"',
        '   inkscape:export-filename=".\crate_id_UC_1_white_4K.png"'
        '   inkscape:export-xdpi="96"'
        '   inkscape:export-ydpi="96"'
        '   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"',
        '   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"',
        '   xmlns="http://www.w3.org/2000/svg"',
        '   xmlns:svg="http://www.w3.org/2000/svg"',
        '   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"',
        '   xmlns:cc="http://creativecommons.org/ns#"',
        '   xmlns:dc="http://purl.org/dc/elements/1.1/">',
        '   <title id="title1">Cybernautic Studios 4K Texture</title>',
        '   <sodipodi:namedview',
        '       id="namedview1"',
        '       pagecolor="#505050"',
        '       bordercolor="#eeeeee"',
        '       borderopacity="1" inkscape:showpageshadow="0"',
        '       inkscape:pageopacity="0" inkscape:pagecheckerboard="0"',
        '       inkscape:deskcolor="#505050" inkscape:document-units="mm"',
        '       inkscape:zoom="0.10578743"',
        '       inkscape:cx="8190.9539" inkscape:cy="2443.5794"',
        '       inkscape:current-layer="layer1" shape-rendering="crispEdges">'
    ]

    groupInfo = '   </sodipodi:namedview>\n   <defs id="defs1" />\n   <g inkscape:label="Pages" inkscape:groupmode="layer" id="pages1">\n'

    def __init__(self, filename):
        print("in the svg constructor!")
        self.file = open(filename, 'w')
        self.__write_header__()

    def __write_header__(self):
        for line in self.header_template:
            self.file.write(line + "\n")

    # pageNum: int  A value from >= 0
    # id: str       The string ID of the crate
    # title: str    The string title of the ID (ie T_DECAL)
    def createPage(self, pageNum, id, title):
        pageResolution = 4096

        # 5 pages per line
        pagesPerLine = 5
        pageLoc_X = (pageNum % pagesPerLine) * pageResolution + (pageNum % pagesPerLine)
        pageLoc_Y = int(pageNum / pagesPerLine) * pageResolution

        pageID = "page{}".format(pageNum+1)
        label = "{}_{}".format(title, pageNum+1)
        self.file.write('   <inkscape:page x="{x}" y="{y}" width="{res}" height="{res}"'.format(x = pageLoc_X, y= pageLoc_Y, res=pageResolution) + "\n")
        self.file.write('       id="' + pageID + "\"\n")
        self.file.write('       margin="0" bleed="0"' + "\n")
        self.file.write('       inkscape:label="' + label + "\"/>\n")

        # Update the group info
        self.groupInfo += '      <g inkscape:label="Page_{}"'.format(pageNum+1)
        self.groupInfo += ' id="page_{}"\n'.format(pageNum+1)
        self.groupInfo += '      transform="translate(150,1000)" style="fill:#ffffff">\n'
        self.groupInfo += '        <text\n'
        self.groupInfo += '          xml:space="preserve"\n'
        self.groupInfo += '          style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:150px;font-family:\'Arial\';-inkscape-font-specification:\'Arial, Normal\';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal;display:inline;fill:#ffffff;stroke:#ffffff;stroke-width:0;stroke-linejoin:round"\n'
        self.groupInfo += '          x="{}" '.format(pageLoc_X + 2)
        self.groupInfo += 'y="{}"\n'.format(pageLoc_Y + 6)
        self.groupInfo += '          id="text{}"\n'.format(pageNum+1)
        self.groupInfo += '          inkscape:label="ID{}">'.format(pageNum+1)
        self.groupInfo += '<tspan sodipodi:role="line" id="tspan{}"'.format(pageNum+1)
        # self.groupInfo += '             x="{}" '.format(pageLoc_X + 10)
        # self.groupInfo += 'y="{}">{}</tspan></text>\n</g>\n'.format(pageLoc_Y + 10, id)
        self.groupInfo += '>{}</tspan></text>\n      </g>\n'.format(id)


    def __write_group_info__(self):
        self.file.write(self.groupInfo)
        self.file.write('   </g>\n')

    def __write_metadata__(self):
        metadata = [
            '   <metadata id="metadata1">',
            '       <rdf:RDF>',
            '           <cc:Work rdf:about="">',
            '               <dc:title>Cybernautic Studios 4K Texture</dc:title>',
            '               <dc:creator>',
            '                   <cc:Agent>',
            '                       <dc:title>Jeff Davies - Cybernautic Studios</dc:title>',
            '                   </cc:Agent>',
            '               </dc:creator>',
            '               <dc:rights>',
            '                   <cc:Agent>',
            '                       <dc:title>All Rights Reserved - Jeff Davies</dc:title>',
            '                   </cc:Agent>',
            '               </dc:rights>',
            '           </cc:Work>',
            '       </rdf:RDF>',
            '   </metadata>'
        ]
        for line in metadata:
            self.file.write(line + "\n")

    def close(self):
        self.__write_group_info__()
        self.__write_metadata__()
        self.file.close

