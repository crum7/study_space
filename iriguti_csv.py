#!/usr/bin/env python
# -*- coding: utf8 -*-

from tkinter import font
from turtle import bgcolor, color
import gspread
import sys
import tkinter
from tkinter import *
from tkinter import ttk
import json
import time
import asyncio
from invoke import run
from sqlalchemy import null

import csv
import pprint

import pandas
import datetime


#google スプレッドシート
'''
#ServiceAccountC#FED965entials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountC#FED965entials 

#2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

#認証情報設定
#ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
c#FED965entials = ServiceAccountC#FED965entials.from_json_keyfile_name('/home/snowyowl/Downloads/spreadsheet-test-348013-a3cae18af3da.json', scope)

#OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(c#FED965entials)

#共有設定したスプレッドシートキーを変数[SPREADSHEET_KEY]に格納する。
SPREADSHEET_KEY = '1Mup6OsY9bRQTNYXiq0PlW4TYL44h8ZFMRpLSjepRjqA'

#共有設定したスプレッドシートのシート1を開く
worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

#A1セルの値を受け取る
import_value = worksheet.acell('A1').value
'''


#csvで出力
#カレントディレクトリに配置
csv_path = './sample.csv'
with open(csv_path, 'w') as worksheet:
    writer = csv.writer(worksheet)
    writer.writerow(['id','席の状況','席番号','入室時刻','退出時刻','在室時間'])
    writer.writerow([777, 777, 'XX'])


worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
# CSVで保存
worksheet_databaframe.to_csv(csv_path,index=False)







'''-------------------------------------------------------------------------------------------------
                 _   _             
  ___ __ _ _   _| |_(_) ___  _ __  
 / __/ _` | | | | __| |/ _ \| '_ \ 
| (_| (_| | |_| | |_| | (_) | | | |
 \___\__,_|\__,_|\__|_|\___/|_| |_|
    

csv内の値を変更、代入した場合はいちいち.to_csvでアップデートする必要あり。
csv内の値を参照、検索したいときは、関数毎で再読込する必要あり。


-------------------------------------------------------------------------------------------------
'''
    












#################################tkinter
root = tkinter.Tk()
root.geometry("800x1200")
root.configure(bg="white")

root.title(u"空席確認")

#frameを設定
frame_1 = Frame(root,bg="white")
frame_2 = Frame(root,bg="white")
loop = asyncio.get_event_loop()
cell_num = 2


#ラベル
static = tkinter.Label(frame_2, font=("",20),text=u'学生証のバーコードをスキャンしてください',bg="white",foreground="#707070")
kokuban = tkinter.Label(frame_2,text=u'                                                   黒板                                                   ',font=50,bg="#5A9BD5",foreground="white")
_1 = tkinter.Label(frame_1,text=u'1',font=10,bg="white",foreground="#707070")
_2 = tkinter.Label(frame_1,text=u'2',font=10,bg="white",foreground="#707070")
_3 = tkinter.Label(frame_1,text=u'3',font=10,bg="white",foreground="#707070")
_4 = tkinter.Label(frame_1,text=u'4',font=10,bg="white",foreground="#707070")
_5 = tkinter.Label(frame_1,text=u'5',font=10,bg="white",foreground="#707070")
_6 = tkinter.Label(frame_1,text=u'6',font=10,bg="white",foreground="#707070")
_7 = tkinter.Label(frame_1,text=u'7',font=10,bg="white",foreground="#707070")
_8 = tkinter.Label(frame_1,text=u'8',font=10,bg="white",foreground="#707070")

_A = tkinter.Label(frame_1,text=u'A',font=10,bg="white",foreground="#707070")
_B = tkinter.Label(frame_1,text=u'B',font=10,bg="white",foreground="#707070")
_C = tkinter.Label(frame_1,text=u'C',font=10,bg="white",foreground="#707070")
_D = tkinter.Label(frame_1,text=u'D',font=10,bg="white",foreground="#707070")
_E = tkinter.Label(frame_1,text=u'E',font=10,bg="white",foreground="#707070")










#エントリー
EditBox = tkinter.Entry(frame_2,font=("",20),foreground="#707070",bg="white")

#自動退出処理-----------------------------------------------------------------------------------------------------.bind()を使うんだって
def repeat(event):
    taisyutu()
    
    
#https://rait-09-kts.hatenablog.jp/entry/2021/07/04/212916
EditBox.bind('<Return>', repeat)















def A1_init():
    A1["bg"] = "white"
    A1["state"] = tkinter.NORMAL



def A2_init():
    A2["bg"] = "white"
    A2["state"] = tkinter.NORMAL





def A3_init():
    A3["bg"] = "white"
    A3["state"] = tkinter.NORMAL




def A4_init():
    A4["bg"] = "white"
    A4["state"] = tkinter.NORMAL




def A5_init():
    A5["bg"] = "white"
    A5["state"] = tkinter.NORMAL




def A6_init():
    A6["bg"] = "white"
    A6["state"] = tkinter.NORMAL





def B1_init():
    B1["bg"] = "white"
    B1["state"] = tkinter.NORMAL





def B2_init():
    B2["bg"] = "white"
    B2["state"] = tkinter.NORMAL





def B3_init():
    B3["bg"] = "white"
    B3["state"] = tkinter.NORMAL





def B4_init():
    B4["bg"] = "white"
    B4["state"] = tkinter.NORMAL





def B5_init():
    B5["bg"] = "white"
    B5["state"] = tkinter.NORMAL





def B6_init():
    B6["bg"] = "white"
    B6["state"] = tkinter.NORMAL






def C1_init():
    C1["bg"] = "white"
    C1["state"] = tkinter.NORMAL





def C2_init():
    C2["bg"] = "white"
    C2["state"] = tkinter.NORMAL




def C3_init():
    C3["bg"] = "white"
    C3["state"] = tkinter.NORMAL



def C4_init():
    C4["bg"] = "white"
    C4["state"] = tkinter.NORMAL




def C5_init():
    C5["bg"] = "white"
    C5["state"] = tkinter.NORMAL




def C6_init():
    C6["bg"] = "white"
    C6["state"] = tkinter.NORMAL




def D1_init():
    D1["bg"] = "white"
    D1["state"] = tkinter.NORMAL





def D2_init():
    D2["bg"] = "white"
    D2["state"] = tkinter.NORMAL




def D3_init():

    D3["bg"] = "white"
    D3["state"] = tkinter.NORMAL
    



def D4_init():
    D4["bg"] = "white"
    D4["state"] = tkinter.NORMAL




def D5_init():
    D5["bg"] = "white"
    D5["state"] = tkinter.NORMAL




def D6_init():
    D6["bg"] = "white"
    D6["state"] = tkinter.NORMAL





def E1_init():
    E1["bg"] = "white"
    E1["state"] = tkinter.NORMAL





def E2_init():
    E2["bg"] = "white"
    E2["state"] = tkinter.NORMAL





def E3_init():
    E3["bg"] = "white"
    E3["state"] = tkinter.NORMAL





def E4_init():
    E4["bg"] = "white"
    E4["state"] = tkinter.NORMAL





def E5_init():
    E5["bg"] = "white"
    E5["state"] = tkinter.NORMAL





def E6_init():
    E6["bg"] = "white"
    E6["state"] = tkinter.NORMAL
























# A1ボタンが押されるとここが呼び出される
#
def A1_check():

    
    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'A1',nowtime])
    
    

    
    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)

    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    A1["bg"] = "#FED965"
    A1["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)
        












# A2ボタンが押されるとここが呼び出される
#
def A2_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'A2',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    A2["bg"] = "#FED965"
    A2["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)











# A3ボタンが押されるとここが呼び出される
#
def A3_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'A3',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    A3["bg"] = "#FED965"
    A3["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)



# A4ボタンが押されるとここが呼び出される
#
def A4_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'A4',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    A4["bg"] = "#FED965"
    A4["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)


# A5ボタンが押されるとここが呼び出される

def A5_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'A5',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    A5["bg"] = "#FED965"
    A5["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)



# A6ボタンが押されるとここが呼び出される
#
def A6_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'A6',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    A6["bg"] = "#FED965"
    A6["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)






# B1ボタンが押されるとここが呼び出される

def B1_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'B1',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    B1["bg"] = "#FED965"
    B1["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)











# B2


def B2_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'B2',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    B2["bg"] = "#FED965"
    B2["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)













# B3ボタンが押されるとここが呼び出される


def B3_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'B3',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    B3["bg"] = "#FED965"
    B3["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)


# B4ボタンが押されるとここが呼び出される


def B4_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'B4',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    B4["bg"] = "#FED965"
    B4["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)












# B5ボタンが押されるとここが呼び出される


def B5_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'B5',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    B5["bg"] = "#FED965"
    B5["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)










# B6


def B6_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'B6',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    B6["bg"] = "#FED965"
    B6["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)












# C1ボタンが押されるとここが呼び出される


def C1_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'C1',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    C1["bg"] = "#FED965"
    C1["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)
















# C1ボタンが押されるとここが呼び出される

def C2_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'C2',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    C2["bg"] = "#FED965"
    C2["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)













# C3

def C3_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'C3',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    C3["bg"] = "#FED965"
    C3["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)











# C4

def C4_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'C4',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    C4["bg"] = "#FED965"
    C4["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)















# C5

def C5_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'C5',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    C5["bg"] = "#FED965"
    C5["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)














# C6
def C6_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'C6',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    C6["bg"] = "#FED965"
    C6["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)

















# D1ボタンが押されるとここが呼び出される

def D1_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'D1',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    D1["bg"] = "#FED965"
    D1["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)
















# D2

def D2_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'D2',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    D2["bg"] = "#FED965"
    D2["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)













# D3

def D3_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'D3',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    D3["bg"] = "#FED965"
    D3["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)











# D4

def D4_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()

    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'D4',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    D4["bg"] = "#FED965"
    D4["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)













# D5

def D5_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()

    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'D5',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    D5["bg"] = "#FED965"
    D5["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)



















# D6
def D6_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'D6',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    D6["bg"] = "#FED965"
    D6["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)
























# E1ボタンが押されるとここが呼び出される
def E1_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'E1',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    E1["bg"] = "#FED965"
    E1["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)













def E2_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'E2',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    E2["bg"] = "#FED965"
    E2["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)





















    
def E3_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'E3',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    E3["bg"] = "#FED965"
    E3["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)













    
def E4_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'E4',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    E4["bg"] = "#FED965"
    E4["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)

















    
def E5_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'E5',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    E5["bg"] = "#FED965"
    E5["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)













    
def E6_check():


    #ユーザーidを、セルに書き込む
    user_num = EditBox.get()
    nowtime = datetime.datetime.now()
    
    #aは、追記
    with open(csv_path, 'a') as worksheet:
        writer = csv.writer(worksheet)    
        writer.writerow([user_num,1,'E6',nowtime])

    worksheet_databaframe = pandas.read_csv(filepath_or_buffer = csv_path)
    # CSVで保存
    worksheet_databaframe.to_csv(csv_path,index=False)
    print("change color")

    #席の状況に応じて色変える
    E6["bg"] = "#FED965"
    E6["state"]  = "disable"

    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)





#更新
#退出処理されたものを更新する。
#席の状況が0のものを2に変えて、ボタンを初期化する
def update():

    worksheet_databaframe_update = pandas.read_csv(filepath_or_buffer = csv_path)
    
    #ゼロがcsv内にあるかどうかを調べる。resultにはリストが返される。
    result = worksheet_databaframe_update.query('席の状況 == 0')
        
        
    print(result.index.values)

    result_len = len(result)
    #リストの中の要素の数だけ、検索、削除を繰り返す。
    print(len(result))


        #0を2にすべて置き換える。
    for i in range(result_len):
        print('update')

        #退出した人の席の状況は、2にする。
        worksheet_databaframe_update.iloc[result.index.values[int(i)],1]=2


        find_value = worksheet_databaframe_update.iloc[result.index.values[int(i)],2]
        print(find_value)


            
        if find_value == 'A1':
            A1_init()
        elif find_value =='A2':
            A2_init()
        elif find_value == 'A3':
            A3_init()
        elif find_value == 'A4':
            A4_init()
        elif find_value == 'A5':
            A5_init()
        elif find_value == 'A6':
                A6_init()
        elif find_value == 'A2':
            A2_init()
        elif find_value == 'B2':
            B2_init()
        elif find_value == 'B3':
            B3_init()
        elif find_value == 'B4':
            B4_init()
        elif find_value == 'B5':
            B5_init()
        elif find_value == 'B6':
            B6_init()
        elif find_value == 'B1':
            B1_init()
        elif find_value == 'C2':
            C2_init()
        elif find_value == 'C3':
            C3_init()
        elif find_value == 'C4':
            C4_init()
        elif find_value == 'C5':
            C5_init()
        elif find_value == 'C6':
            C6_init()
        elif find_value == 'C1':
            C1_init()
        elif find_value == 'D2':
            D2_init()
        elif find_value == 'D3':
            D3_init()
        elif find_value == 'D4':
            D4_init()
        elif find_value == 'D5':
            D5_init()
        elif find_value == 'D6':
            D6_init()
        elif find_value == 'D1':
            D1_init()
        elif find_value == 'E2':
            E2_init()
        elif find_value == 'E3':
            E3_init()
        elif find_value == 'E4':
            E4_init()
        elif find_value == 'E5':
            E5_init()
        elif find_value == 'E1':
            E1_init()

    # CSVで保存
    worksheet_databaframe_update.to_csv(csv_path,index=False)
    #entryの中身をなくす
    EditBox.delete(0, tkinter.END)


    










#席の状況を1から0にする。
def taisyutu():


    
    #EditBox.get()は、str型で読み込まれるので、intに直してやる。
    user_num_taisyutu = int(EditBox.get())
    worksheet_databaframe_taisyutu = pandas.read_csv(filepath_or_buffer = csv_path)

    #ゼロがcsv内にあるかどうかを調べる。resultにはリストが返される。
    #pandasの中で変数を使うときは、変数の前に@をつける。
    some_user = worksheet_databaframe_taisyutu.query('id == @user_num_taisyutu')
    
    print(some_user.index.values[0])
    print(some_user.index)



    #退出する人の席の状況を1にする。
    worksheet_databaframe_taisyutu.iloc[some_user.index.values[0],1]=0


    #また、退出した人のユーザーのidの先頭に、退出済みとして書き込む
    worksheet_databaframe_taisyutu.iloc[some_user.index.values[0],0]=user_num_taisyutu+10000

    #退出した時間を追記
    now_time_2 = datetime.datetime.now()
    worksheet_databaframe_taisyutu.iloc[some_user.index.values[0],4]=now_time_2

    #自習室にいた時間
    #自習室に入った時間をcsvから持ってくる。ここでは、datetime.datetime.now()で得られたデータをstrとして扱う。
    in_time = worksheet_databaframe_taisyutu.iloc[some_user.index.values[0],3]
    out_time = str(now_time_2)

    #在室時間を計算するための処理
    #in_timeをシフトで日付と時間で分ける。  日付は[0]に、時間は[1]に格納される。
    re_in_time = in_time.split(' ')
    re_out_time = out_time.split(' ')
    
    #更に時間、分、秒に分ける。
    cal_in_time = re_in_time[1].split(':')
    cal_out_time = re_out_time[1].split(':')
    print(cal_in_time,cal_out_time)

    #計算 秒は、整数値のみ
    cal_time = int(cal_out_time[0]) - int(cal_in_time[0])
    cal_minute = int(cal_out_time[1]) - int(cal_in_time[1])
    cal_seconds = int(float(cal_out_time[2])) - int(float(cal_in_time[2]))

    cal_all = str(cal_time)+':'+str(cal_minute)+':'+str(cal_seconds)

    print(cal_all)
    

    #csvに書き込み
    worksheet_databaframe_taisyutu.iloc[some_user.index.values[0],5]=cal_all

    
    

    worksheet_databaframe_taisyutu.to_csv(csv_path,index=False)

    update()
    














    
























#更新ボタン
taisyutu_button = tkinter.Button(
    frame_2,
    height = 2,
    width=4,
    text='退出',
    command = lambda: taisyutu(),
    font=('',10),
    #relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#FED965", 
    highlightcolor= "#FED965",
    bg="#5A9BD5",
    foreground="white"
    
    )








# A1の席

A1 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: A1_check(),
    font=('',20),
    bg="white",
    #relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )



# A2の席

A2 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: A2_check(),
    font=('',20),bg="white",#relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )


# A3の席

A3 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: A3_check(),
    font=('',20),bg="white",#relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )


# A4の席

A4 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: A4_check(),
    font=('',20),bg="white",#relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )



# A5の席

A5 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: A5_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )


# A6の席

A6 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: A6_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )



# B1の席

B1 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: B1_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )


# B2の席

B2 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: B2_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )


# B3の席

B3 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: B3_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    )

# B4の席

B4 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: B4_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )

# B5の席

B5 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: B5_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )

# B6の席

B6 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: B6_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )



# C1の席


C1 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: C1_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )


# C1の席


C2 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: C2_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )



# C1の席


C3 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: C3_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )


# C1の席


C4 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: C4_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )


# C1の席


C5 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: C5_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )


# C1の席


C6 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: C6_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )

# D1の席


D1 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: D1_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )

D2 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: D2_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )


D3 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: D3_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )


D4 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: D4_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )


D5 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: D5_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )


D6 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: D6_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )



# E1の席
E1 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: E1_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )


# E1の席
E2 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: E2_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )


# E1の席
E3 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: E3_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )


# E1の席
E4 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: E4_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )


# E1の席
E5 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: E5_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )


# E1の席
E6 = tkinter.Button(
    frame_1,
    height = 3,
    width=6,
    command = lambda: E6_check(),
    font=('',20),bg="white",relief=tkinter.FLAT,
    highlightthickness=4,
    highlightbackground = "#6A9CCF", 
    highlightcolor= "#6A9CCF"
    
    )















# Layoutcolumn

frame_2.grid(row=0, column=0)
static.grid(row = 0,column=1,padx=5,pady=5)
EditBox.grid(row = 1,column=1,padx=5,pady=5,ipadx=60, ipady=20)
kokuban.grid(row = 2,column=1,padx=5,pady=5)
frame_2.grid()

frame_1.grid(row=2, column=0)
_1.grid(row = 4, column=1,padx=5,pady=5)
_2.grid(row = 5, column=1,padx=5,pady=5)
_3.grid(row = 6, column=1,padx=5,pady=5)
_4.grid(row = 7, column=1,padx=5,pady=5)
_5.grid(row = 8, column=1,padx=5,pady=5)
_6.grid(row = 9, column=1,padx=5,pady=5)

_A.grid(row = 3, column=2,padx=5,pady=5)
_B.grid(row = 3, column=3,padx=5,pady=5)
_C.grid(row = 3, column=4,padx=5,pady=5)
_D.grid(row = 3, column=5,padx=5,pady=5)
_E.grid(row = 3, column=6,padx=5,pady=5)

A1.grid(row=4, column=2,padx=5,pady=5)
A2.grid(row=5, column=2,padx=5,pady=5)
A3.grid(row=6, column=2,padx=5,pady=5)
A4.grid(row=7, column=2,padx=5,pady=5)
A5.grid(row=8, column=2,padx=5,pady=5)
A6.grid(row=9, column=2,padx=5,pady=5)
B1.grid(row=4, column=3,padx=5,pady=5)
B2.grid(row=5, column=3,padx=5,pady=5)
B3.grid(row=6, column=3,padx=5,pady=5)
B4.grid(row=7, column=3,padx=5,pady=5)
B5.grid(row=8, column=3,padx=5,pady=5)
B6.grid(row=9, column=3,padx=5,pady=5)
C1.grid(row=4, column=4,padx=5,pady=5)
C2.grid(row=5, column=4,padx=5,pady=5)
C3.grid(row=6, column=4,padx=5,pady=5)
C4.grid(row=7, column=4,padx=5,pady=5)
C5.grid(row=8, column=4,padx=5,pady=5)
C6.grid(row=9, column=4,padx=5,pady=5)
D1.grid(row=4, column=5,padx=5,pady=5)
D2.grid(row=5, column=5,padx=5,pady=5)
D3.grid(row=6, column=5,padx=5,pady=5)
D4.grid(row=7, column=5,padx=5,pady=5)
D5.grid(row=8, column=5,padx=5,pady=5)
D6.grid(row=9, column=5,padx=5,pady=5)
E1.grid(row=4, column=6,padx=5,pady=5)
E2.grid(row=5, column=6,padx=5,pady=5)
E3.grid(row=6, column=6,padx=5,pady=5)
E4.grid(row=7, column=6,padx=5,pady=5)
E5.grid(row=8, column=6,padx=5,pady=5)
E6.grid(row=9, column=6,padx=5,pady=5)





root.mainloop()







