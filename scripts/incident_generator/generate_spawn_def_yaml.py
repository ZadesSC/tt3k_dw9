#This file generates basic spawning incidents for the list of characters
import csv
import sys
import operator
import yaml
import os
from ruamel.yaml import YAML
import pathlib
import subprocess

file_prefix="tt3k_dw9_"

#input_files_location="events_def/"
input_files_location="test_def/"
output_files_location="output/"
#text_loc="../../text/db/"
text_loc="output/text/db/"
lua_loc="output/script/campaign/mod/"
lua_base_indent=""

id_inc_mod=1
payload_id_start=1540000000
junction_id_start=1550000000


data = {'events':[]}

def main():
	#clean out output folder
	p = subprocess.Popen("rm -rf " + output_files_location + "*", shell=True).wait()

	#make output directories
	pathlib.Path(output_files_location + "db/incidents_tables/").mkdir(parents=True, exist_ok=True)
	pathlib.Path(output_files_location + "db/cdir_events_incident_option_junctions_tables/").mkdir(parents=True, exist_ok=True)
	pathlib.Path(output_files_location + "db/cdir_events_incident_payloads_tables/").mkdir(parents=True, exist_ok=True)
	pathlib.Path(output_files_location + "text/db/").mkdir(parents=True, exist_ok=True)
	pathlib.Path(output_files_location + "script/campaign/mod/").mkdir(parents=True, exist_ok=True)

	#write the incident table tsvs
	with open(output_files_location + "db/incidents_tables/" + file_prefix + "incident_spawn.tsv", "w") as incident_output, \
	open(output_files_location + "db/cdir_events_incident_option_junctions_tables/" + file_prefix + "incident_option_junctions_spawn.tsv", "w") as incident_option_junctions_output, \
	open(output_files_location + "db/cdir_events_incident_payloads_tables/" + file_prefix + "incident_payloads_spawn.tsv", "w") as incident_payloads_output, \
	open(text_loc + file_prefix + "incidents.loc.tsv", "w") as incident_loc_output, \
	\
	open(output_files_location + file_prefix + "dilemma_spawn.tsv", "w") as dilemma_output, \
	open(output_files_location + file_prefix + "dilemma_option_junctions_spawn.tsv", "w") as dilemma_option_junctions_output, \
	open(output_files_location + file_prefix + "dilemma_payloads_spawn.tsv", "w") as dilemma_payloads_output, \
	open(output_files_location + file_prefix + "dilemma_choice_details.tsv", "w") as dilemma_choice_details_output, \
	open(text_loc + file_prefix + "dilemma_choices.loc.tsv", "w") as dilemma_choices_loc_output, \
	open(text_loc + file_prefix + "dilemmas.loc.tsv", "w") as dilemma_loc_output:#, \
	#\
	#open(text_loc + file_prefix + "dilemma_loc_pc.loc.tsv", "w") as lua_output:

		#writer init for incidents
		incident_writer = csv.writer(incident_output, delimiter='\t', lineterminator='\n')
		incident_option_junctions_writer = csv.writer(incident_option_junctions_output, delimiter='\t', lineterminator='\n')
		incident_payloads_writer = csv.writer(incident_payloads_output, delimiter='\t', lineterminator='\n')
		incident_loc_writer = csv.writer(incident_loc_output, delimiter='\t', lineterminator='\n')

		#writer init for dilemma
		dilemma_writer = csv.writer(dilemma_output, delimiter='\t', lineterminator='\n')
		dilemma_option_junctions_writer = csv.writer(dilemma_option_junctions_output, delimiter='\t', lineterminator='\n')
		dilemma_payloads_writer = csv.writer(dilemma_payloads_output, delimiter='\t', lineterminator='\n')
		dilemma_choice_details_writer = csv.writer(dilemma_choice_details_output, delimiter='\t', lineterminator='\n')
		dilemma_choices_loc_writer = csv.writer(dilemma_choices_loc_output, delimiter='\t', lineterminator='\n')
		dilemma_loc_writer = csv.writer(dilemma_loc_output, delimiter='\t', lineterminator='\n')

		# create data arrays for each table
		incident_base_data = []
		incident_option_junctions_data = []
		incident_payloads_data = []
		incident_text_data = []

		dilemma_base_data = []
		dilemma_option_junctions_data = []
		dilemma_payloads_data = []
		dilemma_choice_details_data = []
		dilemma_choices_text_data = []
		dilemma_text_data = []

		lua_lines = []

		#write incident table header for tsv
		incident_writer.writerow(["incidents_tables"])
		incident_writer.writerow(["0"])
		incident_writer.writerow(["generate","key", "ui_image", "prioritised", "event_category"])

		incident_option_junctions_writer.writerow(["cdir_events_incident_option_junctions_tables"])
		incident_option_junctions_writer.writerow(["0"])
		incident_option_junctions_writer.writerow(["id", "-", "incident_key", "option_key", "value", "target"])

		incident_payloads_writer.writerow(["cdir_events_incident_payloads_tables"])
		incident_payloads_writer.writerow(["0"])
		incident_payloads_writer.writerow(["id", "-", "incident_key", "payload_key", "value", "target_key"])

		#lua writer

		#write dilemma table header for tsv
		dilemma_writer.writerow(["dilemmas_tables"])
		dilemma_writer.writerow(["0"])
		dilemma_writer.writerow(["generate","key", "localised_description", "localised_title", "ui_image", "prioritised", "event_category", "sound_popup_override", "sound_click_override"])

		dilemma_option_junctions_writer.writerow(["cdir_events_dilemma_option_junctions_tables"])
		dilemma_option_junctions_writer.writerow(["0"])
		dilemma_option_junctions_writer.writerow(["dilemma_key", "id", "-", "option_key", "value", "target_key"])

		dilemma_payloads_writer.writerow(["cdir_events_dilemma_payloads_tables"])
		dilemma_payloads_writer.writerow(["0"])
		dilemma_payloads_writer.writerow(["choice_key", "dilemma_key", "id", "-", "payload_key", "value", "target"])

		dilemma_choice_details_writer.writerow(["cdir_events_dilemma_choice_details_tables"])
		dilemma_choice_details_writer.writerow(["2"])
		dilemma_choice_details_writer.writerow(["choice_key", "dilemma_key", "display_dilemma_choice_if_ceo_active", "required_ceos"])

		for events_def_file in os.listdir(input_files_location):
			filename, extension =  os.path.splitext(events_def_file)
			if extension != ".yaml" and extension != ".yml":
				continue
			if "events_def" not in events_def_file:
				continue

			events_def_file_location = input_files_location + events_def_file
			print("Reading file: " + events_def_file)

			with open(events_def_file_location, 'r') as yaml_input_file:
				events_data = yaml.safe_load(yaml_input_file)
				events_list = events_data.get('events')

				if not events_data.get('enabled'):
					print("File " + events_def_file + " is disabled, skipping...")
					continue

				for event in events_list:
					if not ('enabled' not in event or event.get('enabled') is True):
						print("Skipping " + event.get('event_name') + " since it is disabled")
						continue
					print("Event name: " + event.get('event_name'))

					#Load default values for event information
					if 'event_type' not in event:
						event.update({'event_type': 'incident'})
					if 'title' not in event:
						event.update({'title': ''})
					if 'description' not in event:
						event.update({'description': ''})
					if 'ui_image' not in event:
						event.update({'ui_image': '3k_event_ready_for_duty'})
					if 'generate' not in event:
						event.update({'generate': False})
					if 'prioritized' not in event:
						event.update({'prioritized': False})
					if 'event_category' not in event:
						event.update({'event_category': 'tt3k_dw9_historical'})
					if 'sound_popup_override' not in event:
						event.update({'sound_popup_override': ''})
					if 'sound_click_override' not in event:
						event.update({'sound_click_override': ''})

					#build type agnoistic data for writing
					event_base_data=[]
					event_option_junctions_data=[]
					event_payload_data=[]
					event_choice_details_data=[]
					choices_text_data=[]
					text_data=[]

					is_dilemma=False
					if event.get('event_type') == 'dilemma':
						is_dilemma=True

					#write to base table(dilemma/incident table)
					#we assume dilemma and incident are the only valid options
					event_name=""
					if is_dilemma:
						event_name = resolve_event_name(event.get('event_name'))
						base_row=[event.get('generate'), event_name, event.get('title'), event.get('description'), event.get('ui_image'), event.get('prioritized'), event.get('event_category'), event.get('sound_popup_override'), event.get('sound_click_override')]
						event_base_data.append(base_row)

						text_data.append(["dilemmas_localised_title_" + event_name, event.get('title'), True])
						text_data.append(["dilemmas_localised_description_" + event_name, event.get('description'), True])
					else:
						event_name = resolve_event_name(event.get('event_name'))
						base_row=[event.get('generate'), event_name, event.get('ui_image'), event.get('prioritized'), event.get('event_category')]
						event_base_data.append(base_row)

						text_data.append(["incidents_localised_title_" + event_name, event.get('title'), True])
						text_data.append(["incidents_localised_description_" + event_name, event.get('description'), True])

					#write to option_junctions, the schema for the table should be the same for both
					for target in event.get('target'):
						target_name = next(iter(target))
						target_data = target.get(target_name)
						option_junctions_dict = target_data[0].get('option_junctions')

						#setup default for option_junctions
						if 'CND_FIRST_ROUND' not in option_junctions_dict and target_name == 'default':
							option_junctions_dict.update({'CND_FIRST_ROUND': 0})
						#if 'CND_LAST_ROUND' not in option_junctions_dict and target_name == 'default':
						#	option_junctions_dict.update({'CND_LAST_ROUND': 999})
						if 'VAR_CHANCE' not in option_junctions_dict and target_name == 'default':
							option_junctions_dict.update({'VAR_CHANCE': 50000})
						if 'CND_CATEGORY_ROUNDS_TILL_NEXT' not in option_junctions_dict and target_name == 'default':
							option_junctions_dict.update({'CND_CATEGORY_ROUNDS_TILL_NEXT': 0})

						#get option_junctions data
						if is_dilemma:
							for key, value in option_junctions_dict.items():
								resolved_value = resolve_option_junctions_value(key, value)
								event_option_junctions_data.append([event_name, get_junctions_id(), 0, key, resolved_value, target_name])
						else:
							for key, value in option_junctions_dict.items():
								resolved_value = resolve_option_junctions_value(key, value)
								event_option_junctions_data.append([get_junctions_id(), 0, event_name, key, resolved_value, target_name])

						#make sure payloads exists
						if len(target_data) > 1 and 'payloads' in target_data[1]:
							payloads_dict = target_data[1].get('payloads')

							#get payloads data, dilemmas function differently with choice keys
							#choice_key	dilemma_key	id	-	payload_key	value	target
							if is_dilemma:
								for choice, choice_values in payloads_dict.items():
									for key, value in choice_values.items():
										resolved_value = resolve_payloads_value(key, value)
										event_payload_data.append([choice, event_name, get_payloads_id(), 0, key, resolved_value, target_name])
							else:
								for key, value in payloads_dict.items():
									resolved_value = resolve_payloads_value(key, value)
									event_payload_data.append([get_payloads_id(), 0, event_name, key, resolved_value, target_name])

					#process dilemma choices
					if is_dilemma:
						for choice_key in event.get('choice'):
							choice_data = event.get('choice').get(choice_key)

							if "display_dilemma_choice_if_ceo_active" in choice_data:
								ddcica = choice_data.get("display_dilemma_choice_if_ceo_active")
							else:
								ddcica = False

							if 'required_ceos' in choice_data:
								required_ceos = choice_data.get("required_ceos")
							else:
								required_ceos = ''

							#write to choice data
							event_choice_details_data.append([choice_key, event_name, ddcica, required_ceos])

							#write to text
							choice_title_key = "cdir_events_dilemma_choice_details_localised_choice_title_" + event_name + choice_key
							choice_label_key = "cdir_events_dilemma_choice_details_localised_choice_label_" + event_name + choice_key
							choice_title = choice_data.get('choice_title')
							choice_label = choice_data.get('choice_label')
							choices_text_data.append([choice_title_key, choice_title, True])
							choices_text_data.append([choice_label_key, choice_label, True])

					#this is an custom event, generate lua as well
					#add_lua_lines(lua_lines, event_name_pc, event)
					if event.get('is_custom'):
						custom_data = event.get('custom_data')

						# write function start
						# add comma to end of previous custom event
						# if len(lua_lines) is not 0:
						# 	lua_lines[len(lua_lines) - 1].append(",\n")
						# lua_lines.append("[\"" + event_name_pc + "\"] = {\n")
						# lua_lines.append("\tfunction()\n")
						lua_lines.append("\t\tif context:incident() == \"" + event_name + "\" then\n")

						# write each action as a function being called
						for custom_datum in custom_data:
							custom_action_type = custom_datum.get('ACTION_TYPE')

							if custom_action_type == 'SPAWN':
								target_faction = resolve_faction_name(custom_datum.get('TARGET_FACTION'))
								target_character = resolve_template_name(custom_datum.get('TARGET_TEMPLATE'))
								target_character_element = resolve_officer_element(target_character)

								# write lua action
								lua_lines.append(
									"\t\t\tcdir_events_manager:spawn_character_subtype_template_in_faction(\"" + target_faction + "\", \"" + "3k_general_" + target_character_element + "\", \"" + target_character + "\")\n")
							else:
								print("Invalid ACTION_TYPE: " + custom_action_type)
								exit(1)

						# write lua footer
						# lua_lines.append("\tend,\n")
						# lua_lines.append("\tnil\n")
						# lua_lines.append("}")
						lua_lines.append("\t\tend;\n")

					if is_dilemma:
						dilemma_base_data.extend(event_base_data)
						dilemma_option_junctions_data.extend(event_option_junctions_data)
						dilemma_payloads_data.extend(event_payload_data)
						dilemma_choice_details_data.extend(event_choice_details_data)
						dilemma_choices_text_data.extend(choices_text_data)
						dilemma_text_data.extend(text_data)
					else:
						incident_base_data.extend(event_base_data)
						incident_option_junctions_data.extend(event_option_junctions_data)
						incident_payloads_data.extend(event_payload_data)
						incident_text_data.extend(text_data)

		#generate files for incidents for players
		for row in incident_base_data:
			incident_writer.writerow(row)
		for row in incident_option_junctions_data:
			incident_option_junctions_writer.writerow(row)
		for row in incident_payloads_data:
			incident_payloads_writer.writerow(row)
		for row in incident_text_data:
			incident_loc_writer.writerow(row)

		#generate files for dilemmas for players
		for row in dilemma_base_data:
			dilemma_writer.writerow(row)
		for row in dilemma_option_junctions_data:
			dilemma_option_junctions_writer.writerow(row)
		for row in dilemma_payloads_data:
			dilemma_payloads_writer.writerow(row)
		for row in dilemma_choice_details_data:
			dilemma_choice_details_writer.writerow(row)
		for row in dilemma_choices_text_data:
			dilemma_choices_loc_writer.writerow(row)
		for row in dilemma_text_data:
			dilemma_loc_writer.writerow(row)

	#open lua file at end to avoid stack limit
	with open(lua_loc + file_prefix + "custom_events.lua", "w") as lua_output:
		#write lua header
		# write opening lua
		lua_output.write("core:add_listener(\n")
		lua_output.write("\t\"tt3k_dw9_custom_event_listener\",\n")
		lua_output.write("\t\"IncidentOccuredEvent\",\n")
		lua_output.write("\tfunction(context)\n")
		lua_output.write("\t\treturn string.find(context:incident(), \"tt3k_dw9\")\n")
		lua_output.write("\tend,\n")
		lua_output.write("\tfunction(context)\n")
		lua_output.write("\t\tout(\"TT3K_DW9 CUSTOM EVENT FIRED\")\n")

		#write lua
		for row in lua_lines:
			#print("LUA: " + row)
			lua_output.write(lua_base_indent + row)

		#write lua footer
		lua_output.write("\tend,\n")
		lua_output.write("\ttrue\n")
		lua_output.write(")")

#split into own function because we are running into max blocksize zzz
def add_lua_lines(lua_lines, event_name, event_data):
	if event_data.get('is_custom'):
		custom_data = event_data.get('custom_data')

		# write function start
		# add comma to end of previous custom event
		if len(lua_lines) is not 0:
			lua_lines[len(lua_lines) - 1].append(",\n")
		lua_lines.append("[" + event_name + "] = {\n")
		lua_lines.append("\tfunction()\n")

		# write each action as a function being called
		for custom_datum in custom_data:
			custom_action_type = custom_datum.get('ACTION_TYPE')

			if custom_action_type == 'SPAWN':
				target_faction = custom_datum.get('TARGET_FACTION')
				target_character = resolve_template_name(custom_datum.get('TARGET_TEMPLATE'))
				target_character_element = resolve_officer_element(target_character)

				# write lua action
				lua_lines.append(
					"\t\tcdir_events_manager:spawn_character_subtype_template_in_faction(\"" + target_faction + "\", \"" + "3k_general_" + target_character_element + "\", \"" + target_character + "\n);")
			else:
				print("Invalid ACTION_TYPE: " + custom_action_type)
				exit(1)

		# write lua footer
		lua_lines.append("\tend,")
		lua_lines.append("\tnil")
		lua_lines.append("\t}")

def resolve_option_junctions_value(key, value_to_resolve):
	if key == 'GEN_CND_CHARACTER_TEMPLATE':
		return resolve_template_name(value_to_resolve)
	if key == 'GEN_CND_NOT_CHARACTER_TEMPLATE':
		return resolve_template_name(value_to_resolve)
	if key == 'GEN_CND_FACTION':
		return resolve_faction_name(value_to_resolve)
	if key == 'CND_FACTION':
		return resolve_faction_name(value_to_resolve)
	if key == 'CND_NOT_FACTION':
		return resolve_faction_name(value_to_resolve)
	return value_to_resolve

def resolve_payloads_value(key, value_to_resolve):
	if key == 'SPAWN_AGENT_OFF_MAP' and "CHARACTER_TEMPLATE" not in value_to_resolve:
		officer_key = resolve_template_name(value_to_resolve)
		officer_element = officer_key.rsplit('_', 1)[1]
		return "AGENT[general];AGENT_SUBTYPE[3k_general_" + officer_element + "];CHARACTER_TEMPLATE[" + officer_key + "]"
	if key == 'MARRIAGE' and "CHARACTER_TEMPLATE_KEY" not in value_to_resolve:
		officer_key = resolve_template_name(value_to_resolve)
		officer_element = officer_key.rsplit('_', 1)[1]
		return "CHARACTER_TEMPLATE_KEY[" + officer_key + "];AGENT_SUBTYPE[3k_general_" + officer_element + "]"
	return value_to_resolve

def resolve_officer_element(full_template_name_to_resolve):
	officer_key = resolve_template_name(full_template_name_to_resolve)
	officer_element = officer_key.rsplit('_', 1)[1]
	return officer_element

def resolve_event_name(name_to_resolve):
	resolved_name = name_to_resolve
	if 'historical' not in name_to_resolve:
		#resolved_name = "3k_main_historical_" + resolved_name
		resolved_name = "tt3k_dw9_" + resolved_name
	return resolved_name

#ytr names MUST be passed as a full template name
def resolve_template_name(name_to_resolve):
	if 'historical' in name_to_resolve:
		return name_to_resolve
	else:
		resolved_name = '3k_main_template_historical_' + name_to_resolve
		if 'earth' not in resolved_name and 'fire' not in resolved_name and 'metal' not in resolved_name  and 'water' not in resolved_name  and 'wood' not in resolved_name:
			print(name_to_resolve + " is not a valid name, exiting")
			exit(1)
		return resolved_name

def resolve_faction_name(name_to_resolve):

	if 'shu' == name_to_resolve:
		return '3k_main_faction_liu_bei'
	elif 'wu' == name_to_resolve:
		return '3k_main_faction_sun_jian'
	elif 'wei' == name_to_resolve:
		return '3k_main_faction_cao_cao'
	elif 'faction' not in name_to_resolve:
		print(name_to_resolve + "is not a valid faction, exiting")
		exit(1)
	else:
		return name_to_resolve

def get_junctions_id():
	global junction_id_start
	junction_id_start+=id_inc_mod
	return junction_id_start

def get_payloads_id():
	global payload_id_start
	payload_id_start+=id_inc_mod
	return payload_id_start

if __name__ == '__main__':
    main()

