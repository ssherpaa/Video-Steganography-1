import os

from stegano import lsb


def decode_string(video):
    # frame_extraction(video)
    secret = []
    root = '/Users/pasang/vid_frames/'
    # frame_direc = '/Users/tchiringlama/extraction/video_frames/1.png'
    # for i in range(len(os.listdir(root))):
    # f_name = "{}{}.png".format(root, i)
    f_name = video
    secret_dec = lsb.reveal(f_name)
    # if secret_dec is None:
    #     break
    print(secret_dec)
    # secret.append(secret_dec)
    # print(secret)


if __name__ == '__main__':
    # frame_direc = '/Users/tchiringlama/extraction/video_frames/1.png'
    frame_direc = '/Users/tchiringlama/PycharmProjects/Video-Steganography/tmp1/3.png'
    decode_string(frame_direc)
