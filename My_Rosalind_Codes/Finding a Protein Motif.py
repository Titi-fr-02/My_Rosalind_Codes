import requests
import re

file_path = input("Enter the file path: ").replace('"', '')

with open(file_path, 'r') as source:
    proteins_ID = source.read().splitlines()

ID_pattern_6 = r'[A-Z][0-9][A-Z0-9]{3}[0-9]'
ID_pattern_10 = r'[A-NR-Z][0-9][A-Z][A-Z0-9]{2}[0-9][A-Z][A-Z0-9]{2}[0-9]'
Glyco_pattern = r'N[^P][ST][^P]'

ID_dict = {}

for i in proteins_ID:
    matches_6 = re.search(ID_pattern_6, i)
    matches_10 = re.search(ID_pattern_10, i)
    if matches_6:
        clean_id = matches_6.group()
        ID_dict[i] = clean_id
    elif matches_10:
        clean_id = matches_10.group()
        ID_dict[i] = clean_id

for key, id_list in ID_dict.items():
    positions = []
    url = f"https://rest.uniprot.org/uniprotkb/{id_list}.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "sequence" in data and "value" in data["sequence"]:
            sequence = data["sequence"]["value"]
            for i in range(len(sequence) - 3):
                quadruplet = sequence[i:i + 4]
                if re.match(r'N[^P][ST][^P]', quadruplet):
                    positions.append(i + 1)
        if positions:
            position_str = ' '.join(str(pos) for pos in positions)
            print(key); print(position_str)
        else:
            pass
    else:
        print("Failed to retrieve data:", response.status_code)