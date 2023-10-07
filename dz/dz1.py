import colorama

# Список стилей колорама
available_styles = colorama.Style.__dict__.keys()
print("Available styles:", available_styles)

# Список цветов текста
available_text_colors = colorama.Fore.__dict__.keys()
print("Available text colors:", available_text_colors)

# Список задних фонов
available_background_colors = colorama.Back.__dict__.keys()
print("Available background colors:", available_background_colors)