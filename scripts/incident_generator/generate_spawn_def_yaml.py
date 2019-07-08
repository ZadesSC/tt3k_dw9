#This file generates basic spawning incidents for the list of characters
import csv
import sys
import operator
import yaml
import os
from ruamel.yaml import YAML

file_prefix="tt3k_dw9_"

input_files_location="events_def/"
output_files_location="output/"
#text_loc="../../text/db/"
text_loc="output/text/db/"
#input_file="events_def_incidents_spawn.yaml"
#input_file="events_def_incidents_move.yaml"
#input_file="events_def_incidents_marriage.yaml"

id_inc_mod=1
payload_id_start=1540000000
junction_id_start=1550000000


data = {'events':[]}

def main():
	#write the incident table tsvs
	with open(output_files_location + file_prefix + "incident_spawn_pc.tsv", "w") as incident_pc_output, \
	open(output_files_location + file_prefix + "incident_spawn_npc.tsv", "w") as incident_npc_output, \
	open(output_files_location + file_prefix + "incident_option_junctions_spawn_pc.tsv", "w") as incident_option_junctions_pc_output, \
	open(output_files_location + file_prefix + "incident_option_junctions_spawn_npc.tsv", "w") as incident_option_junctions_npc_output, \
	open(output_files_location + file_prefix + "incident_payloads_spawn_pc.tsv", "w") as incident_payloads_pc_output, \
	open(output_files_location + file_prefix + "incident_payloads_spawn_npc.tsv", "w") as incident_payloads_npc_output, \
	open(text_loc + file_prefix + "incident_loc_pc.loc.tsv", "w") as incident_loc_pc_output, \
	\
	open(output_files_location + file_prefix + "dilemma_spawn_pc.tsv", "w") as dilemma_pc_output, \
	open(output_files_location + file_prefix + "dilemma_spawn_npc.tsv", "w") as dilemma_npc_output, \
	open(output_files_location + file_prefix + "dilemma_option_junctions_spawn_pc.tsv", "w") as dilemma_option_junctions_pc_output, \
	open(output_files_location + file_prefix + "dilemma_option_junctions_spawn_npc.tsv", "w") as dilemma_option_junctions_npc_output, \
	open(output_files_location + file_prefix + "dilemma_payloads_spawn_pc.tsv", "w") as dilemma_payloads_pc_output, \
	open(output_files_location + file_prefix + "dilemma_payloads_spawn_npc.tsv", "w") as dilemma_payloads_npc_output, \
	open(text_loc + file_prefix + "dilemma_loc_pc.loc.tsv", "w") as dilemma_loc_pc_output:

		#writer init for incidents
		incident_pc_writer = csv.writer(incident_pc_output, delimiter='\t', lineterminator='\n')
		incident_npc_writer = csv.writer(incident_npc_output, delimiter='\t', lineterminator='\n')

		incident_option_junctions_pc_writer = csv.writer(incident_option_junctions_pc_output, delimiter='\t', lineterminator='\n')
		incident_option_junctions_npc_writer = csv.writer(incident_option_junctions_npc_output, delimiter='\t', lineterminator='\n')

		incident_payloads_pc_writer = csv.writer(incident_payloads_pc_output, delimiter='\t', lineterminator='\n')
		incident_payloads_npc_writer = csv.writer(incident_payloads_npc_output, delimiter='\t', lineterminator='\n')

		incident_loc_pc_writer = csv.writer(incident_loc_pc_output, delimiter='\t', lineterminator='\n')

		#writer init for dilemma
		dilemma_pc_writer = csv.writer(dilemma_pc_output, delimiter='\t', lineterminator='\n')
		dilemma_npc_writer = csv.writer(dilemma_npc_output, delimiter='\t', lineterminator='\n')

		dilemma_option_junctions_pc_writer = csv.writer(dilemma_option_junctions_pc_output, delimiter='\t', lineterminator='\n')
		dilemma_option_junctions_npc_writer = csv.writer(dilemma_option_junctions_npc_output, delimiter='\t', lineterminator='\n')

		dilemma_payloads_pc_writer = csv.writer(dilemma_payloads_pc_output, delimiter='\t', lineterminator='\n')
		dilemma_payloads_npc_writer = csv.writer(dilemma_payloads_npc_output, delimiter='\t', lineterminator='\n')

		dilemma_loc_pc_writer = csv.writer(dilemma_loc_pc_output, delimiter='\t', lineterminator='\n')

		#write incident table header for tsv
		incident_pc_writer.writerow(["incidents_tables"])
		incident_pc_writer.writerow(["0"])
		incident_pc_writer.writerow(["generate","key", "ui_image", "prioritised", "event_category"])
		incident_npc_writer.writerow(["incidents_tables"])
		incident_npc_writer.writerow(["0"])
		incident_npc_writer.writerow(["generate","key", "ui_image", "prioritised", "event_category"])

		incident_option_junctions_pc_writer.writerow(["cdir_events_incident_option_junctions_tables"])
		incident_option_junctions_pc_writer.writerow(["0"])
		incident_option_junctions_pc_writer.writerow(["id", "-", "incident_key", "option_key", "value", "target"])
		incident_option_junctions_npc_writer.writerow(["cdir_events_incident_option_junctions_tables"])
		incident_option_junctions_npc_writer.writerow(["0"])
		incident_option_junctions_npc_writer.writerow(["id", "-", "incident_key", "option_key", "value", "target"])

		incident_payloads_pc_writer.writerow(["cdir_events_incident_payloads_tables"])
		incident_payloads_pc_writer.writerow(["0"])
		incident_payloads_pc_writer.writerow(["id", "-", "incident_key", "payload_key", "value", "target"])
		incident_payloads_npc_writer.writerow(["cdir_events_incident_payloads_tables"])
		incident_payloads_npc_writer.writerow(["0"])
		incident_payloads_npc_writer.writerow(["id", "-", "incident_key", "payload_key", "value", "target"])

		#write dilemma table header for tsv
		dilemma_pc_writer.writerow(["dilemmas_tables"])
		dilemma_pc_writer.writerow(["0"])
		dilemma_pc_writer.writerow(["generate","key", "localised_description", "localised_title", "ui_image", "prioritised", "event_category", "sound_popup_override", "sound_click_override"])
		dilemma_npc_writer.writerow(["dilemmas_tables"])
		dilemma_npc_writer.writerow(["0"])
		dilemma_npc_writer.writerow(["generate","key", "localised_description", "localised_title", "ui_image", "prioritised", "event_category", "sound_popup_override", "sound_click_override"])

		dilemma_option_junctions_pc_writer.writerow(["cdir_events_dilemma_option_junctions_tables"])
		dilemma_option_junctions_pc_writer.writerow(["0"])
		dilemma_option_junctions_pc_writer.writerow(["dilemma_key", "id", "-", "option_key", "value", "target"])
		dilemma_option_junctions_npc_writer.writerow(["cdir_events_dilemma_option_junctions_tables"])
		dilemma_option_junctions_npc_writer.writerow(["0"])
		dilemma_option_junctions_npc_writer.writerow(["dilemma_key", "id", "-", "option_key", "value", "target"])

		dilemma_payloads_pc_writer.writerow(["cdir_events_dilemma_payloads_tables"])
		dilemma_payloads_pc_writer.writerow(["0"])
		dilemma_payloads_pc_writer.writerow(["choice_key", "dilemma_key", "id", "-", "payload_key", "value", "target"])
		dilemma_payloads_npc_writer.writerow(["cdir_events_dilemma_payloads_tables"])
		dilemma_payloads_npc_writer.writerow(["0"])
		dilemma_payloads_npc_writer.writerow(["choice_key", "dilemma_key", "id", "-", "payload_key", "value", "target"])

		#create data arrays for each table
		incident_base_data_pc=[]
		incident_option_junctions_data_pc=[]
		incident_payloads_data_pc=[]
		incident_text_data_pc=[]

		dilemma_base_data_pc=[]
		dilemma_option_junctions_data_pc=[]
		dilemma_payloads_data_pc=[]
		dilemma_text_data_pc=[]

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
						event.update({'event_category': 'historical'})
					if 'sound_popup_override' not in event:
						event.update({'sound_popup_override': ''})
					if 'sound_click_override' not in event:
						event.update({'sound_click_override': ''})

					#build type agnoistic data for writing
					event_base_data_pc=[]
					event_option_junctions_data_pc=[]
					event_payload_data_pc=[]
					text_data_pc=[]

					event_base_data_npc=[]
					event_option_junctions_table_data_npc=[]
					event_payload_data_npc=[]
					text_data_npc=[]

					is_dilemma=False
					if event.get('event_type') == 'dilemma':
						is_dilemma=True

					#write to base table(dilemma/incident table)
					#we assume dilemma and incident are the only valid options
					event_name_pc=""
					event_name_npc=""
					if is_dilemma:
						event_name_pc = resolve_event_name(event.get('event_name')) + "_dilemma_pc"
						base_row=[event.get('generate'), event_name_pc, event.get('title'), event.get('description'), event.get('ui_image'), event.get('prioritized'), event.get('event_category'), event.get('sound_popup_override'), event.get('sound_click_override')]
						event_base_data_pc.append(base_row)
					else:
						event_name_pc = resolve_event_name(event.get('event_name')) + "_incident_pc"
						base_row=[event.get('generate'), event_name_pc, event.get('ui_image'), event.get('prioritized'), event.get('event_category')]
						event_base_data_pc.append(base_row)

						event_name_npc = resolve_event_name(event.get('event_name')) + "_incident_npc"
						base_row=[event.get('generate'), event_name_npc, event.get('ui_image'), event.get('prioritized'), event.get('event_category')]
						event_base_data_npc.append(base_row)

						text_data_pc.append(["incidents_localised_title_" + event_name_pc, event.get('title'), True])
						text_data_pc.append(["incidents_localised_description_" + event_name_pc, event.get('description'), True])

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
								event_option_junctions_data_pc.append([event_name_pc, get_junctions_id(), 0, key, resolved_value, target_name])
						else:
							for key, value in option_junctions_dict.items():
								resolved_value = resolve_option_junctions_value(key, value)
								event_option_junctions_data_pc.append([get_junctions_id(), 0, event_name_pc, key, resolved_value, target_name])

						#make sure payloads exists
						if len(target_data) > 1 and 'payloads' in target_data[1]:
							payloads_dict = target_data[1].get('payloads')

							#get payloads data, dilemmas function differently with choice keys
							#choice_key	dilemma_key	id	-	payload_key	value	target
							if is_dilemma:
								for choice, choice_values in payloads_dict.items():
									for key, value in choice_values.items():
										resolved_value = resolve_payloads_value(key, value)
										event_payload_data_pc.append([choice, event_name_pc, get_payloads_id(), 0, key, resolved_value, target_name])
							else:
								for key, value in payloads_dict.items():
									resolved_value = resolve_payloads_value(key, value)
									event_payload_data_pc.append([get_payloads_id(), 0, event_name_pc, key, resolved_value, target_name])

					if is_dilemma:
						dilemma_base_data_pc.extend(event_base_data_pc)
						dilemma_option_junctions_data_pc.extend(event_option_junctions_data_pc)
						dilemma_payloads_data_pc.extend(event_payload_data_pc)
						dilemma_text_data_pc.extend(text_data_pc)
					else:
						incident_base_data_pc.extend(event_base_data_pc)
						incident_option_junctions_data_pc.extend(event_option_junctions_data_pc)
						incident_payloads_data_pc.extend(event_payload_data_pc)
						incident_text_data_pc.extend(text_data_pc)

		#generate files for incidents for players
		for row in incident_base_data_pc:
			incident_pc_writer.writerow(row)
		for row in incident_option_junctions_data_pc:
			incident_option_junctions_pc_writer.writerow(row)
		for row in incident_payloads_data_pc:
			incident_payloads_pc_writer.writerow(row)
		for row in incident_text_data_pc:
			incident_loc_pc_writer.writerow(row)

		#generate files for dilemmas for players
		for row in dilemma_base_data_pc:
			dilemma_pc_writer.writerow(row)
		for row in dilemma_option_junctions_data_pc:
			dilemma_option_junctions_pc_writer.writerow(row)
		for row in dilemma_payloads_data_pc:
			dilemma_payloads_pc_writer.writerow(row)
		for row in dilemma_text_data_pc:
			dilemma_loc_pc_writer.writerow(row)

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

def resolve_event_name(name_to_resolve):
	resolved_name = name_to_resolve
	if 'historical' not in name_to_resolve:
		resolved_name = "3k_main_historical_" + resolved_name
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




















			##atom, please stop auto trimming my document
