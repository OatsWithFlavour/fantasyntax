from processes.substitution import substituiere, ersetze

def change_text(text, regex_dict, bedingungs_dict, ersatz_dict):
    for name, pattern in regex_dict.items():
        if name in bedingungs_dict:
            condition_list = bedingungs_dict[name]
            for condition in condition_list:
                env_muster = regex_dict[condition]
                com_muster = pattern
                com_ersatz = ersatz_dict[name]
                text = substituiere(text, env_muster, com_muster, com_ersatz)
    for name, pattern in regex_dict.items():
        if name not in bedingungs_dict:
            ersatz = ersatz_dict[name]
            text = ersetze(text, pattern, ersatz)
    return text
