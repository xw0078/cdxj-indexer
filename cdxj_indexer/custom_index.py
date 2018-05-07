# TODO: java script search function

def javascript_index(record_body):
    #print(record_body)
    if "</script>" in record_body:
        #print("JS FOUND") #TEST
        return '1'
    else:
        #print("JS NOT FOUND")  # TEST
        return '0'

