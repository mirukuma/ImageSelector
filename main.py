import glob
import sys
import time
import cv2
import os



def main(input_path = "./input", output_path = "./output"):
    selected_file_names = sorted(glob.glob(output_path + "/*"))
    file_names = sorted(glob.glob(input_path + "/*"))

    i = 0
    if len(selected_file_names) > 0:
        i = file_names.index(input_path + '/' + selected_file_names[-1].split('/')[-1])
    good_image = []
    while i < len(file_names):
        img = cv2.imread(file_names[i])
        cv2.imshow(file_names[i],img)
        key = cv2.waitKey()
        img_name = file_names[i].split("/")[-1]
        if key == 48:
            #0キー GOOD画像
            if img_name not in  good_image:
                cv2.imwrite(output_path + "/" + img_name, img)
                good_image.append(img_name)
        elif key == 49:
            #1キー BAD画像
            if img_name in good_image:
                os.remove(output_path + "/" + img_name)
                good_image.remove(img_name)
        elif key == 50:
            #2キー 一個戻る
            i -= 2
        cv2.destroyAllWindows()
        i += 1

if __name__ == "__main__":
    input_path = sys.argv[1] if len(sys.argv) > 1 else None
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    main(input_path,output_path)