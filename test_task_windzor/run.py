from сonversion.converter import FromGoogleCSVtoJSON
from сonversion.fields import fields_gen

link = 'https://drive.google.com/file/d/1zLdEcpzCp357s3Rse112Lch9EMUWzMLE/view'

filename = 'data'


if __name__ == '__main__':
    my_json = FromGoogleCSVtoJSON(link, fields_gen(), filename)
    my_json.write_to_json()

