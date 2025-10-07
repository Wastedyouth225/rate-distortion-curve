import matplotlib.pyplot as plt

bitrates = [130, 310, 660, 1071, 1931, 4591]  # kbps для 144p, 240p, 360p, 480p, 720p, 1080p
vmaf_scores = [6.55, 39.72, 63.42, 75.71, 87.49, 95.59]  # Средние VMAF
resolutions = ['144p', '240p', '360p', '480p', '720p', '1080p']

plt.plot(bitrates, vmaf_scores, 'o-')
plt.xlabel('Битрейт (kbps)')
plt.ylabel('Средний VMAF')
plt.title('Кривая rate-distortion для Big Buck Bunny (h264)')
for i, txt in enumerate(resolutions):
    plt.annotate(txt, (bitrates[i], vmaf_scores[i]), textcoords="offset points", xytext=(0,10), ha='center')
plt.grid(True)
plt.savefig('rate_distortion_curve.png')  # Сохранит как PNG-файл
plt.show()