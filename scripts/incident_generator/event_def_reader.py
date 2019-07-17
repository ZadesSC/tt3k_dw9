import yaml
import csv


def main():
    with open(events_def_file_location, 'r') as yaml_input_file:
        events_data = yaml.safe_load(yaml_input_file)
        events_list = events_data.get('events')

        if not events_data.get('enabled'):
            print("File " + events_def_file + " is disabled, skipping...")

        for event in events_list:
            if not ('enabled' not in event or event.get('enabled') is True):
                print("Skipping " + event.get('event_name') + " since it is disabled")
                continue
            print("Event name: " + event.get('event_name'))

            # write to option_junctions, the schema for the table should be the same for both
            for target in event.get('target'):

                # make sure payloads exists
                if len(target_data) > 1 and 'payloads' in target_data[1]:
                    payloads_dict = target_data[1].get('payloads')

            # process dilemma choices
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



            # this is an custom event, generate lua as well
            # add_lua_lines(lua_lines, event_name_pc, event)
            if event.get('is_custom'):
                custom_data = event.get('custom_data')

                # write each action as a function being called
                for custom_datum in custom_data:
                    custom_action_type = custom_datum.get('ACTION_TYPE')

                    if custom_action_type == 'SPAWN':
                        pass
                    else:
                        print("Invalid ACTION_TYPE: " + custom_action_type)
                        exit(1)

if __name__ == '__main__':
    main()