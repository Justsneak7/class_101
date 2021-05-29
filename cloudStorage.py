import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'b5SdnNd892AAAAAAAAAAAe72wyG_fQLjCllx9K8phBmQ6DqyRTvPqBojyW2bTw8b'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer :-")
    file_to = input("enter the full path to upload to dropbox:- ")  

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()