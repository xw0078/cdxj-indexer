from warcio.archiveiterator import ArchiveIterator

with open("/Users/Xinyue/Google Drive/DLRL/Projects/Web_archive/my_cdxj/data/IAH-20080430204825-00000-blackbook.warc.gz", 'rb') as stream:
    for record in ArchiveIterator(stream):
        if record.rec_type == 'response':
            print(record.rec_headers.get_header('WARC-Target-URI'))
            print(record.raw_stream.read())