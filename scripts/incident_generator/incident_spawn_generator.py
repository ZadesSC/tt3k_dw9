#This file generates basic spawning incidents for the list of characters
import csv
import sys
import operator

file_prefix="tt3k_dw9_"
input_file="incident_def_table.txt"

id_inc_mod=10
payload_id_start=1540000000
junction_id_start=1550000000

text_loc="../../text/db/"

def get_junctions_id():
	global junction_id_start
	junction_id_start+=id_inc_mod
	return junction_id_start

def get_payloads_id():
	global payload_id_start
	payload_id_start+=id_inc_mod
	return payload_id_start

#write the incident table tsvs
with open(file_prefix + "incident_spawn_pc.tsv", "w") as incident_pc_output, open(file_prefix + "incident_spawn_npc.tsv", "w") as incident_npc_output, open(file_prefix + "incident_options_junctions_spawn_pc.tsv", "w") as incident_options_junctions_pc_output, open(file_prefix + "incident_options_junctions_spawn_npc.tsv", "w") as incident_options_junctions_npc_output, open(file_prefix + "incident_payloads_spawn_pc.tsv", "w") as incident_payloads_pc_output, open(file_prefix + "incident_payloads_spawn_npc.tsv", "w") as incident_payloads_npc_output, open(text_loc + file_prefix + "incident_loc_pc.loc.tsv", "w") as incident_loc_pc_output:
	incident_pc_writer = csv.writer(incident_pc_output, delimiter='\t', lineterminator='\n')
	incident_npc_writer = csv.writer(incident_npc_output, delimiter='\t', lineterminator='\n')

	incident_options_junctions_pc_writer = csv.writer(incident_options_junctions_pc_output, delimiter='\t', lineterminator='\n')
	incident_options_junctions_npc_writer = csv.writer(incident_options_junctions_npc_output, delimiter='\t', lineterminator='\n')

	incident_payloads_pc_writer = csv.writer(incident_payloads_pc_output, delimiter='\t', lineterminator='\n')
	incident_payloads_npc_writer = csv.writer(incident_payloads_npc_output, delimiter='\t', lineterminator='\n')

	incident_loc_pc_writer = csv.writer(incident_loc_pc_output, delimiter='\t', lineterminator='\n')

	#write incident table header for tsv
	incident_pc_writer.writerow(["incidents_tables"])
	incident_pc_writer.writerow(["0"])
	incident_pc_writer.writerow(["generate","key", "ui_image", "prioritised", "event_category"])
	incident_npc_writer.writerow(["incidents_tables"])
	incident_npc_writer.writerow(["0"])
	incident_npc_writer.writerow(["generate","key", "ui_image", "prioritised", "event_category"])
	
	incident_options_junctions_pc_writer.writerow(["cdir_events_incident_option_junctions_tables"])
	incident_options_junctions_pc_writer.writerow(["0"])
	incident_options_junctions_pc_writer.writerow(["id", "-", "incident_key", "option_key", "value", "target"])
	incident_options_junctions_npc_writer.writerow(["cdir_events_incident_option_junctions_tables"])
	incident_options_junctions_npc_writer.writerow(["0"])
	incident_options_junctions_npc_writer.writerow(["id", "-", "incident_key", "option_key", "value", "target"])

	incident_payloads_pc_writer.writerow(["cdir_events_incident_payloads_tables"])
	incident_payloads_pc_writer.writerow(["0"])
	incident_payloads_pc_writer.writerow(["id", "-", "incident_key", "payload_key", "value", "target"])
	incident_payloads_npc_writer.writerow(["cdir_events_incident_payloads_tables"])
	incident_payloads_npc_writer.writerow(["0"])
	incident_payloads_npc_writer.writerow(["id", "-", "incident_key", "payload_key", "value", "target"])


	#read def tsv
	with open(input_file) as inputtsvfile:
		reader = csv.DictReader(inputtsvfile, dialect='excel-tab')
		for row in reader:
			#check to see if row is disabled, if so, skip
			if row['is_disabled']:
				continue

			spawn_type=row['spawn_type']
			spawn_turn=row['spawn_turn']

			if spawn_type == "marriage":
				continue
			if spawn_type == "move":
				continue
			#if row['faction_or_template'] == "template":
			#	continue


			#gen_template="3k_main_template_historical_dian_wei_hero_wood"
			gen_template="3k_main_template_historical_" + row['character_name'] + "_hero_" + row['element']

			#general values
			generate="True"
			ui_image="3k_event_ready_for_duty"
			prioritised="True"
			event_category="historical"

			#write basic information
			if spawn_type == "move":
				event_name="3k_main_char_historical_" + row['character_name'] + "_spawn_incident_npc"
				incident_npc_writer.writerow([generate, event_name, ui_image, prioritised, event_category])

			event_name="3k_main_char_historical_" + row['character_name'] + "_spawn_incident_pc"
			incident_pc_writer.writerow([generate, event_name, ui_image, prioritised, event_category])

			incident_options_junctions_pc_writer.writerow([get_junctions_id(), 0, event_name, "CND_FIRST_ROUND", spawn_turn, "default"])
			incident_options_junctions_pc_writer.writerow([get_junctions_id(), 0, event_name, "CND_LAST_ROUND", 999, "default"])
			incident_options_junctions_pc_writer.writerow([get_junctions_id(), 0, event_name, "VAR_CHANCE", 5000, "default"])
			incident_options_junctions_pc_writer.writerow([get_junctions_id(), 0, event_name, "CND_UNIQUE", '', "default"])


			#resolve templates and factions
			if row['faction_or_template'] == "faction":
				if row['faction_or_template_name'] == "shu":
					faction="3k_main_faction_liu_bei"
				elif row['faction_or_template_name'] == "wu":
					faction="3k_main_faction_sun_jian"
				elif row['faction_or_template_name'] == "wei":
					faction="3k_main_faction_cao_cao"
				else:
					faction=row['faction_or_template_name']
				incident_options_junctions_pc_writer.writerow([get_junctions_id(), 0, event_name, "GEN_CND_SELF", '', "default"])
				incident_options_junctions_pc_writer.writerow([get_junctions_id(), 0, event_name, "CND_FACTION", faction, "default"])
				incident_options_junctions_pc_writer.writerow([get_junctions_id(), 0, event_name, "GEN_TARGET_FACTION", '', "default"])

				payload_value="AGENT[general];AGENT_SUBTYPE[3k_general_" + row['element'] + "];CHARACTER_TEMPLATE[" + gen_template + "]"
				incident_payloads_pc_writer.writerow([get_payloads_id(), 0, event_name, "SPAWN_AGENT_OFF_MAP", payload_value, "default"])
				incident_payloads_pc_writer.writerow([get_payloads_id(), 0, event_name, "LOCATED", "FACTION", "default"])

			elif row['faction_or_template'] == "template":
				if "historical" not in row['faction_or_template_name']:
					target_template="3k_main_char_historical_" + row['faction_or_template_name'] + "_hero_" + row['template_element']
				else:
					target_template=row['faction_or_template_name']
				incident_options_junctions_pc_writer.writerow([get_junctions_id(), 0, event_name, "GEN_CND_OWNS", '', "default"])
				incident_options_junctions_pc_writer.writerow([get_junctions_id(), 0, event_name, "GEN_CND_CHARACTER_TEMPLATE", target_template, "default"])
				incident_options_junctions_pc_writer.writerow([get_junctions_id(), 0, event_name, "GEN_TARGET_CHARACTER", '', "default"])

				payload_value="AGENT[general];AGENT_SUBTYPE[3k_general_" + row['element'] + "];CHARACTER_TEMPLATE[" + gen_template + "]"
				incident_payloads_pc_writer.writerow([get_payloads_id(), 0, event_name, "SPAWN_AGENT_OFF_MAP", payload_value, "default"])
			else:
				print("Invalid value for faction_or_template: " + row['faction_or_template'])
				exit()
			event_title_key = "incidents_localised_title_" + event_name
			event_title_value = row['event_title']
			event_body_key = "incidents_localised_description_" + event_name
			event_body_value = row['event_text']
			incident_loc_pc_writer.writerow([event_title_key, event_title_value, "True"])
			incident_loc_pc_writer.writerow([event_body_key, event_body_value, "True"])
