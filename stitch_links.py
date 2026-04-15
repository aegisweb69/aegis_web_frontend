import os
import re

directory = "a:/Aegis_website"
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

# We'll run a few basic string replacements
# Looking for >Features</a> and replacing its preceding href="#"
replacements = {
    r'href="#"([^>]*)>Features</a>': r'href="technology.html"\1>Features</a>',
    r'href="#"([^>]*)>Solutions</a>': r'href="solutions.html"\1>Solutions</a>',
    r'href="#"([^>]*)>Compliance</a>': r'href="solutions.html"\1>Compliance</a>',
    r'href="#"([^>]*)>Pricing</a>': r'href="pricing.html"\1>Pricing</a>',
    # Also Home/Logo
    r'href="#"([^>]*)><span class="font-manrope[^>]*>Aegis</span>': r'href="index.html"\1><span class="font-manrope font-extrabold text-2xl tracking-tighter text-primary">Aegis</span>',
}

for fname in html_files:
    path = os.path.join(directory, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    for pattern, repl in replacements.items():
        content = re.sub(pattern, repl, content)

    # for logo, simpler approach:
    content = re.sub(r'href="#"([^>]*)>\s*<span class="font-manrope', r'href="index.html"\1><span class="font-manrope', content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Links updated.")
