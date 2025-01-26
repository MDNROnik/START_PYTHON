import os


if __name__ == '__main__':
    print(" Welcome To The Robot Speaker ")
    while(1):
        n = input("Enter what you want me say or you want to stop this process then type \"end\"? ")
        if( n.lower() == "end"):
            break
        command = f"mshta vbscript:Execute(\"CreateObject(\"\"SAPI.SpVoice\"\").Speak(\"\"{n}\"\")(window.close)\")"
        os.system(command)
