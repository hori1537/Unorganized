

import ffmpeg
import glob
from pathlib import Path
import glob
import sys
import subprocess
import random 

folder_path = Path('F:\亀動画')
save_path = Path("D:\output")
mts_list = folder_path.glob("*.MTS")

musics_path = Path('music')
music_list = list(musics_path.glob("*.mp3"))


#print(mts_list)
for mts in mts_list:
    mts_name = str(mts.stem)

    minute = 3
    idxs = 45//3

    for t_idx in range(0,idxs):
        t_ = t_idx * minute * 60

        music_path = random.choice(music_list)
        print('music_path',music_path)
        music_stream = ffmpeg.input(str(music_path))
        music_audio  = music_stream.audio
        music_audio = music_audio.filter('afade', type='in', start_time=0, duration=10)
        music_audio = music_audio.filter('afade', type='out', start_time=minute*60-10, duration=10)
        #music_stream = music_stream.filter('afade', type='out', start_time=minute*60-5, duration=5)
    

        movie_stream = ffmpeg.input(str(mts), ss=t_ ,t= t_+minute*60)
        o_path = save_path /'{mts_name}_{t_idx}.MTS'.format(mts_name = mts_name, t_idx=t_idx)
        o_path = str(o_path)

        #movie_stream = ffmpeg.output(movie_stream,  o_path, ss=t_ ,t= t_+minute*60,  vcodec="copy")
        
        # music_stream,
        stream = ffmpeg.output(movie_stream.video, music_audio,o_path, ss=0 ,t= 0+minute*60 , vcodec="copy")
        stream = ffmpeg.overwrite_output(stream)
        ffmpeg.run(stream)

        try:
            ffmpeg.run(stream)
        except:
            print('error')
            print(mts)
            print(t_idx)
    sys.exit()




# reference
# https://shizenkarasuzon.hatenablog.com/entry/2019/06/15/012844
# https://blog.shikoan.com/pytube-ffmepg-concat-video-audio/
# https://qiita.com/satoshi2nd/items/4f6814b795a772af4af0
# https://github.com/kkroening/ffmpeg-python/tree/master/examples#audiovideo-pipeline
