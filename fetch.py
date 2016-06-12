import requests

import parse
import nltkutils


def get_part_link(vendor, model, part):
	""" Gets a link to requested part """
	cars_link = 'http://exist.ru/cat/TecDoc/Cars/{}?all=1'.format(vendor)
	if (not model):
		return "Список автомобилей {}: {}".format(vendor, cars_link) 

	cars_response = requests.get(cars_link)
	if cars_response.status_code == 404:
		return "Такой производитель слишком неизвестен :)"
	
	# Getting list of models from HTML
	models = parse.parse_models_list(cars_response.text)
	model_key = nltkutils.get_closest_word(models.keys(), model)

  # Getting model link
	model_link = 'http://exist.ru{}'.format(models[model_key])

	if (not part):
		"Запчасти на {}: {}".format(model_key, model_link)

	# Getting list of complectations from HTML
	complectations_response = requests.get(model_link)
	complectations = parse.parse_complectations_list(complectations_response.text)
	# Getting the first (for simplicity) complectation in the list
	# Let's also cut 'r=1' suffix from link, it's useless
	complectation_link = 'http://exist.ru{}'.format(complectations[0][:-3])

	# Getting list of part types from HTML
	parts_types_response = requests.get(complectation_link)
	parts_types = parse.parse_parts_types_list(parts_types_response.text)
	part_type_key = nltkutils.get_closest_phrase(parts_types.keys(), part)
	# Getting part type link
	part_type_link = model_link = 'http://exist.ru{}'.format(parts_types[part_type_key])

	# Getting list of parts from HTML
	parts_response = requests.get(part_type_link)
	parts = parse.parse_parts_list(parts_response.text)
	# Getting the first (for simplicity) complectation in the list
	if (not parts):
		"Не удалось найти такую запчасть."

	part_link = 'http://exist.ru{}'.format(parts[0])

	# Return link to search page
	return "{} для {}: {}".format(part_type_key, model_key, part_link)


if __name__ == "__main__":
	get_part_link('Ford', 'Sierra', 'двигатель')