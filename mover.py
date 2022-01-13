import os
import shutil

source = "/home/yzhang24/spatiotemporal-open-surgery/1945/1945/youtube-videos"
final_dest = "/home/yzhang24/spatiotemporal-open-surgery/1945/1945/youtube-videos/already_done"
batch_list = "/home/yzhang24/spatiotemporal-open-surgery/1945/1945/json_to_transfer/extract.txt"
with open(batch_list) as batch:
        list = []
        list = (batch.read())
        list = list.splitlines()
        for f in os.listdir(source):
                #print(f)
                for item in list:
                        print("searching for ",item, "in ",f)
                        if item in f:
                                 print("found!")
                                 shutil.move(f,final_dest)
                                 print("moved!")
                        else:
                                print("")
                                #print(f)
                                #print(item)
