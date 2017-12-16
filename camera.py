import cv2


###########################################################
# CLIENT KAMERA - INITIALISASI OBJECT
###########################################################
# Image processingnya bisa di taroh di sini, terus hasilnya
# balikin ke object buat di upstream nanti

class VideoCamera(object):

    # Fungsi untuk inisialisasi kamera client
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    # Fungsi untuk melepas koneksi camera client bila sudah tidak digunakan
    def __del__(self):
        self.video.release()

    # menggisi object dengan hasil capture dari kamera untuk di upstream
    def get_frame(self):
        # succes capture video
        success, image = self.video.read()

        # taruh algoritma image processingnya di bawah sini <(^0^<)

        # conver gambar untuk di upstream
        ret, jpeg = cv2.imencode('.jpg', image)

        # balikin hasil nya ke object untuk di upstream
        return jpeg.tobytes()
