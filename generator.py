import os

# Ordnerpfad zu den Bildern
image_folder = "images/theatergruppe/flugzettelbilder"

# Zielordner für die HTML-Datei
output_file = "theaterbilder.html"

# Alle Dateien im Ordner auflisten
files = os.listdir(image_folder)

# Filter für JPG und JPEG Dateien
jpg_files = [f for f in files if f.lower().endswith(('.jpg', '.JPG'))]

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
                {actor_link}
            </div>
        </div>
    </li>"""

# HTML-Code für die Einträge generieren
html_items = []
for year in sorted_years:
    main_image = years[year]["main"]
    p_image = years[year]["P"]

    actor_link = f'<a href="images/theatergruppe/flugzettelbilder/{p_image}" target="_blank" class="btn btn-link text-dark-gray text-decoration-line-bottom">Schauspieler</a>' if p_image else ""

    if main_image:  # Nur Jahre mit einem Hauptbild einfügen
        html_items.append(list_item_template.format(main_image=main_image, year=year, actor_link=actor_link))

# Zusammenfügen und HTML-Datei speichern
html_output = html_template.format(items="\n".join(html_items))

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_output)

print(f"HTML-Datei wurde erfolgreich erstellt: {output_file}")
