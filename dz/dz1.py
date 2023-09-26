import colorama


available_styles = colorama.Style.__dict__.keys()
print("Available styles:", available_styles)

available_text_colors = colorama.Fore.__dict__.keys()
print("Available text colors:", available_text_colors)

available_background_colors = colorama.Back.__dict__.keys()
print("Available background colors:", available_background_colors)