import json
import csv
import sys
import argparse
import struct
import uuid

schema_location="schemas/"
schema_file_name="schema_3k.json"
output_location="output/"

def main():
    #figure out if we are writing to a normal db or a loc
    if args.loc:
        write_loc()
    else:
        write_db()

def write_loc():
    tsv_reader = csv.reader(args.input, delimiter='\t')
    loc_bytes = bytearray(b'')

    rows_count = 0;
    for index, row in enumerate(tsv_reader):
        if row[0] is None:
            print("WARN: " + args.input.name + " is missing data in row " + row + ", skipping...")
            continue

        #add utf16 key
        str_len = len(row[0])
        loc_bytes.extend(struct.pack("h", str_len))
        loc_bytes.extend(bytes(row[0], 'utf16')[2:])

        #add utf16 value
        str_len = len(row[1])
        loc_bytes.extend(struct.pack("h", str_len))
        loc_bytes.extend(bytes(row[1], 'utf16')[2:])

        #add bool
        loc_bytes.extend(struct.pack("?", row[2]))

        rows_count +=1

    header_bytes = bytearray(b'')
    #write loc header
    header_bytes.extend(bytearray(b'\xff\xfeLOC\x00'))
    #write loc version (always 1)
    header_bytes.extend(bytearray(b'\x01\x00\x00\x00'))
    #write table entries count
    header_bytes.extend(struct.pack("i", rows_count))

    total_bytes = bytearray(b'')
    total_bytes.extend(header_bytes)
    total_bytes.extend(loc_bytes)
    args.output.write(total_bytes)

    #close at end
    args.input.close()


def write_db():
    # get schema data
    schema_data = get_schema()

    # need to get a normal reader to get the header row so I can make a dict reader :thinking:
    tsv_reader_header = csv.reader(args.input, delimiter='\t')
    tsv_header = list(tsv_reader_header)[2]
    args.input.close()
    f = open(args.input.name)
    p_out("Table Header: " + str(tsv_header))

    # get tsv
    # tsv_reader = csv.DictReader(f, fieldnames=tsv_header, delimiter='\t')
    tsv_reader = csv.DictReader(f, fieldnames=list(tsv_header), delimiter='\t')
    db_bytes = bytearray(b'')

    row_count = 0
    for index, row in enumerate(tsv_reader):
        p_out(row)
        # first row is table name
        if index == 0:
            if list(row.items())[0] is None:
                p_out("ERROR: Invalid File header, line 1: " + args.input.name)
                exit(1)
            table_name = list(row.items())[0][1]
            p_out("Table Name: " + table_name)
            table_schema = get_table_schema(table_name, schema_data)
        # second row is table version
        elif index == 1:
            if list(row.items())[0] is None:
                print("ERROR: Invalid File header, line 2: " + args.input.name)
                exit(1)
            table_version = list(row.items())[0][1]
            p_out("Table Version: " + table_version)
        # third row is definition
        elif index == 2:
            pass
        # fourth row and on is data
        else:
            if len(row) == 0:
                continue
            db_bytes.extend(convert_row_to_binary(row, table_schema, table_version))
            row_count += 1

    # write to output file
    total_bytes = bytearray(b'')
    total_bytes.extend(convert_file_header_to_binary(table_version, row_count))
    total_bytes.extend(db_bytes)
    args.output.write(total_bytes)

    # close file at end
    args.input.close()
    args.output.close()

def get_schema():
    schema_to_read = schema_location + schema_file_name
    schema_file = open(schema_to_read, 'r')
    schema_data = json.load(schema_file)
    schema_file.close()
    return schema_data

def get_table_schema(table_name, schema_data):
    for table_def in schema_data["tables_definitions"]:
        if table_def["name"] == table_name:
            return table_def
    print("ERROR: Table " + table_name + " not found in schema")
    exit(1)

def convert_row_to_binary(row, table_schema, table_version):
    fields_data=None
    for version in table_schema["versions"]:
        if version.get("version") is int(table_version):
            fields_data = version.get("fields")

    if fields_data is None:
        print("ERROR: no valid data found in schema, table version: " + table_version)
        exit(1)
    for field in fields_data:
        if field["field_name"] not in row:
            print("ERROR: Table row does not contain schema field: " + field["field_name"])
            exit(1)

    #convert row data to binary
    row_bytes = bytearray(b'')
    for index, field in enumerate(fields_data):
        field_name = field["field_name"]
        #get and encode value type
        if field["field_type"] == "StringU8":
            str_len = len(row[field_name])
            row_bytes.extend(struct.pack("h", str_len))
            row_bytes.extend(bytes(row[field_name], 'utf8'))
        elif field["field_type"] == "Boolean":
            row_bytes.extend(struct.pack("?", row[field_name]))
        elif field["field_type"] == "LongInteger":
            row_bytes.extend(struct.pack("q", int(row[field_name])))
        elif field["field_type"] == "OptionalStringU8":
            if row[field_name] == '':
                row_bytes.extend(struct.pack("?", False))
            else:
                row_bytes.extend(struct.pack("?", True))
                str_len = len(row[field_name])
                row_bytes.extend(struct.pack("h", str_len))
            row_bytes.extend(bytes(row[field_name], 'utf8'))
        else:
            print("ERROR: Schema table type " + field["field_type"] + " has not been implemented yet")
            exit(1)
    return row_bytes

def p_out(str):
    if args.verbose:
        print(str)

def convert_file_header_to_binary(table_version, rows_count):
    header_bytes = bytearray(b'')
    #guid marker
    header_bytes.extend(bytearray(b'\xfd\xfe\xfc\xff'))
    #guid_len
    header_bytes.extend(struct.pack("h", 36))
    #guid
    id=str(uuid.uuid4())
    for c in id:
        header_bytes.extend(struct.pack("h", ord(c)))
    #version marker
    header_bytes.extend(bytearray(b'\xfc\xfd\xfe\xff'))
    #version
    header_bytes.extend(struct.pack("i", int(table_version)))
    #mystery /x00 byte
    header_bytes.extend(bytearray(b'\x00'))
    #entry row count
    header_bytes.extend(struct.pack("i", rows_count))
    return header_bytes

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Converts tsv files into db files for Total War: THREE KINGDOMS')
    parser.add_argument("--input", required=True, help="the input tsv file to be processed",type=argparse.FileType('r'))
    parser.add_argument("--output", required=True, help="the output db file", type=argparse.FileType('wb'))
    parser.add_argument("--loc", help="this is a loc database",  action='store_true')
    parser.add_argument("--verbose", help="enable debug logging",  action='store_true')
    args = parser.parse_args()
    main()
