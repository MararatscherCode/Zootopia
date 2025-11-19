import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def safe_summary(animals):
  output = ''
  for animal in animals:
    name = animal.get("name")
    if name:
      output += f"Name: {name}\n"

    characteristics = animal.get("characteristics") or {}
    diet = characteristics.get("diet")
    if diet:
      output += f"Diet: {diet}\n"

    locations = animal.get("locations") or []
    if isinstance(locations, list) and len(locations) > 0:
      first_location = locations[0]
      if first_location:
        output += f"Location: {first_location}\n"
        

    type_value = characteristics.get("type")
    if type_value:
      output += f"Type: {type_value}\n"
    output += "\n"
  return output


def main():
  try:
    animals_data = load_data('animals_data.json')
  except Exception as e:
    print(f"Error loading data: {e}")
    return

  summary = safe_summary(animals_data)
  tpl_path = 'animals_template.html'
  try:
    with open(tpl_path, 'r', encoding='utf-8') as f:
      tpl = f.read()
  except Exception as e:
    print(f"Error reading template {tpl_path}: {e}")
    return


  output_path = 'animals_template.html'
  filled = tpl.replace('__REPLACE_ANIMALS_INFO__', f"{summary}")
  try:
    with open(output_path, 'w', encoding='utf-8') as f:
      f.write(filled)
    print(f"Generated {output_path} (template preserved as {tpl_path})")
  except Exception as e:
    print(f"Error writing output {output_path}: {e}")

if __name__ == "__main__":
  main()