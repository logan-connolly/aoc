import re


def validate(pass_dict, full_check=False):
    """Check that not only all fields are present, but that content is valid"""

    def validate_keys():
        required_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
        key_diff = required_keys - set(pass_dict.keys())
        if len(key_diff) > 1:
            return False
        if len(key_diff) == 1:
            return "cid" in key_diff
        return True

    def validate_ecl():
        return pass_dict["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    def validate_hcl():
        return re.fullmatch(r"^#(?:[0-9a-fA-F]{3}){1,2}$", pass_dict["hcl"]) is not None

    def validate_hgt():
        hgt = pass_dict["hgt"]
        try:
            hgt_val, _ = hgt.split("cm") if "cm" in hgt else hgt.split("in")
            hgt_min, hgt_max = (150, 193) if "cm" in hgt else (59, 76)
            return hgt_min <= int(hgt_val) <= hgt_max
        except ValueError:
            return False

    def validate_pid():
        return len(pass_dict["pid"]) == 9

    def validate_range(key, min_val, max_val):
        return min_val <= int(pass_dict[key]) <= max_val

    if validate_keys():
        if full_check:
            return all(
                [
                    validate_ecl(),
                    validate_hcl(),
                    validate_hgt(),
                    validate_pid(),
                    validate_range("byr", 1920, 2002),
                    validate_range("iyr", 2010, 2020),
                    validate_range("eyr", 2020, 2030),
                ]
            )
        return True
    return False
