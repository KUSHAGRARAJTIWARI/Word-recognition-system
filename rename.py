#import os module for using rename method and listdir
import os
#method which handle all the operation regarding rename the file.
def rename_files():
    #variable initialization
    os.chdir('D:/train_images')
    i=0
    #loop to travel all the file of given folder ravi.
    for file_name in os.listdir():
        #new name of  the file should be like newname1.html...
        dstination="Aa" + str(i) + ".jpg"
        source=file_name
        
        #rename function calls to rename the files.
        os.rename(source, dstination)
        #variable increment to differenciate the all files like newname1.html
        #,newname2.html ..... so on.
        i += 1
    print("All files has been renamed successfully...")    
#rename_files method call.
rename_files()