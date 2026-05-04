import os
import unicodedata

def normalize_filename(filename):
    # Türkçe karakterleri kaldır
    nfkd_form = unicodedata.normalize('NFKD', filename)
    only_ascii = nfkd_form.encode('ASCII', 'ignore').decode('ASCII')

    # boşlukları alt çizgi yap
    only_ascii = only_ascii.replace(" ", "_")

    return only_ascii


def fix_filenames(folder_path):
    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)

        if not os.path.isfile(old_path):
            continue

        new_name = normalize_filename(filename)
        new_path = os.path.join(folder_path, new_name)

        if old_path != new_path:
            os.rename(old_path, new_path)
            print(f"✔ {filename} → {new_name}")


if __name__ == "__main__":
    fix_filenames("data/database")