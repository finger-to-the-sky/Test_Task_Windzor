import json
import sys
import pandas as pd
import os


class FromGoogleCSVtoJSON:

    def __init__(self, link: str, fields: list, filename: str):
        self.link = link
        self.filename = filename
        self.fields = fields

    def parse(self):
        try:
            path = 'https://drive.google.com/uc?export=download&id=' + \
                   self.link.split('/')[-2]
            df = pd.read_csv(path)

            return (list(df.keys()), df.values)
        except Exception:
            print('Wrong URL entered')
            sys.exit(44)

    def take_data(self):
        data = self.parse()

        keys = data[0]
        result = {'data': []}
        values = data[1]
        needed_keys = list(set(self.fields) & set(keys))

        for ls in values:
            dicts = {}
            for key in needed_keys:
                dicts[keys[keys.index(key)]] = ls[keys.index(key)]
            result['data'].append(dicts)
        return result

    def write_to_json(self):
        result = self.take_data()
        try:
            os.mkdir(f'{os.getcwd()}/files')
        except FileExistsError:
            pass
        finally:
            with open(f'./files/{self.filename}.json', 'w', encoding='utf-8') as\
                    jsfile:
                results_json = json.dumps(result, indent=4)
                jsfile.write(results_json)

