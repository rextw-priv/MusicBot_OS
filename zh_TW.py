greeting = """
✋ 歡迎來到棒棒勝 Music 的 Bot ! 🎧
輸入關鍵字來搜尋音樂資料庫，傳送音樂檔案以增加至資料庫。
輸入 `/help` 來獲取說明!
** 丟進本 Bot 的音樂不會同步到頻道唷!只有頻道的會同步過來 owo **
"""

help = """
輸入關鍵字來搜尋音樂資料庫。
在關鍵字後輸入`type:TYPE`來限定音樂格式，像這樣:
```棒棒勝 type:flac```
```棒棒勝 type:mp3```
```棒棒勝 type:mpeg```
若同時想搜尋作者和曲名，請用 `>` 隔開 (預設為作者、曲名都納入搜尋)，像這樣:
```棒棒勝>洨安之歌```
也可以搭配`type`指令，像這樣:
```棒棒勝>洨安之歌 type:flac```
輸入 `/stats` 來獲取 bot 資訊。
用 `/music` 指令來在群聊內使用棒棒勝 Music Bot，像這樣:
`/music 棒棒勝`
對於一個音樂文件回覆 `/add` 來新增至資料庫。
此外，本 bot 也支援 inline mode。
在所有地方輸入 `@music_Index_bot` 加空格後便可搜尋音樂。
"""

not_found = """
找不到資料 :/
"""
    
texts = {
    'tagNotFound': "傳送失敗...是不是你的音樂檔案少了資訊標籤? :("
    'musicExists': "資料庫裡已經有這首囉 owo"
    'sentExistedMusic': lambda sender, artist, title: str(sender) +" 傳送了重複的歌曲 "+ str(artist) +" - "+ str(title)
    'replaced': "檔案大小較資料庫內的大，已取代!"
    'sentLargerMusic': lambda sender, artist, title: str(sender) + " 傳送了大小較大的歌曲 " + str(artist) + " - " + str(title)
    'addMusic': lambda sender, artist, title: str(sender) + " 新增了 " + str(artist) + " - " + str(title)
    'inquiredAdminListRefused': lambda user: str(user) + ' 查詢了管理員名單，遭到拒絕。'
    'denied': "存取遭拒。"
    'inquiredAdminList': lambda user: str(user) + ' 查詢了管理員名單'
    'deleteRefused': lambda user, keyword: str(user) + ' 意圖刪除 ' + str(keyword) + '，遭到拒絕。'
    'deleteNumTypeArt': lambda sender, num, type, artist, title: str(sender) + " 刪除了 " + str(num) + ' 個 ' + str(type).upper() + " 格式的 " + str(artist) + "的" + str(title)
    'deleteNumArt': lambda sender, num, artist, title: str(sender) + " 刪除了 " + str(num) + ' 個 '  + str(artist) + "的" + str(title)
    'deleteNumType':lambda sender, num, type, keyword: str(sender) + " 刪除了 " + str(num) + ' 個 '  + str(type).upper() + " 格式的 " + str(keyword)
    'deleteNum': lambda sender, num, keyword: str(sender) + " 刪除了 " + str(num) + ' 個 '  + str(keyword)
    'deleteError': "刪除元素個數有問題RRR"
    'nextPage': "下一頁"
    'searchTypeArt': lambda sender, type, artist, title: str(sender) + " 搜尋了 " + str(type).upper() + " 格式的 " + str(artist) + "的" + str(title)
    'searchArt': lambda sender, artist, title: str(sender) + " 搜尋了 " + str(artist) + "的" + str(title)
    'searchType': lambda sender, type, keyword: str(sender) + " 搜尋了 " + str(type).upper() + " 格式的 " + str(keyword)
    'search': lambda user, keyword: str(user) + " 搜尋了 " + str(keyword)
    'searchError': "元素個數有問題RRR"
    'newUser': lambda user: "新用戶 " + str(user)
    'exit': lambda user: str(user) + " 退出了"
    'bye': "掰掰! 😢"
    'statsNotReady': "統計資訊還沒好!"
    'musicCalc': lambda count, size: str(count) + '首歌曲' + str(size)
    'unknownArtist': "未知藝術家"
    'untitled': "無標題"
    }