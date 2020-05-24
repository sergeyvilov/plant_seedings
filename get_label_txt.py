import os

with open('labels.txt', 'w') as f:
    for species_name in next(os.walk('train/'))[1]:
        f.write(species_name + '\n')
