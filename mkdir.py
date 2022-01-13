import ffmpeg
import os
import shutil

# Strip the file string name to exclude the file extension

##FILE_CLEAN = YOUR_FILE.strip(".mp4")


# From a folder full of videos...

source = "/Users/yilunzhang/test_source_2"

source_files = os.listdir(source)

for file in source_files:
    print(file)
    os.chdir(source)
    if file.endswith('.mp4'):
        print("Here is a video!")
        print(file)
        clean_file = file.strip(".mp4")
        os.mkdir(clean_file)
        print("Dir made!")
        new_dir = source + "/" + clean_file
        print(new_dir)
        # Now we move the file into its new folder
        shutil.move(file,new_dir)
        print("moved!")
        # Now we specify the file to extract frames
        YOUR_FILE = new_dir + "/" + file
        print(YOUR_FILE)
        # Now we add the frame extraction
        ## First we change the working dir
        os.chdir(new_dir)

        probe = ffmpeg.probe(YOUR_FILE)
        time = float(probe['streams'][0]['duration']) // 2
        width = probe['streams'][0]['width']
        parts = 10

        intervals = time // parts
        intervals = int(intervals)
        interval_list = [(i * intervals, (i + 1) * intervals) for i in range(parts)]
        i = 0

        for item in interval_list:
            (
                ffmpeg
                .input(YOUR_FILE, ss=item[1])
                .filter('scale', width, -1)
                .output('frame' + str(i) + '_' + clean_file + '.jpg', vframes=1)
                .run()
            )
            i += 1
        print('done!')










## Move corresponding extracted frames into that folder 