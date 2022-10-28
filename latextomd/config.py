DEFAULT_OPTIONS = {"remove_comments": True, "strip_lines": True}

# Replace without regex
replace_simple = [
    ["\\ds\\", "\\displaystyle\\"],
    ["$\\C$", "\\mathcal{C}"],
    ["\\e^", "\\text{e}^"],
    ["\\mathscr", "\\mathcal"],
    # ["\\[", "$$"],
    # ["\\]", "$$"],
    ["\n$$", "\n$$\n"],
    ["$$\n", "\n$$\n"],
    ["\\begin", "\n\\begin"],
    ["\\begin{center}", ""],
    ["\\end{center}", ""],
    ["\\begin{solution}", ":::startsolution\n"],
    ["\\end{solution}", "\n\n:::endsolution"],
]


# Deleted with TexSoup
# Example: \vspace{1cm} -> ""
del_commands = [
    "vspace",
    "Bareme",
    "cornouaille",
    "renewcommand",
    "setbar",
    "esp",
    "encadre",
    "ref",
    "arraycolsep",
    "label",
    "renewcommand",
    "hspace",
    "parindent",
    "raisebox",
    "rhead",
    "lhead",
    "lfoot",
    "rfoot",
    "addtolength",
    "pagestyle",
    "thispagestyle",
    "marginpar",
    "newpage",
    "hfill",
    "medskip",
    "bigskip",
    "smallskip",
    "setlength",
    "decofourleft",
    "footrulewidth",
    "decofourright",
]

del_environnements = [r"\begin{center}", r"\end{center}"]

del_blocks = ["center"]

replace_commands = [
    # ["chapter", "# S_T_R"],
    # ["section", "## S_T_R"],
    # ["subsection", "### S_T_R"],
    # ["textbf", "**S_T_R**"],
    # ["textsc", "S_T_R"],
    # ["emph", "_S_T_R_"],
    ["psframebox", "S_T_R"],
]

# template mkdocs

fake_admonition = {"latex_name": "definition", "type": "tip", "texte": "Défintion"}


def template_mkdocs(admonition: dict):
    admonition = f"""\n!!!tip "{admonition["texte"]} """ + r'\2"\n\n'
    end = r"\\end{" + admonition["latex_name"] + "}"


# admonitions

admonitions_mkdocs = [
    # definition
    [
        r"\\begin\{definition\}(\[(?P<block_title>.*?)\])?",
        """\n!!!tip "Définition """ + r'\2"\n\n',
    ],
    [r"\\end{definition}", "\n\n:::"],
    # definitions
    [
        r"\\begin\{definitions\}(\[(?P<block_title>.*?)\])?",
        """\n!!!tip "Définitions """ + r'\2"\n\n',
    ],
    [r"\\end{definitions}", "\n\n:::"],
    # exemple
    [
        r"\\begin\{exemple\}(\[(?P<block_title>.*?)\])?",
        """\n!!!example "Exemple """ + r'\2"\n\n',
    ],
    [r"\\end{exemple}", "\n\n:::"],
    # exemples
    [
        r"\\begin\{exemples\}(\[(?P<block_title>.*?)\])?",
        """\n!!!example "Exemples """ + r'\2"\n\n',
    ],
    [r"\\end{exemples}", "\n\n:::"],
    # remarque
    [
        r"\\begin\{remarque\}(\[(?P<block_title>.*?)\])?",
        """\n!!!note "Remarque """ + r'\2"\n\n',
    ],
    [r"\\end{remarque}", "\n\n:::"],
    # remarques
    [
        r"\\begin\{remarques\}(\[(?P<block_title>.*?)\])?",
        """\n!!!note "Remarques """ + r'\2"\n\n',
    ],
    [r"\\end{remarques}", "\n\n:::"],
    # propriete
    [
        r"\\begin\{propriete\}(\[(?P<block_title>.*?)\])?",
        """\n!!!tip "Propriété """ + r'\2"\n\n',
    ],
    [r"\\end{propriete}", "\n\n:::"],
    # proprietes
    [
        r"\\begin\{proprietes\}(\[(?P<block_title>.*?)\])?",
        """\n!!!tip "Propriétés """ + r'\2"\n\n',
    ],
    [r"\\end{proprietes}", "\n\n:::"],
    # theoreme
    [
        r"\\begin\{theoreme\}(\[(?P<block_title>.*?)\])?",
        """\n!!!tip "Théorème """ + r'\2"\n\n',
    ],
    [r"\\end{theoreme}", "\n\n:::"],
    # theorem
    [
        r"\\begin\{theorem\}(\[(?P<block_title>.*?)\])?",
        """\n!!!tip "Theorem """ + r'\2"\n\n',
    ],
    [r"\\end{theorem}", "\n\n:::"],
    # methode
    [
        r"\\begin\{methode\}(\[(?P<block_title>.*?)\])?",
        """\n!!!faq "Méthode """ + r'\2"\n\n',
    ],
    [r"\\end{methode}", "\n\n:::"],
]

admonitions_docusaurus = [
    [
        r"\\begin\{definition\}(\[(?P<block_title>.*?)\])?",
        r"\n:::tip Définition: \2\n\n",
    ],
    [r"\\end{definition}", "\n\n:::"],
    [
        r"\\begin\{definitions\}(\[(?P<block_title>.*?)\])?",
        r"\n:::tip Définitions: \2\n\n",
    ],
    [r"\\end{definitions}", "\n\n:::"],
    [
        r"\\begin\{propriete\}(\[(?P<block_title>.*?)\])?",
        r"\n:::tip Propriété: \2\n\n",
    ],
    [r"\\end{propriete}", "\n\n:::"],
    [
        r"\\begin\{proprietes\}(\[(?P<block_title>.*?)\])?",
        r"\n:::tip Propriétés: \2\n\n",
    ],
    [r"\\end{proprietes}", "\n\n:::"],
    # theoreme
    [
        r"\\begin\{theoreme\}(\[(?P<block_title>.*?)\])?",
        r"\n:::tip Théorème: \2\n\n",
    ],
    [r"\\end{theoreme}", "\n\n:::"],
    # theorem
    [
        r"\\begin\{theorem\}(\[(?P<block_title>.*?)\])?",
        r"\n:::tip Theorem: \2\n\n",
    ],
    [r"\\end{theorem}", "\n\n:::"],
    [
        r"\\begin\{exemple\}(\[(?P<block_title>.*?)\])?",
        r"\n:::note Exemple: \2\n\n",
    ],
    [r"\\end{exemple}", "\n\n:::"],
    [
        r"\\begin\{remarques\}(\[(?P<block_title>.*?)\])?",
        r"\n:::note Remarques: \2\n\n",
    ],
    [r"\\end{remarques}", "\n\n:::"],
    [
        r"\\begin\{remarque\}(\[(?P<block_title>.*?)\])?",
        r"\n:::note Remarque: \2\n\n",
    ],
    [r"\\end{remarque}", "\n\n:::"],
    [
        r"\\begin\{preuve\}(\[(?P<block_title>.*?)\])?",
        r"\n:::note Preuve: \2\n\n",
    ],
    [r"\\end{preuve}", "\n\n:::"],
    [
        r"\\begin\{methode\}(\[(?P<block_title>.*?)\])?",
        r"\n:::warning Méthode: \2\n\n",
    ],
    [r"\\end{methode}", "\n\n:::"],
]


clean_quote = [r'\\"', '"']

blocks = [
    [r"\\begin\{multicols\}\{((?P<arg>.*?))\}", ""],
    [r"\\end{multicols}", ""],
    [r"\\begin\{minipage\}\{((?P<arg>.*?))\}", ""],
    [r"\\end{minipage}", ""],
    [r"\\begin\{colitemize\}\{((?P<arg>.*?))\}", r"\\begin{itemize}"],
    [r"\\end{colitemize}", r"\\end{itemize}"],
]


math_sub = [
    [r"\\np\{((?P<arg>.*?))\}", r"\1"],
    [r"\\nombre\{((?P<arg>.*?))\}", r"\1"],
    # [r"\\section\{((?P<arg>.*?))\}", r':::section \1'],
    [r"\\textsf\{((?P<arg>.*?))\}", r"\1"],
    [r"\\Large(\{(?P<arg>.*?)\})?", r"\1"],
    [r"\\parbox\{((?P<arg>.*?))\}", ""],
    [r"\\end\{((?P<arg>.*?))\}", r"\\end{\1}\n"],
    [r"\\Oijk", r"$\\left(\\text{O};~\\vect{i},~\\vect{j},~\\vect{k}\\right)$"],
    [r"\\Ouv", r"$\\left(\\text{O};~\\vect{u},~\\vect{v}\\right)$"],
    [r"\\Oij", r"$\\left(\\text{O};~\\vect{i},~\\vect{j}\\right)$"],
    [r"\\vect\{((?P<arg>.*?))\}", r"\\overrightarrow{\1}"],
    [r"\\e(\W)", r"\1"],
]


postpandoc = [
    [r"\\textsf\{((?P<arg>.*?))\}", r"\1"],
    [r"\\Large(\{(?P<arg>.*?)\})?", r"\1"],
    [r"\\parbox\{((?P<arg>.*?))\}", ""],
    [r"\\parindent\{((?P<arg>.*?))\}", ""],
    [r"\\hspace\{((?P<arg>.*?))\}", ""],
    [r"\\pagestyle\{((?P<arg>.*?))\}", ""],
    [r"\\thispagestyle\{((?P<arg>.*?))\}", ""],
    [r"\\enlargethispage\{((?P<arg>.*?))\}", ""],
    [r"\\vspace\{((?P<arg>.*?))\}", ""],
    [r"\\end\{((?P<arg>.*?))\}", r"\\end{\1}\n"],
    [r"\\Oijk", r"$\\left(\\text{O};~\\vect{i},~\\vect{j},~\\vect{k}\\right)$"],
    [r"\\Ouv", r"$\\left(\\text{O};~\\vect{u},~\\vect{v}\\right)$"],
    [r"\\Oij", r"$\\left(\\text{O};~\\vect{i},~\\vect{j}\\right)$"],
    [r"\\vect\{((?P<arg>.*?))\}", r"\\overrightarrow{\1}"],
    [r"\\rbrace", r"\\}"],
    [r"\\strut", ""],
    [r"\\quad", ""],
    [r"\\setlength", ""],
    [r"\\e(\W)", r"\1"],
    [r"\\psframebox\[.*\]", ""],
    [r"\\ldotcarreaux\[.*\]", ""],
    [r"\\bigskip", ""],
    [r"\\smallskip", ""],
    [r"\\medskip", ""],
    [r"\\hfill", ""],
    # [r"\\label\{.*\}", ""],
    [r"\\hypertarget\{.*\}", ""],
    [r'\\"', '"']
    # [r"\\fexo\{((?P<arg>.*?))\}\{((?P<arg>.*?))\}\{((?P<arg>.*?))\}", r"\1\n\2\n\3"],
]
