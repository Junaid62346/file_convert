import ffmpeg
# import os

def video_to_gif():
    # for file in os.listdir("video"):
    #     if file.endswith((".mp4", ".MP4")):
    #         file_name = file.split(".")[0]
    #         print(file_name)
    #         gif_file = file_name + ".gif"

            stream = ffmpeg.input("название_файла") #тут указываем путь до файла
            # stream = ffmpeg.filter(stream, "fps", fps=5) # здесь можно указать фпс и другие атрибуты если нужно получить gif
            stream = ffmpeg.output(stream, "название выходного_файла") # здесь пишем откуда брать видео и как его сохранить (в каком формате)
            ffmpeg.run(stream)

def main():
    video_to_gif()

if __name__ == "__main__":
    main()




