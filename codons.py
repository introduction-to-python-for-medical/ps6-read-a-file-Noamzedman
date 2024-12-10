def create_codon_dict(file_path):
    d = {}
    with open(file_path, 'r') as file:  # פתיחה בטוחה של הקובץ
        rows = file.readlines()
        for row in rows:
            cells = row.strip().split('\t')
            if len(cells) >= 3:  # בדיקה שהשורה מכילה את כל הנתונים הדרושים
                codon = cells[0]
                amino_acid = cells[2]
                d[codon] = amino_acid
    return d


