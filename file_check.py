import glob
import os
import sys

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


class Application(Frame):
    """ File Name Judgment Class """

    def __init__(self,master):
        super().__init__(master)

        # ウィジェット非表示
        master.withdraw()

        # フォルダ選択ダイアログの表示
        absPath = os.path.abspath(os.path.dirname(__file__))
        messagebox.showinfo('○×プログラム','ファイルが存在するかを確認します')
        dirPath = filedialog.askdirectory(initialdir = absPath)

        # フォルダの中身を処理
        file_collection = dirPath + '/' + '*'
        filepath = glob.glob(file_collection)
        fileslist = [os.path.basename(f) for f in filepath]

        filejudge = {'file1': 'no', 'file2': 'no','file3': 'no','file4': 'no','file5': 'no'}
        file_list = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt']


        # ファイル名が正しいかをチェック
        try:
            if file_list[0] in fileslist:
                filejudge['file1'] = 'ok'
            if file_list[1] in fileslist:
                filejudge['file2'] = 'ok'
            if file_list[2] in fileslist:
                filejudge['file3'] = 'ok'
            if file_list[3] in fileslist:
                filejudge['file4'] = 'ok'
            if file_list[4] in fileslist:
                filejudge['file5'] = 'ok'

            not_name_file = [file_list[idx] for idx, val in enumerate(filejudge.values()) if val == 'no']
            not_file = '  '.join(not_name_file)

            # 処理ファイル名の出力
            messagebox.showinfo(
                'ファイル名判定プログラム',
                'file1.txt : {}\r'.format(filejudge['file1']) +
                'file2.txt : {}\r'.format(filejudge['file2']) +
                'file3.txt : {}\r'.format(filejudge['file3']) +
                'file4.txt : {}\r'.format(filejudge['file4']) +
                'file5.txt : {}\r'.format(filejudge['file5']) +
                '==============================\r' +
                'ファイル名が間違ってます。または、ファイル名が存在しません。\r' +
                '{}\r'.format(not_file) +
                '==============================\r'
            )
            sys.exit()
        except Exception:
            sys.exit()

if __name__ == "__main__":
    win = Tk()
    app = Application(master=win)
    app.mainloop()
