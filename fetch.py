import requests

import parse
import nltkutils


def get_part_link(vendor, model, part):
	""" Gets a link to requested part """
	cars_response = requests.get('http://exist.ru/cat/TecDoc/Cars/{}?all=1'.format(vendor))
	if cars_response.status_code == 404:
		return "Vendor does not exist"
	
	# Getting list of models from HTML
	models = parse.parse_models_list(cars_response.text)
	model_key = nltkutils.get_closest_word(models.keys(), model)
  # Getting model link
	model_link = models[model_key]
	return 'http://exist.ru{}'.format(model_link)

	# # Getting list of complectations from HTML
	# complectations_response = requests.get(model_link.format(vendor))
	# complectations = parse.parse_complectations_list()
	# # Getting the first (for simplicity) complectation in the list
	# complectation_link = next(iter(some_collection))

	# print(complectation_link)



if __name__ == "__main__":
	get_part_link('Ford', 'Sierra', 'двигатель')