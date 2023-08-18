import speedtest

def cc():
    print("Testing internet speed..........")
    st = speedtest.Speedtest()
    st.get_best_server()

    print("Testing downloading speed.....")
    download_speeed = st.download() / 10**6
    print(f"Downloading {download_speeed:.2f}")
    print("Testing uploading speed.....")
    upload_speed = st.upload() / 10**6
    print(f"Uploading {upload_speed:.2f}")

    print("Testing ping....")
    ping = st.results.ping
    print(f"Testing ping:{ping  }")


if __name__ == '__main__':

    cc()