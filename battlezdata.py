import cv2
import numpy as np

def merge_images(images):
    total_height = sum(image.shape[0] for image in images)
    max_width = max(image.shape[1] for image in images)
    merged_image = np.zeros((total_height, max_width), dtype=np.uint8)

    current_y = 0
    for image in images:
        merged_image[current_y:current_y + image.shape[0], :image.shape[1]] = image
        current_y += image.shape[0]

    return merged_image

battle_z_list = cv2.imread('assets/battle-z/list.jpg', 0)
battle_z_loading = cv2.imread('assets/battle-z/loading.jpg', 0)
battle_z_cancel = cv2.imread('assets/battle-z/cancel.jpg', 0)
battle_z_items_data = {
    '1-son-goku-super-saiyan-3': {
        'image': cv2.imread('assets/battle-z/items/1-son-goku-super-saiyan-3.jpg', 0),
        'level_target': 11,
        'description': 'Son Goku Super Saiyan 3',
        'skip': False
    },
    '2-broly-super-saiyan-legendaire': {
        'image': cv2.imread('assets/battle-z/items/2-broly-super-saiyan-legendaire.jpg', 0),
        'level_target': 11,
        'description': 'Broly Super Saiyan Légendaire',
        'skip': False
    },
    '3-saga-de-namek': {
        'image': cv2.imread('assets/battle-z/items/3-saga-de-namek.jpg', 0),
        'level_target': 11,
        'description': 'Saga de Namek',
        'skip': False
    },
    '4-freezer-pleine-puissance': {
        'image': cv2.imread('assets/battle-z/items/4-freezer-pleine-puissance.jpg', 0),
        'level_target': 11,
        'description': 'Freezer Pleine Puissance',
        'skip': False
    },
    '5-kamehameha-familial': {
        'image': cv2.imread('assets/battle-z/items/5-kamehameha-familial.jpg', 0),
        'level_target': 11,
        'description': 'Kamehameha Familial',
        'skip': False
    },
    '6-son-gohan-ultime': {
        'image': cv2.imread('assets/battle-z/items/6-son-gohan-ultime.jpg', 0),
        'level_target': 11,
        'description': 'Son Gohan Ultime',
        'skip': False
    },
    '7-piccolo': {
        'image': cv2.imread('assets/battle-z/items/7-piccolo.jpg', 0),
        'level_target': 11,
        'description': 'Piccolo',
        'skip': False
    },
    '8-boo-petit': {
        'image': cv2.imread('assets/battle-z/items/8-boo-petit.jpg', 0),
        'level_target': 11,
        'description': 'Boo Petit',
        'skip': False
    },
    '9-beerus': {
        'image': cv2.imread('assets/battle-z/items/9-beerus.jpg', 0),
        'level_target': 11,
        'description': 'Beerus',
        'skip': False
    },
    '10-broly': {
        'image': cv2.imread('assets/battle-z/items/10-broly.jpg', 0),
        'level_target': 11,
        'description': 'Broly',
        'skip': False
    },
    '11-son-goku-jr-super-saiyan': {
        'image': cv2.imread('assets/battle-z/items/11-son-goku-jr-super-saiyan.jpg', 0),
        'level_target': 11,
        'description': 'Son Goku Jr Super Saiyan',
        'skip': False
    },
    '12-vegeta-jr-super-saiyan': {
        'image': cv2.imread('assets/battle-z/items/12-vegeta-jr-super-saiyan.jpg', 0),
        'level_target': 11,
        'description': 'Vegeta Jr Super Saiyan',
        'skip': False
    },
    '13-omega-shenron': {
        'image': cv2.imread('assets/battle-z/items/13-omega-shenron.jpg', 0),
        'level_target': 11,
        'description': 'Omega Shenron',
        'skip': False
    },
    '14-gotenks-super-saiyan-3': {
        'image': cv2.imread('assets/battle-z/items/14-gotenks-super-saiyan-3.jpg', 0),
        'level_target': 11,
        'description': 'Gotenks Super Saiyan 3',
        'skip': False
    },
    '15-canon-garric-pere-fils': {
        'image': cv2.imread('assets/battle-z/items/15-canon-garric-pere-fils.jpg', 0),
        'level_target': 11,
        'description': 'Canon Garric Père Fils',
        'skip': False
    },
    '16-golden-freezer': {
        'image': cv2.imread('assets/battle-z/items/16-golden-freezer.jpg', 0),
        'level_target': 11,
        'description': 'Golden Freezer',
        'skip': False
    },
    '17-goku-black': {
        'image': cv2.imread('assets/battle-z/items/17-goku-black.jpg', 0),
        'level_target': 11,
        'description': 'Goku Black',
        'skip': False
    },
    '18-freezer-2e-forme': {
        'image': cv2.imread('assets/battle-z/items/18-freezer-2e-forme.jpg', 0),
        'level_target': 11,
        'description': 'Freezer 2e Forme',
        'skip': False
    },
    '19-broly-super-saiyan-legendaire': {
        'image': cv2.imread('assets/battle-z/items/19-broly-super-saiyan-legendaire.jpg', 0),
        'level_target': 11,
        'description': 'Broly Super Saiyan Légendaire',
        'skip': False
    },
    '20-combats-feroces': {
        'image': cv2.imread('assets/battle-z/items/20-combats-feroces.jpg', 0),
        'level_target': 11,
        'description': 'Combats Féroces',
        'skip': False
    },
    '21-cell-parfait': {
        'image': cv2.imread('assets/battle-z/items/21-cell-parfait.jpg', 0),
        'level_target': 11,
        'description': 'Cell Parfait',
        'skip': False
    },
    '22-cell-parfait': {
        'image': cv2.imread('assets/battle-z/items/22-cell-parfait.jpg', 0),
        'level_target': 11,
        'description': 'Cell Parfait',
        'skip': False
    },
    '23-son-goku-super-saiyan-divin-ss': {
        'image': cv2.imread('assets/battle-z/items/23-son-goku-super-saiyan-divin-ss.jpg', 0),
        'level_target': 11,
        'description': 'Son Goku Super Saiyan Divin SS',
        'skip': False
    },
    '24-omega-shenron': {
        'image': cv2.imread('assets/battle-z/items/24-omega-shenron.jpg', 0),
        'level_target': 11,
        'description': 'Omega Shenron',
        'skip': False
    },
    '25-zamasu-fusion': {
        'image': cv2.imread('assets/battle-z/items/25-zamasu-fusion.jpg', 0),
        'level_target': 11,
        'description': 'Zamasu Fusion',
        'skip': False
    },
    '26-saga-rivaux-du-destin': {
        'image': cv2.imread('assets/battle-z/items/26-saga-rivaux-du-destin.jpg', 0),
        'level_target': 11,
        'description': 'Saga Rivaux du Destin',
        'skip': False
    },
    '27-vegetto-super-saiyan-divin-ss': {
        'image': cv2.imread('assets/battle-z/items/27-vegetto-super-saiyan-divin-ss.jpg', 0),
        'level_target': 11,
        'description': 'Vegetto Super Saiyan Divin SS',
        'skip': False
    },
    '28-vegeta-super-saiyan-divin-ss': {
        'image': cv2.imread('assets/battle-z/items/28-vegeta-super-saiyan-divin-ss.jpg', 0),
        'level_target': 11,
        'description': 'Vegeta Super Saiyan Divin SS',
        'skip': False
    },
    '29-trunks-super-saiyan-futur': {
        'image': cv2.imread('assets/battle-z/items/29-trunks-super-saiyan-futur.jpg', 0),
        'level_target': 11,
        'description': 'Trunks Super Saiyan Futur',
        'skip': False
    },
    '30-goku-black-super-saiyan-rose': {
        'image': cv2.imread('assets/battle-z/items/30-goku-black-super-saiyan-rose.jpg', 0),
        'level_target': 11,
        'description': 'Goku Black Super Saiyan Rosé',
        'skip': False
    },
    '31-saga-combattantes-univers-6': {
        'image': cv2.imread('assets/battle-z/items/31-saga-combattantes-univers-6.jpg', 0),
        'level_target': 11,
        'description': 'Saga Combattantes Univers 6',
        'skip': False
    },
    '32-broly-super-saiyan-3': {
        'image': cv2.imread('assets/battle-z/items/32-broly-super-saiyan-3.jpg', 0),
        'level_target': 11,
        'description': 'Broly Super Saiyan 3',
        'skip': False
    },
    '33-pride-troopers': {
        'image': cv2.imread('assets/battle-z/items/33-pride-troopers.jpg', 0),
        'level_target': 11,
        'description': 'Pride Troopers',
        'skip': False
    },
    '34-super-c-17': {
        'image': cv2.imread('assets/battle-z/items/34-super-c-17.jpg', 0),
        'level_target': 11,
        'description': 'Super C-17',
        'skip': False
    },
    '35-boo-petit-2': {
        'image': cv2.imread('assets/battle-z/items/35-boo-petit-2.jpg', 0),
        'level_target': 11,
        'description': 'Boo Petit 2',
        'skip': False
    },
    '36-le-saiyan-masque': {
        'image': cv2.imread('assets/battle-z/items/36-le-saiyan-masque.jpg', 0),
        'level_target': 11,
        'description': 'Le Saiyan Masqué',
        'skip': False
    },
    '37-super-gogeta': {
        'image': cv2.imread('assets/battle-z/items/37-super-gogeta.jpg', 0),
        'level_target': 11,
        'description': 'Super Gogeta',
        'skip': False
    },
    '38-super-janemba': {
        'image': cv2.imread('assets/battle-z/items/38-super-janemba.jpg', 0),
        'level_target': 11,
        'description': 'Super Janemba',
        'skip': False
    },
    '39-saga-rivaux-du-destin-2': {
        'image': cv2.imread('assets/battle-z/items/39-saga-rivaux-du-destin-2.jpg', 0),
        'level_target': 11,
        'description': 'Saga Rivaux du Destin 2',
        'skip': False
    },
    '40-son-goku-signes-de-ultra-instinct': {
        'image': cv2.imread('assets/battle-z/items/40-son-goku-signes-de-ultra-instinct.jpg', 0),
        'level_target': 11,
        'description': 'Son Goku Signes de Ultra Instinct',
        'skip': False
    },
    '41-son-goku-freezer-forme-finale-ange': {
        'image': cv2.imread('assets/battle-z/items/41-son-goku-freezer-forme-finale-ange.jpg', 0),
        'level_target': 11,
        'description': 'Son Goku & Freezer Forme Finale Ange',
        'skip': False
    },
    '42-saga-des-super-guerriers': {
        'image': cv2.imread('assets/battle-z/items/42-saga-des-super-guerriers.jpg', 0),
        'level_target': 11,
        'description': 'Saga des Super Guerriers',
        'skip': False
    },
    '43-gotenks-super-saiyan-3': {
        'image': cv2.imread('assets/battle-z/items/43-gotenks-super-saiyan-3.jpg', 0),
        'level_target': 11,
        'description': 'Gotenks Super Saiyan 3',
        'skip': False
    },
    '44-broly-super-saiyan-legendaire': {
        'image': cv2.imread('assets/battle-z/items/44-broly-super-saiyan-legendaire.jpg', 0),
        'level_target': 11,
        'description': 'Broly Super Saiyan Légendaire',
        'skip': False
    },
    '45-tapion-hildegarn': {
        'image': cv2.imread('assets/battle-z/items/45-tapion-hildegarn.jpg', 0),
        'level_target': 11,
        'description': 'Tapion & Hildegarn',
        'skip': False
    },
    '46-saga-rivaux-du-destin-3': {
        'image': cv2.imread('assets/battle-z/items/46-saga-rivaux-du-destin-3.jpg', 0),
        'level_target': 11,
        'description': 'Saga Rivaux du Destin 3',
        'skip': False
    },
    '47-cooler-forme-finale': {
        'image': cv2.imread('assets/battle-z/items/47-cooler-forme-finale.jpg', 0),
        'level_target': 11,
        'description': 'Cooler Forme Finale',
        'skip': False
    },
    '48-son-goku-super-saiyan-3-ange': {
        'image': cv2.imread('assets/battle-z/items/48-son-goku-super-saiyan-3-ange.jpg', 0),
        'level_target': 11,
        'description': 'Son Goku Super Saiyan 3 Ange',
        'skip': False
    },
    '49-freezer-1re-forme': {
        'image': cv2.imread('assets/battle-z/items/49-freezer-1re-forme.jpg', 0),
        'level_target': 11,
        'description': 'Freezer 1re Forme',
        'skip': False
    },
    '50-edition-heroines': {
        'image': cv2.imread('assets/battle-z/items/50-edition-heroines.jpg', 0),
        'level_target': 11,
        'description': 'Édition Héroïnes',
        'skip': False
    },
    '51-majin-vegeta': {
        'image': cv2.imread('assets/battle-z/items/51-majin-vegeta.jpg', 0),
        'level_target': 11,
        'description': 'Majin Vegeta',
        'skip': False
    },
    '52-son-goku-super-saiyan': {
        'image': cv2.imread('assets/battle-z/items/52-son-goku-super-saiyan.jpg', 0),
        'level_target': 11,
        'description': 'Son Goku Super Saiyan',
        'skip': False
    },
    '53-bardock': {
        'image': cv2.imread('assets/battle-z/items/53-bardock.jpg', 0),
        'level_target': 11,
        'description': 'Bardock',
        'skip': False
    },
    '54-gorilles': {
        'image': cv2.imread('assets/battle-z/items/54-gorilles.jpg', 0),
        'level_target': 11,
        'description': 'Gorilles',
        'skip': False
    },
    '55-hit': {
        'image': cv2.imread('assets/battle-z/items/55-hit.jpg', 0),
        'level_target': 11,
        'description': 'Hit',
        'skip': False
    },
    '56-dragon-ball-fighterz': {
        'image': cv2.imread('assets/battle-z/items/56-dragon-ball-fighterz.jpg', 0),
        'level_target': 11,
        'description': 'Dragon Ball FighterZ',
        'skip': False
    },
    '57-trunks-super-saiyan-jeune': {
        'image': cv2.imread('assets/battle-z/items/57-trunks-super-saiyan-jeune.jpg', 0),
        'level_target': 11,
        'description': 'Trunks Super Saiyan Jeune',
        'skip': False
    },
    '58-son-gohan-super-saiyan-futur': {
        'image': cv2.imread('assets/battle-z/items/58-son-gohan-super-saiyan-futur.jpg', 0),
        'level_target': 11,
        'description': 'Son Gohan Super Saiyan Futur',
        'skip': False
    },
    '59-saga-db-fusions': {
        'image': cv2.imread('assets/battle-z/items/59-saga-db-fusions.jpg', 0),
        'level_target': 11,
        'description': 'Saga DB Fusions',
        'skip': False
    },
    '60-saga-db-fusions-2': {
        'image': cv2.imread('assets/battle-z/items/60-saga-db-fusions-2.jpg', 0),
        'level_target': 11,
        'description': 'Saga DB Fusions 2',
        'skip': False
    },
    '61-trunks-et-son-goten-petits': {
        'image': cv2.imread('assets/battle-z/items/61-trunks-et-son-goten-petits.jpg', 0),
        'level_target': 11,
        'description': 'Trunks et Son Goten Petits',
        'skip': False
    },
    '62-saga-rivaux-du-destin-4': {
        'image': cv2.imread('assets/battle-z/items/62-saga-rivaux-du-destin-4.jpg', 0),
        'level_target': 11,
        'description': 'Saga Rivaux du Destin 4',
        'skip': False
    },
    '63-gogeta-super-saiyan-4-contre-omega-shenron': {
        'image': cv2.imread('assets/battle-z/items/63-gogeta-super-saiyan-4-contre-omega-shenron.jpg', 0),
        'level_target': 11,
        'description': 'Gogeta Super Saiyan 4 contre Omega Shenron',
        'skip': False
    },
    '64-son-goku-super-saiyan-ange-vegeta-super-saiyan-ange': {
        'image': cv2.imread('assets/battle-z/items/64-son-goku-super-saiyan-ange-vegeta-super-saiyan-ange.jpg', 0),
        'level_target': 11,
        'description': 'Son Goku Super Saiyan Ange & Vegeta Super Saiyan Ange',
        'skip': False
    },
    '65-son-goku-super-saiyan-vegeta-super-saiyan': {
        'image': cv2.imread('assets/battle-z/items/65-son-goku-super-saiyan-vegeta-super-saiyan.jpg', 0),
        'level_target': 11,
        'description': 'Son Goku Super Saiyan & Vegeta Super Saiyan',
        'skip': False
    },
    '66-saga-rivaux-du-destin-5': {
        'image': cv2.imread('assets/battle-z/items/66-saga-rivaux-du-destin-5.jpg', 0),
        'level_target': 11,
        'description': 'Saga Rivaux du Destin 5',
        'skip': False
    },
    '67-vegeta-super-saiyan-divin-ss': {
        'image': cv2.imread('assets/battle-z/items/67-vegeta-super-saiyan-divin-ss.jpg', 0),
        'level_target': 11,
        'description': 'Vegeta Super Saiyan Divin SS',
        'skip': False
    },
    '68-dokkan-all-star': {
        'image': cv2.imread('assets/battle-z/items/68-dokkan-all-star.jpg', 0),
        'level_target': 11,
        'description': 'Dokkan All Star',
        'skip': False
    },
    '69-thales': {
        'image': cv2.imread('assets/battle-z/items/69-thales.jpg', 0),
        'level_target': 11,
        'description': 'Thales',
        'skip': False
    },
    '70-son-gohan-ultime': {
        'image': cv2.imread('assets/battle-z/items/70-son-gohan-ultime.jpg', 0),
        'level_target': 11,
        'description': 'Son Gohan Ultime',
        'skip': False
    },
    '71-cell-forme-parfaite-cell-junior': {
        'image': cv2.imread('assets/battle-z/items/71-cell-forme-parfaite-cell-junior.jpg', 0),
        'level_target': 11,
        'description': 'Cell Forme Parfaite & Cell Junior',
        'skip': False
    },
    '72-golden-freezer-ange': {
        'image': cv2.imread('assets/battle-z/items/72-golden-freezer-ange.jpg', 0),
        'level_target': 11,
        'description': 'Golden Freezer Ange',
        'skip': False
    },
    '73-fusion-bleue-et-super-saiyan-rose': {
        'image': cv2.imread('assets/battle-z/items/73-fusion-bleue-et-super-saiyan-rose.jpg', 0),
        'level_target': 11,
        'description': 'Fusion Bleue et Super Saiyan Rosé',
        'skip': False
    },
    '74-trunks-jeune-futur-mai-futur': {
        'image': cv2.imread('assets/battle-z/items/74-trunks-jeune-futur-mai-futur.jpg', 0),
        'level_target': 11,
        'description': 'Trunks Jeune Futur & Mai Futur',
        'skip': False
    },
    '75-goku-black-super-saiyan-rose-zamasu': {
        'image': cv2.imread('assets/battle-z/items/75-goku-black-super-saiyan-rose-zamasu.jpg', 0),
        'level_target': 11,
        'description': 'Goku Black Super Saiyan Rosé & Zamasu',
        'skip': False
    },
    '76-son-goku-super-saiyan-4-ultra-puissance-max': {
        'image': cv2.imread('assets/battle-z/items/76-son-goku-super-saiyan-4-ultra-puissance-max.jpg', 0),
        'level_target': 11,
        'description': 'Son Goku Super Saiyan 4 Ultra Puissance Max',
        'skip': False
    },
    '77-son-goku-gt-pan-gt-trunks-gt': {
        'image': cv2.imread('assets/battle-z/items/77-son-goku-gt-pan-gt-trunks-gt.jpg', 0),
        'level_target': 11,
        'description': 'Son Goku GT, Pan GT & Trunks GT',
        'skip': False
    },
    '78-edition-heroines-2': {
        'image': cv2.imread('assets/battle-z/items/78-edition-heroines-2.jpg', 0),
        'level_target': 11,
        'description': 'Édition Héroïnes 2',
        'skip': False
    },
    '79-son-goku': {
        'image': cv2.imread('assets/battle-z/items/79-son-goku.jpg', 0),
        'level_target': 11,
        'description': 'Son Goku',
        'skip': False
    },
    '80-freezer-pleine-puissance': {
        'image': cv2.imread('assets/battle-z/items/80-freezer-pleine-puissance.jpg', 0),
        'level_target': 11,
        'description': 'Freezer Pleine Puissance',
        'skip': False
    },
    '81-metal-cooler': {
        'image': cv2.imread('assets/battle-z/items/81-metal-cooler.jpg', 0),
        'level_target': 11,
        'description': 'Metal Cooler',
        'skip': False
    },
    '82-cooler': {
        'image': cv2.imread('assets/battle-z/items/82-cooler.jpg', 0),
        'level_target': 11,
        'description': 'Cooler',
        'skip': False
    },
    '83-son-goku-enfant': {
        'image': cv2.imread('assets/battle-z/items/83-son-goku-enfant.jpg', 0),
        'level_target': 11,
        'description': 'Son Goku Enfant',
        'skip': False
    },
    '84-bardock-super-saiyan-3': {
        'image': cv2.imread('assets/battle-z/items/84-bardock-super-saiyan-3.jpg', 0),
        'level_target': 11,
        'description': 'Bardock Super Saiyan 3',
        'skip': False
    },
    '85-bojack-puissance-max-guerrier-galactique': {
        'image': cv2.imread('assets/battle-z/items/85-bojack-puissance-max-guerrier-galactique.jpg', 0),
        'level_target': 11,
        'description': 'Bojack Puissance Max Guerrier Galactique',
        'skip': False
    },
    '86-gogeta-super-saiyan': {
        'image': cv2.imread('assets/battle-z/items/86-gogeta-super-saiyan.jpg', 0),
        'level_target': 11,
        'description': 'Gogeta Super Saiyan',
        'skip': False
    },
    '87-broly-super-saiyan': {
        'image': cv2.imread('assets/battle-z/items/87-broly-super-saiyan.jpg', 0),
        'level_target': 11,
        'description': 'Broly Super Saiyan',
        'skip': False
    },
    '88-saga-batailles-divines': {
        'image': cv2.imread('assets/battle-z/items/88-saga-batailles-divines.jpg', 0),
        'level_target': 11,
        'description': 'Saga Batailles Divines',
        'skip': False
    },
    '89-son-gohan-super-saiyan-enfant': {
        'image': cv2.imread('assets/battle-z/items/89-son-gohan-super-saiyan-enfant.jpg', 0),
        'level_target': 11,
        'description': 'Son Gohan Super Saiyan Enfant',
        'skip': False
    },
    '90-cell-forme-parfaite': {
        'image': cv2.imread('assets/battle-z/items/90-cell-forme-parfaite.jpg', 0),
        'level_target': 11,
        'description': 'Cell Forme Parfaite',
        'skip': False
    },
    '91-son-goku-super-saiyan-divin': {
        'image': cv2.imread('assets/battle-z/items/91-son-goku-super-saiyan-divin.jpg', 0),
        'level_target': 11,
        'description': 'Son Goku Super Saiyan Divin',
        'skip': False
    },
    '92-super-vegetto': {
        'image': cv2.imread('assets/battle-z/items/92-super-vegetto.jpg', 0),
        'level_target': 11,
        'description': 'Super Vegetto',
        'skip': False
    },
    '93': {
        'image': cv2.imread('assets/battle-z/items/93.jpg', 0),
        'level_target': 11,
        'description': 'Item 93',
        'skip': False
    },
    '94': {
        'image': cv2.imread('assets/battle-z/items/94.jpg', 0),
        'level_target': 11,
        'description': 'Item 94',
        'skip': False
    },
    '95': {
        'image': cv2.imread('assets/battle-z/items/95.jpg', 0),
        'level_target': 11,
        'description': 'Item 95',
        'skip': False
    },
    '96': {
        'image': cv2.imread('assets/battle-z/items/96.jpg', 0),
        'level_target': 11,
        'description': 'Item 96',
        'skip': False
    },
    '97': {
        'image': cv2.imread('assets/battle-z/items/97.jpg', 0),
        'level_target': 11,
        'description': 'Item 97',
        'skip': False
    },
    '98': {
        'image': cv2.imread('assets/battle-z/items/98.jpg', 0),
        'level_target': 11,
        'description': 'Item 98',
        'skip': False
    },
    '99': {
        'image': cv2.imread('assets/battle-z/items/99.jpg', 0),
        'level_target': 11,
        'description': 'Item 99',
        'skip': False
    },
    '100': {
        'image': cv2.imread('assets/battle-z/items/100.jpg', 0),
        'level_target': 11,
        'description': 'Item 100',
        'skip': False
    },
    '101': {
        'image': cv2.imread('assets/battle-z/items/101.jpg', 0),
        'level_target': 11,
        'description': 'Item 101',
        'skip': False
    },
    '102': {
        'image': cv2.imread('assets/battle-z/items/102.jpg', 0),
        'level_target': 11,
        'description': 'Item 102',
        'skip': False
    },
    '103': {
        'image': cv2.imread('assets/battle-z/items/103.jpg', 0),
        'level_target': 11,
        'description': 'Item 103',
        'skip': False
    },
    '104': {
        'image': cv2.imread('assets/battle-z/items/104.jpg', 0),
        'level_target': 11,
        'description': 'Item 104',
        'skip': False
    },
    '105': {
        'image': cv2.imread('assets/battle-z/items/105.jpg', 0),
        'level_target': 11,
        'description': 'Item 105',
        'skip': False
    },
    '106': {
        'image': cv2.imread('assets/battle-z/items/106.jpg', 0),
        'level_target': 11,
        'description': 'Item 106',
        'skip': False
    },
    '107': {
        'image': cv2.imread('assets/battle-z/items/107.jpg', 0),
        'level_target': 11,
        'description': 'Item 107',
        'skip': False
    },
    '108': {
        'image': cv2.imread('assets/battle-z/items/108.jpg', 0),
        'level_target': 11,
        'description': 'Item 108',
        'skip': False
    },
    '109': {
        'image': cv2.imread('assets/battle-z/items/109.jpg', 0),
        'level_target': 11,
        'description': 'Item 109',
        'skip': False
    },
    '110': {
        'image': cv2.imread('assets/battle-z/items/110.jpg', 0),
        'level_target': 11,
        'description': 'Item 110',
        'skip': False
    },
    '111': {
        'image': cv2.imread('assets/battle-z/items/111.jpg', 0),
        'level_target': 11,
        'description': 'Item 111',
        'skip': False
    },
    '112': {
        'image': cv2.imread('assets/battle-z/items/112.jpg', 0),
        'level_target': 11,
        'description': 'Item 112',
        'skip': False
    },
    '113': {
        'image': cv2.imread('assets/battle-z/items/113.jpg', 0),
        'level_target': 11,
        'description': 'Item 113',
        'skip': False
    },
    '114': {
        'image': cv2.imread('assets/battle-z/items/114.jpg', 0),
        'level_target': 11,
        'description': 'Item 114',
        'skip': False
    },
    '115': {
        'image': cv2.imread('assets/battle-z/items/115.jpg', 0),
        'level_target': 11,
        'description': 'Item 115',
        'skip': False
    },
    '116': {
        'image': cv2.imread('assets/battle-z/items/116.jpg', 0),
        'level_target': 11,
        'description': 'Item 116',
        'skip': False
    },
    '117': {
        'image': cv2.imread('assets/battle-z/items/117.jpg', 0),
        'level_target': 11,
        'description': 'Item 117',
        'skip': False
    },
    '118': {
        'image': cv2.imread('assets/battle-z/items/118.jpg', 0),
        'level_target': 11,
        'description': 'Item 118',
        'skip': False
    },
    '119': {
        'image': cv2.imread('assets/battle-z/items/119.jpg', 0),
        'level_target': 11,
        'description': 'Item 119',
        'skip': False
    },
    '120': {
        'image': cv2.imread('assets/battle-z/items/120.jpg', 0),
        'level_target': 11,
        'description': 'Item 120',
        'skip': False
    },
    '121': {
        'image': cv2.imread('assets/battle-z/items/121.jpg', 0),
        'level_target': 11,
        'description': 'Item 121',
        'skip': False
    },
    '122': {
        'image': cv2.imread('assets/battle-z/items/122.jpg', 0),
        'level_target': 11,
        'description': 'Item 122',
        'skip': False
    },
    '123': {
        'image': cv2.imread('assets/battle-z/items/123.jpg', 0),
        'level_target': 11,
        'description': 'Item 123',
        'skip': False
    },
    '124': {
        'image': cv2.imread('assets/battle-z/items/124.jpg', 0),
        'level_target': 11,
        'description': 'Item 124',
        'skip': False
    },
    '125': {
        'image': cv2.imread('assets/battle-z/items/125.jpg', 0),
        'level_target': 11,
        'description': 'Item 125',
        'skip': False
    },
    '126': {
        'image': cv2.imread('assets/battle-z/items/126.jpg', 0),
        'level_target': 11,
        'description': 'Item 126',
        'skip': False
    },
    '127': {
        'image': cv2.imread('assets/battle-z/items/127.jpg', 0),
        'level_target': 11,
        'description': 'Item 127',
        'skip': False
    },
    '128': {
        'image': cv2.imread('assets/battle-z/items/128.jpg', 0),
        'level_target': 11,
        'description': 'Item 128',
        'skip': False
    },
    '129': {
        'image': cv2.imread('assets/battle-z/items/129.jpg', 0),
        'level_target': 11,
        'description': 'Item 129',
        'skip': False
    },
    '130': {
        'image': cv2.imread('assets/battle-z/items/130.jpg', 0),
        'level_target': 11,
        'description': 'Item 130',
        'skip': False
    },
    '131': {
        'image': cv2.imread('assets/battle-z/items/131.jpg', 0),
        'level_target': 11,
        'description': 'Item 131',
        'skip': False
    },
    '132': {
        'image': cv2.imread('assets/battle-z/items/132.jpg', 0),
        'level_target': 11,
        'description': 'Item 132',
        'skip': False
    },
    '133': {
        'image': cv2.imread('assets/battle-z/items/133.jpg', 0),
        'level_target': 11,
        'description': 'Item 133',
        'skip': False
    },
    '134': {
        'image': cv2.imread('assets/battle-z/items/134.jpg', 0),
        'level_target': 11,
        'description': 'Item 134',
        'skip': False
    },
    '135': {
        'image': cv2.imread('assets/battle-z/items/135.jpg', 0),
        'level_target': 11,
        'description': 'Item 135',
        'skip': False
    },
    '136': {
        'image': cv2.imread('assets/battle-z/items/136.jpg', 0),
        'level_target': 11,
        'description': 'Item 136',
        'skip': False
    },
    '137': {
        'image': cv2.imread('assets/battle-z/items/137.jpg', 0),
        'level_target': 11,
        'description': 'Item 137',
        'skip': False
    },
    '138': {
        'image': cv2.imread('assets/battle-z/items/138.jpg', 0),
        'level_target': 11,
        'description': 'Item 138',
        'skip': False
    },
    '139': {
        'image': cv2.imread('assets/battle-z/items/139.jpg', 0),
        'level_target': 11,
        'description': 'Item 139',
        'skip': False
    },
    '140': {
        'image': cv2.imread('assets/battle-z/items/140.jpg', 0),
        'level_target': 11,
        'description': 'Item 140',
        'skip': False
    },
    '141': {
        'image': cv2.imread('assets/battle-z/items/141.jpg', 0),
        'level_target': 11,
        'description': 'Item 141',
        'skip': False
    },
    '142': {
        'image': cv2.imread('assets/battle-z/items/142.jpg', 0),
        'level_target': 11,
        'description': 'Item 142',
        'skip': False
    },
    '143': {
        'image': cv2.imread('assets/battle-z/items/143.jpg', 0),
        'level_target': 11,
        'description': 'Item 143',
        'skip': False
    },
    '144': {
        'image': cv2.imread('assets/battle-z/items/144.jpg', 0),
        'level_target': 11,
        'description': 'Item 144',
        'skip': False
    },
    '145': {
        'image': cv2.imread('assets/battle-z/items/145.jpg', 0),
        'level_target': 11,
        'description': 'Item 145',
        'skip': False
    },
    '146': {
        'image': cv2.imread('assets/battle-z/items/146.jpg', 0),
        'level_target': 11,
        'description': 'Item 146',
        'skip': False
    },
    '147': {
        'image': cv2.imread('assets/battle-z/items/147.jpg', 0),
        'level_target': 11,
        'description': 'Item 147',
        'skip': False
    },
    '148': {
        'image': cv2.imread('assets/battle-z/items/148.jpg', 0),
        'level_target': 11,
        'description': 'Item 148',
        'skip': False
    },
    '149': {
        'image': cv2.imread('assets/battle-z/items/149.jpg', 0),
        'level_target': 11,
        'description': 'Item 149',
        'skip': False
    },
    '150': {
        'image': cv2.imread('assets/battle-z/items/150.jpg', 0),
        'level_target': 11,
        'description': 'Item 150',
        'skip': False
    },
    '151': {
        'image': cv2.imread('assets/battle-z/items/151.jpg', 0),
        'level_target': 11,
        'description': 'Item 151',
        'skip': False
    },
    '152': {
        'image': cv2.imread('assets/battle-z/items/152.jpg', 0),
        'level_target': 11,
        'description': 'Item 152',
        'skip': False
    },
    '153': {
        'image': cv2.imread('assets/battle-z/items/153.jpg', 0),
        'level_target': 11,
        'description': 'Item 153',
        'skip': False
    },
    '154': {
        'image': cv2.imread('assets/battle-z/items/154.jpg', 0),
        'level_target': 11,
        'description': 'Item 154',
        'skip': False
    },
    '155': {
        'image': cv2.imread('assets/battle-z/items/155.jpg', 0),
        'level_target': 11,
        'description': 'Item 155',
        'skip': False
    },
    '156': {
        'image': cv2.imread('assets/battle-z/items/156.jpg', 0),
        'level_target': 11,
        'description': 'Item 156',
        'skip': False
    },
    '157': {
        'image': cv2.imread('assets/battle-z/items/157.jpg', 0),
        'level_target': 11,
        'description': 'Item 157',
        'skip': False
    },
    '158': {
        'image': cv2.imread('assets/battle-z/items/158.jpg', 0),
        'level_target': 11,
        'description': 'Item 158',
        'skip': False
    },
    '159': {
        'image': cv2.imread('assets/battle-z/items/159.jpg', 0),
        'level_target': 11,
        'description': 'Item 159',
        'skip': False
    },
    '160': {
        'image': cv2.imread('assets/battle-z/items/160.jpg', 0),
        'level_target': 11,
        'description': 'Item 160',
        'skip': False
    },
    '161': {
        'image': cv2.imread('assets/battle-z/items/161.jpg', 0),
        'level_target': 11,
        'description': 'Item 161',
        'skip': False
    },
    '162': {
        'image': cv2.imread('assets/battle-z/items/162.jpg', 0),
        'level_target': 11,
        'description': 'Item 162',
        'skip': False
    },
    '163': {
        'image': cv2.imread('assets/battle-z/items/163.jpg', 0),
        'level_target': 11,
        'description': 'Item 163',
        'skip': False
    }
}
battle_z_items = [data['image'] for data in battle_z_items_data.values()]
battle_z_items_image = merge_images(battle_z_items)
cv2.imwrite(f"./tmp/battle-z-items.jpg", battle_z_items_image)
battle_z_item = cv2.imread('assets/battle-z/item.jpg', 0)
battle_z_item_infos_combat = cv2.imread('assets/battle-z/infos-combat.jpg', 0)
battle_z_item_enemy_level_label = cv2.imread('assets/battle-z/enemy-level-label.jpg', 0)
battle_z_item_new_enemy = cv2.imread('assets/battle-z/new-enemy.jpg', 0)
battle_z_item_back = cv2.imread('assets/battle-z/back.jpg', 0)
battle_z_item_templates = [
    cv2.imread("assets/battle-z/are-you-sure.jpg", 0),
    cv2.imread("assets/battle-z/ok.jpg", 0),
    cv2.imread("assets/battle-z/ok2.jpg", 0),
    cv2.imread("assets/battle-z/start.jpg", 0),
    cv2.imread("assets/battle-z/next-level.jpg", 0),
    cv2.imread("assets/battle-z/close.jpg", 0),
    cv2.imread("assets/battle-z/rank-up.jpg", 0),
    cv2.imread("assets/battle-z/ds.jpg", 0),
]

battle_z_item_level = []
for i in range(1, 32):
    battle_z_item_level.append(cv2.imread(f"assets/battle-z/item-level/{i}.jpg", 0))
battle_z_item_level_image = merge_images(battle_z_item_level)
cv2.imwrite(f"./tmp/battle-z-item-level.jpg", battle_z_item_level_image)

battle_z_list_level = []
for i in range(1, 32):
    battle_z_list_level.append(cv2.imread(f"assets/battle-z/list-level/{i}.jpg", 0))
battle_z_list_level_image = merge_images(battle_z_list_level)
cv2.imwrite(f"./tmp/battle-z-list-level.jpg", battle_z_list_level_image)