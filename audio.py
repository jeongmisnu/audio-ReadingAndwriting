from time import sleep
import librosa.display
import numpy as np
import soundfile as sf
from pydub import AudioSegment
import matplotlib.pyplot as plt


path = "audio/뮤즈블라썸_어쿠스틱_코믹_호른(릴스).wav"
path1 = "test/뮤즈블라썸_어쿠스틱_코믹_호른(릴스).mp3"
path2 = "audio/뮤즈블라썸_어쿠스틱_코믹_호른_릴스_.ogg"
dst = "audio/Preview_뮤즈블라썸_EDM_테크노.wav"
dst1 = "audio/StarWars60.wav"
dst2 = "audio/StarWars3.wav"

test = "test/Preview_뮤즈블라썸_EDM_테크노.mp3"
test1 = "test/Preview_뮤즈블라썸_EDM_테크노.wav"

message = '10010001100111000100110000011101100000111000001110010010010101011001010100101000'

select = path
# sfo = sf.SoundFile(select)
# print(sfo)

# y, sr = sf.read(select)
# print('soundFile', y, sr)

# print([i[0] for i in y])

# dtype = ''
# if int(sfo.subtype[-2:]) <= 32:
#     dtype = 'float' + '32'

# else:
#     dtype = 'float' + '64'
sr = librosa.get_samplerate(select)
y, sr = librosa.load(select, sr=sr, mono=False, dtype='float64')
print('librosa', y, sr)


duration = librosa.get_duration(y=y, sr=sr)
print('duration', duration)
# y = [i[0] for i in y]

STFTData = librosa.stft(y, n_fft=512, hop_length=480,
                        win_length=512, center=True)
STFTDataMag = np.abs(STFTData)
STFTDataPhs = np.angle(STFTData)


MagShape = STFTDataMag.shape

print('MagShape', MagShape)
print('STFTDataMag', STFTDataMag)
# print('STFTDataPhs', STFTDataPhs)

data = []

if len(MagShape) == 3:
    yNum = MagShape[1]//4

    dataLen = 0
    for y in range(1, 4):
        for i in range(0, MagShape[1]-1):
            if i % 5 == 0:
                data.append([str('%.5f' % STFTDataMag[0][i][yNum*y]),
                            str('%.5f' % STFTDataMag[1][i][yNum*y])])
                # data.append(str('%.5f' % STFTDataMag[i][128]))
                # print('MagShape Index: {}'.format(i))
                dataLen += 1

            if dataLen == len(message):
                break
        if dataLen == len(message):
            break

else:
    yNum = MagShape[0]//4

    dataLen = 0
    for y in range(1, 4):
        for i in range(0, MagShape[0]-1):
            if i % 5 == 0:
                data.append(str('%.5f' % STFTDataMag[i][yNum*y]))
                # data.append(str('%.5f' % STFTDataMag[i][128]))
                # print('MagShape Index: {}'.format(i))
                dataLen += 1

            if dataLen == len(message):
                break
        if dataLen == len(message):
            break

print(data)


# audSeg = AudioSegment.from_wav(dst)
# audSeg.export(dst1, format="mp3")

# audSeg = AudioSegment.from_mp3(test)
# audSeg.export(test1, format="wav")

# sfo = soundfile.read(test, format='mp3')
# print(sfo)

'''
librosa.load()

path: 파일경로
sr: 샘플링 속도
mono: 신호를 모노로 변환
offset: 이 시점부터 파일을 읽습니다 (단위: 초)
duration: 여기까지 파일을 읽어옵니다 (단위: 초)
dtype: 데이터 유형
res_type: 리샘플링 유형(참고 참조)

Returns
y: np.ndarray [shape=(n,) or (…, n)]
srnumber > 0 [scalar]
'''
