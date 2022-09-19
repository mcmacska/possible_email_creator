import json


def possible_email_creator(name, domain, year):
    e_list = []

    name = str(name).lower().split(" ")

    username1 = ""
    for i in name:
        username1 += i

    username2 = ""
    name.reverse()
    for i in name:
        username2 += i

    # print(username1)
    # print(username2)

    e_list.append(f"{username1}@{domain}")
    e_list.append(f"{username2}@{domain}")

    for z in range(0, 32):
        e_list.append(f"{username1}{z}@{domain}")
        e_list.append(f"{username2}{z}@{domain}")

    for i in range(0, 10):
        e_list.append(f"{username1}0{i}@{domain}")
        e_list.append(f"{username2}0{i}@{domain}")
        # for l in range(0, 32):
        #     e_list.append(f"{username1}{k}@{domain}")
        #     e_list.append(f"{username2}{k}@{domain}")

    e_list.append(f"{username1}{year}@{domain}")
    e_list.append(f"{username2}{year}@{domain}")

    return e_list


def file_reader(path_):
    f = open(path_, "r")
    content = f.read()
    f.close()
    return content


def file_writer(path_, content_):
    f = open(path_, "w")
    f.write(content_)
    f.close()


def file_appender(path_, content_):
    f = open(path_, "a")
    f.write(content_)
    f.close()


def json_loader(path_):
    content_json = json.loads(file_reader(path_))
    return content_json


# main
if __name__ == "__main__":

    json_data_path = "data.json"

    json_content = json_loader(json_data_path)

    path = "emails_to_search.txt"

    email_list = possible_email_creator(json_content["Name"], json_content["Domain"], json_content["Year"])

    for k in email_list:
        file_appender(path, f"{k}\n")
