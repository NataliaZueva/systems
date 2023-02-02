import json
import whois


def is_domain_available(domain_name):
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)


def get_available_domen(domen_list):
    available_domen = []
    for domain in domen_list:
        if is_domain_available(domain):
            available_domen.append(domain)
            print(domain)
    return available_domen


def get_domen_from_json(json_file_path):
    text = json.load(open(json_file_path, encoding="UTF-8"))
    today_reg_list = text["2022-12-12"]
    domen_list = []

    for site in today_reg_list:
        for url in site["urls"]:
            if "https" in url:
                domain = url.split('/')[2]
                if domain not in domen_list:
                    domen_list.append(domain)

    return domen_list


domen = json.load(open("d_list.json", encoding="UTF-8"))
available_domen_list = get_available_domen(domen)
print(available_domen_list)