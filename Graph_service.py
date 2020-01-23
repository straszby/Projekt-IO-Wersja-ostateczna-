from File import File


def build_modules_graph_structure(files_list):
    data = []
    for x in files_list:
        for y in x.functions:
            for z in make_list_of_functions(y.functions):
                second_module = find_model_of_function(files_list, z, x.name)
                if second_module == None:
                    continue
                for draw in data:
                    if draw[0] == x.name:
                        if draw[2] == second_module:
                            draw[4] += 1
                            break
                else:
                    data.append([x.name,"" , second_module, "", 1])

    return data


def make_list_of_functions(list):
    data = []
    for x in list:
        duplicate = 0
        for y in data:
            if y == x:
                duplicate = 1
                break
        if duplicate == 0:
            data.append(x)
    return data


def find_model_of_function(files_list, name, name_mod):
    for x in files_list:
        if name_mod == x.name:
            continue
        for y in x.functions:
            if y.name == name:
                return x.name

