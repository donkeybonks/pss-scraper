import urllib.request
from util import *
from xml.dom import minidom

# Constants
FILES_URL = r'http://api2.pixelstarships.com/FileService/ListFiles2?deviceType=DeviceTypeiPhone'
AWS_URL = r'http://pixelstarships.s3.amazonaws.com/'

class File:
    def __init__(self, source):
        self.Id = source.attributes['Id'].value
        self.Filename = source.attributes['Filename'].value
        self.DateUpdated = source.attributes['DateUpdated'].value
        self.FileDownloadCategory = source.attributes['FileDownloadCategory'].value
        self.AwsFilename = source.attributes['AwsFilename'].value

    def __repr__(self):
        str = "{{ File {0}: ".format(self.Id)
        str += "Filename='{0}', ".format(self.Filename)
        str += "DateUpdated='{0}', ".format(self.DateUpdated)
        str += "FileDownloadCategory='{0}', ".format(self.FileDownloadCategory)
        str += "AwsFilename='{0}' }}".format(self.AwsFilename)
        return str

    def id(self):
        return int(self.Id)

    def filename(self):
        return str(self.Filename)

    def remote_filename(self):
        return AWS_URL + str(self.AwsFilename)


# Load files from remote as a list
def load_files():
    with urllib.request.urlopen(FILES_URL) as response:
        source = response.read()
    source = source.decode("utf-8")
    xmldoc = minidom.parseString(source)
    for file in xmldoc.getElementsByTagName('File'):
        yield File(file)

# Return a dictionary of files loaded and keyed by id
def files_dictionary():
    files = load_files()
    return dict((file.id(), file) for file in files)

# Pass file as File
def save_file(file):
    url = file.remote_filename()
    urllib.request.urlretrieve(url, "files/" + file.filename())

