import random, time

def main():
    print("Progress Bar Simulation")
    bytesDownloaded = 0
    downloadSize = 4096

    while bytesDownloaded < downloadSize:
        pb = ProgressBar()
        bytesDownloaded += random.randint(0, 100)

        barStr = pb.getProgressBar(bytesDownloaded, downloadSize)

        print(barStr, end="", flush=True)
        
        time.sleep(0.2)
       
        print("\b" * len(barStr), end="", flush=True)

class ProgressBar:
    barWidth = 0
    BAR = chr(9608)

    def __init__(self, barWidth: int = 40) -> None:
        self.barWidth = barWidth

    def getProgressBar(self, progress: int, total: int) -> str:
        
        progressBar = "["

        if (progress > total):
            progress = total
        elif (progress < 0):
            progress = 0

        numberOfBars = int((progress / total) * self.barWidth)

        progressBar += self.BAR * numberOfBars
        progressBar += ' ' * (self.barWidth - numberOfBars)
        progressBar += ']'

        progressBar += ' ' +  str(progress) + '/' + str(total)

        return progressBar


if __name__ == "__main__":
    main()

