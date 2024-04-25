import numpy as np
from scipy.signal import chirp
import matplotlib.pyplot as plt

def getInputData():
    # Chirp 신호 생성
    t = np.linspace(0, 10, 500)  # 시간 범위
    t2 = np.linspace(0, 20, 1000)
    f0 = 1  # 시작 주파수
    f1 = 25  # 끝 주파수
    chirp_signal = chirp(t, f0=f0, f1=f1, t1=10, method='linear')  # 선형 Chirp 신호 생성

    # 생성된 Chirp 신호의 최소값 보정
    chirp_signal -= np.min(chirp_signal)

    # 최대값을 1로 스케일링
    chirp_signal /= np.max(chirp_signal)

    #chirp_signal = np.hstack([chirp_signal, np.flip(chirp_signal)])

    left = list(chirp_signal)
    right = list(np.flip(chirp_signal))
    return left+right

if __name__=="__main__":
    # 생성된 Chirp 신호 시각화
    plt.plot(getInputData())
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()