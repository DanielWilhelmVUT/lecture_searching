from pathlib import Path
import json

file_name = "sequential.json"


#ukol1
def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            reader = json.load(f)
        if field in reader.keys():
            return reader[field]
        else:
            print(f"klic neexistuje: {field}")
            return None

    except FileNotFoundError:
        print(f"nenasel jsem soubor: {file_name}")
        return None

    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name

#ukol2
def linear_search(sequence, hledane_cislo):
    """
    funkce projde seznam prvek po prvku a zapise si kazdy index
    kde nasla hledane cislo do prazdeneho seznamu. Nakonec vrati seznam techto indexu a jejich celkovy pocet.
    """

    indexy = []

    for i in range(len(sequence)):
        if sequence[i] == hledane_cislo:
            indexy.append(i)

    vysledek = {
        "positions": indexy,
        "count": len(indexy)}

    return vysledek

#ukol3
def binary_search(sequence, hledane_cislo):
    leva = 0
    prava = len(sequence) - 1

    while leva <= prava:
        stred = (leva + prava) // 2

        if sequence[stred] == hledane_cislo:
            return stred
        elif sequence[stred] < hledane_cislo:
            leva = stred + 1
        else:
            prava = stred - 1
    return None

def main():
    json_filename = "sequential.json"
    sequential_dataset = read_data(json_filename, "unordered_numbers")
    print(sequential_dataset)

    vysledek = read_data(json_filename, "klic_ktery_neexistuje")
    print(f"testik pro neplatny klic: {vysledek}")

    if sequential_dataset:
        moje_cislo = 9
        vystup = linear_search(sequential_dataset, moje_cislo)

        print(f"tohle cislo jsem hledal: {moje_cislo}")
        print(f"nasel jsem ho na indexu: {vystup['positions']}")
        print(f"tolikrát tam bylo: {vystup['count']}")

    serazena_data = read_data(json_filename, "ordered_numbers")
    if serazena_data:
        hledane_cislo = 120
        index = binary_search(serazena_data, hledane_cislo)
        print(serazena_data)
        if index is not None:
            print(f"cislo: {hledane_cislo} je na indexu: {index}")
        else:
            print(f"cislo: {hledane_cislo} v seznamu neni")

if __name__ == "__main__":
    main()
