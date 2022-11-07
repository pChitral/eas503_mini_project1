def determine_data_type(value):

    data_type = None
    try:
        int(value)
        data_type = int
        return data_type

    except:
        try:
            float(value)
            data_type = float
            return data_type
        except:
            return str


def determine_data_type_of_list(values):

    list_data_type = []
    for value in values:
        if determine_data_type(value) == (str):
            return str
        if determine_data_type(value) not in list_data_type:
            list_data_type.append(determine_data_type(value))
    if float in list_data_type:
        return float
    if int in list_data_type:
        return int


def format_sample_fields(format_field, sample_field):

    output = {}

    dict_keys = sample_field.keys()
    inner_keys = format_field.split(":")

    for key in dict_keys:
        key_key_value = sample_field[key].split(":")
        temp_dict = {}
        for i in range(len(key_key_value)):
            temp_dict[inner_keys[i]] = key_key_value[i]
        output[key] = temp_dict
    return output


def create_dict_from_line(header, line):

    temp_dict = {}
    list_of_lines = line.split("\t")

    for key in header:
        for i in range(len(list_of_lines)):
            temp_dict[key] = list_of_lines[i]

    temp_dict_keys = list(temp_dict.keys())

    Dict_of_dict_of_everything_after_format = {}
    for i in range(9, len(list_of_lines)):
        Dict_of_dict_of_everything_after_format[temp_dict_keys[i]
                                                ] = list_of_lines[i]

    final_ans_dict = {}
    for i in range(8):
        final_ans_dict[temp_dict_keys[i]] = list_of_lines[i]
        if i == 7:
            final_ans_dict["SAMPLE"] = format_sample_fields(
                list_of_lines[i+1], Dict_of_dict_of_everything_after_format)

    # ipdb.set_trace()
    return final_ans_dict


def read_vcf_file(filename):

    with open(filename) as file:
        list_of_lines = []
        for line in file:
            if not line.strip():
                continue
            list_of_lines.append(line.strip("\n"))
    list_of_dicts = []
    headers = list_of_lines[0].split("\t")
    headers[0] = "CHROM"
    for i in range(1, len(list_of_lines)):
        list_of_dicts.append(create_dict_from_line(headers, list_of_lines[i]))
    return list_of_dicts


def extract_info_field(data):

    answer_list = []
    for i in range(len(data)):
        answer_list.append(data[i]["INFO"])
    return answer_list


def create_dictionary_of_info_field_values(data):

    # BEGIN SOLUTION
    dicto = {}
    info_maal = (data)
    ith_info_maal = []

    for i in range(len(info_maal)):
        ith_info_maal = (info_maal[i].split(";"))
        for j in range(len(ith_info_maal)):
            try:
                key, value = ith_info_maal[j].split("=", 1)
                if value != ".":
                    if key not in dicto.keys():
                        dicto[key] = [value]
                    else:
                        if value not in dicto[key]:
                            dicto[key] += [value]
            except:
                continue
    return dicto


def determine_data_type_of_info_fields(data):

    # Let's make our keys handy
    dict_keys = list(data.keys())

    # Setting up the base for the cake
    dict_data_types = {}
    key_data_type = []

    # Appending the data type of the corresponding key in our list "key_data_type""
    for key in dict_keys:
        key_data_type.append(determine_data_type_of_list(data[key]))

    # Fetching the data type for the respective key from our "key_data_type" list and assigning it as the value for our final answer dictionay named "dict_data_types"'s key
    for i in range(len(dict_keys)):
        dict_data_types[dict_keys[i]] = key_data_type[i]

    return dict_data_types


def format_data(data, info_field_data_type):

    final_answer_list_of_dicts = []
    
    for dicto in data:

        # Handling int and float scene
        dicto["QUAL"] = float(dicto["QUAL"])
        dicto["POS"] = int(dicto["POS"])

        # Creating a dictionary from the list and reassigning it to the info field
        dicto["INFO"] = create_dictionary_of_info_field_values(dicto["INFO"])

        # Grabbing all the keys of value of INFO field.
        dicto_keys = list(dicto["INFO"].keys())

        # Putting them in the data type according to the second input of the function that holds the data type for respective field for our INFO field
        for key in dicto_keys:
            convert_type = info_field_data_type[key]
            dicto["INFO"][key] = convert_type(dicto["INFO"][key])

        final_answer_list_of_dicts.append(dicto)
    # ipdb.set_trace()

    return final_answer_list_of_dicts

    # END SOLUTION


def save_data_as_json(data, filename):
    """
    Write a function whose inputs are a Python dictionary and filename. 
    The function will saves the dictionary as a json file using the filename given. 
    Use the json library. 
    Use these options to correctly format your JSON -- 
    sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False. 
    Use this function to save your parsed data as a json file.
    """
    # BEGIN SOLUTION
    import json

    dict_to_json = json.dumps(
        data, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)

    with open(filename, "w") as file:
        file.write(dict_to_json)

    # END SOLUTION


def load_data_from_json(filename):
    """
    Write a function whose input is a filename for a json file. 
    The function should use the filename to read the JSON file in 
    which you saved your final parsed data. 
    """
    # BEGIN SOLUTION
    import json
    reading_json = open(filename)
    data = json.load(reading_json)
    return data
    # END SOLUTION


def find_variant(CHROM, REF, ALT, POS, filename):
    """
    Write a function whose inputs are CHROM, REF, ALT, POS, and filename. 
    Using these inputs, the function should load a JSON file using the given 
    filename and return a list of variants that match the given CHROM, REF, ALT, and POS. 
    """
    # BEGIN SOLUTION
    # import ipdb
    list_of_variants = []
    maal = load_data_from_json(filename)
    for variant in maal:
        if variant["CHROM"] == CHROM and variant["REF"] == REF and variant["ALT"] == ALT and variant["POS"] == POS:
            list_of_variants.append(variant)
    # ipdb.set_trace()
    return list_of_variants
    print("CHROM")
    # END SOLUTION


def pull_basic_and_predictor_fields(filename):
    """
    Load mini_project1_data.json and pull out all the variants that have a 
    """
    # BEGIN SOLUTION
    import json
    maal = json.load(open(filename))

    # END SOLUTION


def pull_basic_and_predictor_fields_gzip(filename):
    # BEGIN SOLUTION
    pass
    # END SOLUTION


def return_all_non_zero_sum_predictor_values():
    # BEGIN SOLUTION
    pass
    # END SOLUTION
