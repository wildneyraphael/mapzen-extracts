import copy
import json

final_file = dict()
with open('admin_level_2_simplified.json') as json_file:
    level_2 = json.load(json_file)
    final_file = copy.deepcopy(level_2)
    
    for i, feature in enumerate(level_2.get('features')):
        if feature.get('properties').get('is_in_state') in ['MAN991R288247', 'MAN991120027']:
            final_file.get('features').remove(feature)

with open('admin_level_2_simplified.json', 'w') as outfile:
    json.dump(final_file, outfile)