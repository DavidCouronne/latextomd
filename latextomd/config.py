DEFAULT_OPTIONS = {
    'remove_comments': True,
    'strip_lines': True
}


# Deleted with TexSoup
del_commands = ['vspace',
                'Bareme',
                'cornouaille',
                'renewcommand',
                'setbar',
                'esp',
                'encadre',
                'ref',
                'arraycolsep',
                'label',
                'renewcommand',
                'hspace',
                'parindent',
                'raisebox',
                'rhead',
                'lhead',
                'lfoot',
                'rfoot',
                'addtolength',
                'pagestyle',
                'thispagestyle',
                'marginpar',
                'newpage',
                'hfill',
                'medskip',
                'bigskip',
                'smallskip',
                'setlength',
                # 'Large',
                'large',
                'decofourleft',
                'footrulewidth',
                'decofourright'
                ]

del_environnements = [r'\begin{center}', r'\end{center}']

del_blocks =['center']