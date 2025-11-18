import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def print_summary(animals):
  for animal in animals:
    name = animal.get("name")
    if name:
      print(f"Name: {name}")

    characteristics = animal.get("characteristics") or {}
    diet = characteristics.get("diet")
    if diet:
      print(f"Diet: {diet}")

    locations = animal.get("locations") or []
    if isinstance(locations, list) and len(locations) > 0:
      first_location = locations[0]
      if first_location:
        print(f"Location: {first_location}")

    type_value = characteristics.get("type")
    if type_value:
      print(f"Type: {type_value}")

    print()


def main():
  try:
    # Use a simple relative filename to keep things straightforward
    animals_data = load_data('animals_data.json')
  except Exception as e:
    print(f"Error loading data: {e}")
    return

  print_summary(animals_data)


if __name__ == "__main__":
  main()