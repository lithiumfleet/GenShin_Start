import pyautogui, numpy, cv2, time
from ffpyplayer.player import MediaPlayer
# time.sleep(5)
full_window_size = pyautogui.size()

# screen_image.show()

def get_screen_shoot():
    full_screen_image = pyautogui.screenshot(None, (0,0)+full_window_size)
    corped_area = (150, 150, full_screen_image.width-150, full_screen_image.height-150)
    screen_image = full_screen_image.convert('L').crop(corped_area)
    screen_image_array = numpy.array(screen_image)
    return screen_image_array


def is_white_image(image_array, delta=300000):
    sum_up = numpy.sum(image_array<240) 
    return numpy.abs(sum_up) < delta
    # return True


def play_video(video_path='GenShin480p.mp4'):
    video_window = 'GenShin'
    video=cv2.VideoCapture(video_path)
    player=MediaPlayer(video_path)
    fps = int(video.get(cv2.CAP_PROP_FPS))
    cv2.namedWindow(video_window, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(video_window, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.setWindowProperty(video_window, cv2.WND_PROP_TOPMOST, cv2.WINDOW_FULLSCREEN)
    while True:
        _, val = player.get_frame()
        grabbed, frame=video.read()
        cv2.imshow(video_window, frame)
        # print( val, grabbed, frame.shape)
        if val=='eof' or cv2.waitKey(fps) == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()


while True:
    time.sleep(0.5)
    screen_image_array = get_screen_shoot()
    state = is_white_image(screen_image_array)
    print(state,end='')
    if state == True:
        print('\b'*4+'Genshin, START!!')
        play_video()
        break
    else:
        print('\b'*5,end='')

# print(margain)

# print(screen_image_array)