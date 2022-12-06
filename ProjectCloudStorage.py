import dropbox
import os
import time


class TransferData:  
    def __init__(self,accessToken):
        self.accessToken = accessToken
    
    def upload_data(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.accessToken)

        for root,dirs,files in os.walk(file_from):
            for name in files:
                local_path = os.path.join(root,name)
                print(local_path)
                
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)
                print(relative_path)
                print(dropbox_path)
        
                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path)
           



def main():
    accessToken = "sl.BUbJz9avzVbCLkGtfOTru7vzIef1vNPb4J_YBZAQ2Nc9xJvBenvb9dIseD3fqawmsQt0xFnTOowFafGyf0Knmu-IelXSmjLwzTovC0LThF07tB8IGoHn3C0khYbRHx1bB8el0HZG_kgB"
    transferData = TransferData(accessToken)
    
    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to dropbox: ")

    transferData.upload_data(file_from,file_to)
    print("File has been uploaded")

if __name__ == '__main__':
    main()

