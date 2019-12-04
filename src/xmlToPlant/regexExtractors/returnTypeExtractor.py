import re


class ReturnTypeExtractor:

    @staticmethod
    def extract_type(xml_string) -> str:
        regex = re.compile('\)*:\s*\w+')
        list_of_types = regex.findall(xml_string)
        # print(list_of_types)
        if ')' in list_of_types[-1]:
            return list_of_types[-1].split(':')[1].lstrip()

        return list_of_types[-1][2:].lstrip()