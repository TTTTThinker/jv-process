# 2022-11-05
# lyj - <lyjhust@hust.edu.cn>

import os
import sys
import time

def get_all_csv(dir:str)->list:
    ''' Get all csv files in directory @dir,
        these csv files are data source need to process
    '''
    file_list = os.listdir(dir)
    csv_file_list = []
    for file in file_list:
        if os.path.splitext(file)[1] == ".csv":
            path = os.path.join(dir, file)
            csv_file_list.append(path)
    return csv_file_list

def jv_load(file:str)->dict:
    ''' Load information from a csv file to corresponding jv_dict.
        Currently, the format of a jv_dict is as follow:
        {
            "filename": "$val",
            "time": "$val",
            "instances": [
                [ "$Voc", "$Jsc", "${Fill Factor}", "$Efficiency", "$Vmax", "$Rs", "$Rsh", "$Voltage" ],
                [ "$Voc", "$Jsc", "${Fill Factor}", "$Efficiency", "$Vmax", "$Rs", "$Rsh", "$Voltage" ],
                ...
            ]
        }
    '''

    jv_dict = {}

    jv_dict["filename"] = file
    with open(file, "r", encoding="iso-8859-1") as f:
        lines = f.read().splitlines()
    
    jv_dict["time"] = lines[5].encode("iso-8859-1").decode("gbk")
    
    instances = []
    instance_num = len(lines[8].split(',')) - 1
        
    for i in range(0, instance_num):
        instances.append([])
    for line in range(9, 16):
        str = lines[line]
        str_list = str.split(',')
        num = len(str_list) - 1
        for i in range(0, num):
            instances[i].append(str_list[i+1])
    jv_dict["instances"] = instances
    
    return jv_dict

def load_all_jv(csv_file_list:list)->list:
    list_of_jv_dict = []
    for file in csv_file_list:
        jv_dict = jv_load(file)
        list_of_jv_dict.append(jv_dict)
    
    return list_of_jv_dict

def jv_write(output_file:str, list_of_jv_dict:list)->None:
    ''' write information from a list of jv_dict to a file '''

    with open(output_file, "ab") as f:
        title = "Filename, Time, Voc, Jsc, FF, PCE, Vmax, Rs, Rsh\n".encode("utf-8")
        f.write(title)

        for dict in list_of_jv_dict:
            for i in range(0, len(dict["instances"])):
                instance = dict["instances"][i]
                # line = "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}\n".format(dict["filename"], dict["time"], instance[0], instance[1], instance[2], instance[3], instance[4], instance[5], instance[6])
                column_a = "{0}, ".format(dict["filename"]).encode("utf-8")
                column_b = "{0}, ".format(dict["time"]).encode("gbk")
                column_c = "{0}, {1}, {2}, {3}, {4}, {5}, {6}\n".format(instance[0], instance[1], instance[2], instance[3], instance[4], instance[5], instance[6]).encode("utf-8")
                line = column_a + column_b + column_c
                f.write(line)

def main(input_dir:str, output_file:str)->None:
    csv_file_list = get_all_csv(input_dir)
    list_of_jv_dict = load_all_jv(csv_file_list)
    jv_write(output_file, list_of_jv_dict)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[ERROR] ==>> At least provide a directory to be processed.")
        print("[HINTS] ==>> e.g. python jv.py E:\Projects\perovskite")
        sys.exit(0)
    elif len(sys.argv) < 3:
        print("[HINTS] ==>> Use default output filename: jv_output_$timestamp.csv")
        input_dir = sys.argv[1]
        output_file = "jv_output_" + str(int(time.time())) + ".csv"
    else:
        input_dir = sys.argv[1]
        output_file = sys.argv[2]
    print("[INPUT]  ==>> ", input_dir)
    print("[OUTPUT] ==>> ", output_file)
    main(input_dir, output_file)