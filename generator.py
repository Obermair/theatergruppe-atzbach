import os

# Ordnerpfad zu den Bildern
image_folder = "images/theatergruppe/flugzettelbilder"

# Zielordner für die HTML-Datei
output_file = "theaterbilder.html"

# Zuordnung der Jahreszahlen zu den Theaterstücknamen
theater_pieces = {
    "1967": ["Die Sternhoferbuam auf Brautschau", "Heimatglocken"],
    "1968": ["Die zwei Neidhammeln"],
    "1970": ["Ehestand und Wehestand"],
    "1971": ["Hirtenspiel"],
    "1972": ["Das große Heimweh"],
    "1973": ["Das Heiratsgenie"],
    "1975": ["Versöhnung am Hubertushof"],
    "1976": ["Die Junggesellensteuer"],
    "1977": ["Der Vagabund"],
    "1978": ["Lipperl auf Brautschau"],
    "1979": ["Das Trauringl"],
    "1980": ["Die lieben Verwandten"],
    "1981": ["Der verflixte Hexenschuss"],
    "1982": ["Der Tonfilmbauer"],
    "1983": ["Das Geheimnis der Waldmühle"],
    "1984": ["Die zwoa Spätzünder"],
    "1985": ["Der Schwur an der Waldkapelle"],
    "1986": ["Wirbelwind ums Findelkind"],
    "1987": ["Kurbetrieb beim Kräuterblasi"],
    "1988": ["Der Millionenstadl"],
    "1989": ["S'Abendglöckerl"],
    "1990": ["S'Listige Ahndl"],
    "1991": ["Der eigene Richter"],
    "1992": ["Null Problem"],
    "1993": ["Sei doch net so dumm"],
    "1994": ["Wenn des bloß guat geht"],
    "1995": ["Der Sandler"],
    "1996": ["Der Dumme hat's Glück"],
    "1997": ["Ehefrau wider Willen"],
    "1998": ["Der Mustergatte"],
    "1999": ["c'est la vie - So ist das Leben"],
    "2000": ["Der Unverbesserliche"],
    "2001": ["Das verflixte Klassentreffen"],
    "2002": ["Die Millionentante"],
    "2003": ["Power Paula"],
    "2004": ["Diamanten im Stroh"],
    "2005": ["Der verhängnisvolle Firmtag"],
    "2006": ["Psychostress und Leberwurst"],
    "2007": ["Liebe, Geld und Altpapier"],
    "2008": ["Das Erbe der Väter"],
    "2009": ["Mit Vollgas ins Glück"],
    "2010": ["Tante Klara"],
    "2011": ["Lustiges Bezirksgericht"],
    "2012": ["Der verkaufte Großvater"],
    "2013": ["Der Finderlohn"],
    "2014": ["Die Hausmeisterin"],
    "2015": ["Woher kommt die Million?"],
    "2016": ["Besenbinder Beppi"],
    "2017": ["Onkel Hubbi wird’s schon richten!"],
    "2018": ["Da Himme wart net"],
    "2019": ["Explosive Landwirtschaft"],
    "2020": ["ausgefallen"],
    "2021": ["ausgefallen"],
    "2022": ["ausgefallen"],
    "2023": ["ausgefallen"],
    "2024": ["Bäckermeister und Schnitzelkönig"]
}

# Alle Dateien im Ordner auflisten
files = os.listdir(image_folder)

# Filter für JPG und JPEG Dateien
jpg_files = [f for f in files if f.lower().endswith(('.jpg', '.JPG', '.png', '.PNG'))]

# Jahreszahlen extrahieren und sortieren
years = {}
for file in jpg_files:
    # Entferne die Dateiendung
    name, ext = os.path.splitext(file)
    
    # Überprüfen, ob die Datei ein "P" für Schauspieler enthält
    if name.endswith("P"):
        year = name[:-1]  # Entferne das "P"
        years[year] = years.get(year, {"main": None, "P": None})
        years[year]["P"] = file
    else:
        year = name
        years[year] = years.get(year, {"main": None, "P": None})
        years[year]["main"] = file

# Sortiere die Jahre absteigend
sorted_years = sorted(years.keys(), reverse=True)

# HTML-Vorlage
html_template = """<ul>
{items}
</ul>"""

list_item_template = """
    <li class=\"grid-item\">
        <div class=\"card border-0 border-radius-4px box-shadow-medium box-shadow-extra-large-hover\">
            <div class=\"blog-image\">
                <a href=\"images/theatergruppe/flugzettelbilder/{main_image}\" target=\"_blank\" class=\"d-block\"><img src=\"images/theatergruppe/flugzettelbilder/{main_image}\" alt=\"\" /></a>
            </div>
            <div class=\"card-body p-13 md-p-11\">
                <p class=\"card-title mb-15px alt-font fw-600 fs-20 text-dark-gray d-inline-block\">Theaterstück {year}</p>
                <p class=\"card-subtitle mb-15px alt-font fs-16 text-gray d-inline-block\">{titles}</p>
                {actor_link}
            </div>
        </div>
    </li>"""

# HTML-Code für die Einträge generieren
html_items = []
for year in sorted_years:
    main_image = years[year]["main"]
    p_image = years[year]["P"]
    titles = "<br/>".join(theater_pieces.get(year, ["Titel unbekannt"]))

    actor_link = f'<a href="images/theatergruppe/flugzettelbilder/{p_image}" target="_blank" class="btn btn-link text-dark-gray text-decoration-line-bottom">Schauspieler</a>' if p_image else ""

    if main_image:  # Nur Jahre mit einem Hauptbild einfügen
        html_items.append(list_item_template.format(main_image=main_image, year=year, titles=titles, actor_link=actor_link))

# Zusammenfügen und HTML-Datei speichern
html_output = html_template.format(items="\n".join(html_items))

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_output)

print(f"HTML-Datei wurde erfolgreich erstellt: {output_file}")