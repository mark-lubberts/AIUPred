from collections import defaultdict
from pathlib import Path

def multifasta_reader(fasta_path):
    """
    (multi) FASTA reader function
    :return: Dictionary with header -> sequence mapping from the file
    """
    try:
        fasta = Path(fasta_path)
        if not fasta.is_file()
            raise ValueError(f"{fasta_path} is not a file")
    except TypeError:
        raise FileNotFoundError(f"Cannot create a valid file path from {fasta_path}")
        
    sequence_dct = defaultdict(str)
    header = None
    with fasta.open("r") as file_handle:
        for line in file_handle:
            line = line.strip()
            if line.startswith('>'):
                header = line
            elif line:
                sequence_dct[header] += line.upper()

    # convert to a regular dictionary before returning
    # This prevents unforseen consequences when trying to retrieve sequences later
    return dict(sequence_dct)
