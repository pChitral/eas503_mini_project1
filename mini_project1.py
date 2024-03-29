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

    # BEGIN SOLUTION

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
    # END SOLUTION


def read_vcf_file(filename):

    # BEGIN SOLUTION
    list_of_lines = []
    list_of_dicts = []

    with open(filename) as file:
        for line in file:
            if not line.strip():
                continue
            if "#" in line:
                line_without_hash = line[1:].rstrip()
            else:
                list_of_lines.append(line.rstrip())

    for i in range(len(list_of_lines)):
        dicto_of_ith_line = create_dict_from_line(
            line_without_hash.split("\t"), list_of_lines[i])
        list_of_dicts.append(dicto_of_ith_line)

    return list_of_dicts
    # END SOLUTION


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
        info_dict = create_dictionary_of_info_field_values(
            extract_info_field([dicto]))

        # Grabbing all the keys of value of INFO field.
        dicto_info_keys = list(info_dict.keys())

        # Putting them in the data type according to the second input of the function that holds the data type for respective field for our INFO field
        for i in range(len(dicto_info_keys)):
            info_dict[dicto_info_keys[i]] = info_field_data_type[dicto_info_keys[i]](
                info_dict[dicto_info_keys[i]][0])
        dicto["INFO"] = info_dict

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
    for variant in load_data_from_json(filename):
        if variant["CHROM"] == CHROM and variant["REF"] == REF and variant["ALT"] == ALT and variant["POS"] == POS:
            list_of_variants.append(variant)
    # ipdb.set_trace()
    return list_of_variants

    # END SOLUTION


def pull_basic_and_predictor_fields(filename):
    """
    Load mini_project1_data.json and pull out all the variants that have a 
    """
    # BEGIN SOLUTION
    import json
    maal = json.load(open(filename))
    int_val_dict = {"FATHMM_pred": {"T": 0,
                                    "D": 1},

                    "LRT_pred": {"D": 1,
                                 "N": 0,
                                 "U": 0},
                    "MetaLR_pred": {"T": 0,
                                    "D": 1},
                    "MetaSVM_pred": {"T": 0,
                                     "D": 1},

                    "MutationAssessor_pred": {"H": 1,
                                              "N": 0,
                                              "L": 0.25,
                                              "M": 0.5},
                    "MutationTaster_pred": {"D": 1,
                                            "P": 0,
                                            "N": 0,
                                            "A": 1},
                    "PROVEAN_pred":  {"D": 1,
                                      "N": 0},
                    "Polyphen2_HDIV_pred": {"D": 1,
                                            "B": 0,
                                            "P": 0.5},
                    "Polyphen2_HVAR_pred":    {"D": 1,
                                               "B": 0,
                                               "P": 0.5},

                    "SIFT_pred": {"D": 1,
                                  "T": 0},
                    "fathmm_MKL_coding_pred": {"D": 1,
                                               "N": 0}

                    }
    predictors = [
        'FATHMM_pred',
        'LRT_pred',
        'MetaLR_pred',
        'MetaSVM_pred',
        'MutationAssessor_pred',
        'MutationTaster_pred',
        'PROVEAN_pred',
        'Polyphen2_HDIV_pred',
        'Polyphen2_HVAR_pred',
        'SIFT_pred',
        'fathmm_MKL_coding_pred']

    fml_list_dict = []
    full_final = []

    for i in range(len(maal)):
        if predictors[0] in maal[i]["INFO"].keys():
            fml_list_dict.append(maal[i])

    for i in range(len(fml_list_dict)):
        temp_dicto = {}
        sum_predictor_values = 0
        for predictor in predictors:
            if predictor in list(fml_list_dict[i]["INFO"].keys()):
                temp_dicto[predictor] = fml_list_dict[i]["INFO"][predictor]
                sum_predictor_values += int_val_dict[predictor][temp_dicto[predictor]]
        temp_dicto["sum_predictor_values"] = sum_predictor_values
        temp_dicto["CHROM"] = fml_list_dict[i]["CHROM"]
        temp_dicto["POS"] = fml_list_dict[i]["POS"]
        temp_dicto["REF"] = fml_list_dict[i]["REF"]
        temp_dicto["ALT"] = fml_list_dict[i]["ALT"]

        full_final.append(temp_dicto)
    return full_final

    # END SOLUTION


def pull_basic_and_predictor_fields_gzip(filename):
    # BEGIN SOLUTION
    int_val_dict = {"FATHMM_pred": {"T": 0,
                                    "D": 1},

                    "LRT_pred": {"D": 1,
                                 "N": 0,
                                 "U": 0},
                    "MetaLR_pred": {"T": 0,
                                    "D": 1},
                    "MetaSVM_pred": {"T": 0,
                                     "D": 1},

                    "MutationAssessor_pred": {"H": 1,
                                              "N": 0,
                                              "L": 0.25,
                                              "M": 0.5},
                    "MutationTaster_pred": {"D": 1,
                                            "P": 0,
                                            "N": 0,
                                            "A": 1},
                    "PROVEAN_pred":  {"D": 1,
                                      "N": 0},
                    "Polyphen2_HDIV_pred": {"D": 1,
                                            "B": 0,
                                            "P": 0.5},
                    "Polyphen2_HVAR_pred":    {"D": 1,
                                               "B": 0,
                                               "P": 0.5},

                    "SIFT_pred": {"D": 1,
                                  "T": 0},
                    "fathmm_MKL_coding_pred": {"D": 1,
                                               "N": 0}

                    }
    predictors = [
        'FATHMM_pred',
        'LRT_pred',
        'MetaLR_pred',
        'MetaSVM_pred',
        'MutationAssessor_pred',
        'MutationTaster_pred',
        'PROVEAN_pred',
        'Polyphen2_HDIV_pred',
        'Polyphen2_HVAR_pred',
        'SIFT_pred',
        'fathmm_MKL_coding_pred']
    
    import gzip
    list_of_dicts = []
    with gzip.open(filename, 'rt') as fp:
        for line in fp:
            temp_dict = {}
            for line in fp:
                if line.startswith("#"):
                    continue
            line_split = line.strip().split("\t")
            info_field = line_split[7]
            sum_predictor_values = 0
            for ele in info_field.split(";"):
                if "=" not in ele:
                    continue
                key, value = ele.split("=")
                if key not in predictors:
                    continue
                if value ==".":
                    continue
                temp_dict[key] = value
                sum_predictor_values += int_val_dict[key][value]
                print(key, value)
            if temp_dict:
                temp_dict["sum_predictor_values"] = sum_predictor_values
                temp_dict["CHROM"] = line_split[0]
                temp_dict["POS"] = line_split[1]
                temp_dict["REF"] = line_split[3]
                temp_dict["ALT"] = line_split[4]
                list_of_dicts.append(temp_dict)
    import json
    import gzip
    dict_to_json = json.dumps(
        list_of_dicts, sort_keys=True, indent=2)

    with gzip.open('mini_project1_gzip.json', "w") as file:
        file.write(dict_to_json)
    # return list_of_dicts
    # END SOLUTION


def return_all_non_zero_sum_predictor_values():
    # BEGIN SOLUTION
    pass
    # END SOLUTION
