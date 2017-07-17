import os
from zipfile import ZipFile, ZIP_DEFLATED
from PIL import Image

# ORIG_CARD = (63, 88)

CARD_SIZE = (744, 1039)
A4_SIZE = (2480, 3508)
DPI = 300

COLOR_MODEL, COLOR_PATTERN = "RGB", (255, 255, 255)
EXTENSION = ".tiff"


def clear_files():
    for file in os.listdir(os.path.join(os.getcwd(), "prepared_cards")):
        os.remove(os.path.join(os.getcwd(), "prepared_cards", file))
    for file in os.listdir(os.path.join(os.getcwd(), "output")):
        os.remove(os.path.join(os.getcwd(), "output", file))


def prepare_images():
    for number, image_name in enumerate(os.listdir(os.path.join(os.getcwd(), "cards"))):
        Image.open(os.path.join(os.getcwd(), "cards", image_name)) \
            .convert(COLOR_MODEL) \
            .resize(CARD_SIZE, Image.BICUBIC) \
            .save(os.path.join(os.getcwd(), "prepared_cards", str(number) + "_" + str(4) + EXTENSION))


def split_name_and_count():
    mass = []
    summ = 0
    for file in os.listdir(os.path.join(os.getcwd(), "prepared_cards")):
        name = file
        repeat = file.split("_")[1]
        repeat = repeat.split(".")[0]
        summ += int(repeat)
        for i in range(int(repeat)):
            mass.append(name)
    return mass


def group(mass, count):
    new_mass = []
    inner_mass = []

    pos = 1

    while pos <= len(mass):
        inner_mass.append(mass[pos - 1])
        if pos % count == 0 or pos == len(mass):
            new_mass.append(inner_mass)
            inner_mass = []
        pos += 1
    return new_mass


def create_a4(cards, count_a4):
    background_a4 = Image.new(COLOR_MODEL, A4_SIZE, COLOR_PATTERN)

    matrix = []
    for n in range(3):
        for m in range(3):
            matrix.append((CARD_SIZE[0] * m, CARD_SIZE[1] * n))

    for i in range(9):
        try:
            background_a4.paste(Image.open(os.path.join(os.getcwd(), "prepared_cards", cards[i])), matrix[i])
        except IndexError:
            break
    background_a4.save(os.path.join(os.getcwd(), "output", str(count_a4) + EXTENSION), dpi=(DPI, DPI))


def create_zip():
    zip_file = ZipFile("Cards.zip", "w", ZIP_DEFLATED)

    for root, dirs, files in os.walk(os.path.join(os.getcwd(), "output")):
        for file in files:
            zip_file.write(os.path.join(root, file), file)

    zip_file.close()


if __name__ == "__main__":
    clear_files()

    print("Preparing images...")
    prepare_images()

    print("creating A4 pattern...")
    for i, mass_group in enumerate(group(split_name_and_count(), 9)):
        create_a4(mass_group, i)

    # print("creating zip..")
    # create_zip()
    #
    # print("removing temp..")
    # clear_files()

    print("Done!")
