⭐Linked List 連結串列 練習

簡介:

這次是用 Python 寫的 Linked List 練習

其中包含:

LeetCode 自解與最優解仿寫

Linked List反轉字串

Linked List找中間節點

Linked List找倒數第K個節點

Linked List取偶數段陣列

✔️python 3.12 ✔️模組化結構

專案結構:
```
interview_project
        ├─ leetcode_best.py (LeetCode最優解仿寫)
        ├─ leetcode_mine.py (LeetCode自解)
        ├─ linked_mid.py (找中間節點)
        ├─ linked_mid2.py (找倒數第K個節點)
        ├─ linked_reverse.py (字串反轉)
        ├─ linked_odd.py (取偶數段陣列)
        ├─ problem.py (無解問題紀錄)
        └─ README.md (程式簡介)
```

※ 無解紀錄問題說明:

在problem.py裡,程式碼尾端有#字號的標記是搞不懂的地方

curr=[] #
even.append(curr) #

理論上這樣會讓空陣列被放進even,但是輸出結果是even裡沒有空陣列,全都是正確的陣列

而只要調換順序將curr放在even.append(curr)的下方,就出現空陣列,且even裡的陣列不是我要的結果

這是我想不明白的地方,求助幾個AI也都沒有給出答案,只是一直修改順序,重複上面兩行的流程而已

因此暫時紀錄,若有幸有這個機會,還請幫助我解決這個問題,謝謝!

使用方法:

( Git Clone用網址 https://github.com/Frank-Pon/Linked_List.git ) clone之後 ->  在終端機輸入 python linked_mid.py ->  開始使用 ✅

專案學習心得:

在刷LeetCode題目的時候,第一次真正遇到遇到Linked List這種資料結構

雖然之前在GOOGLE或是YOUTUBE有了解過資料結構相關內容

但實際遇到的時候還是腦筋一片空白

一開始只把他當成一般的List來處理

結果就是一直沒辦法過關

在經過ChatGPT解釋病互動練習之後,才理解Linked List的邏輯及操作

一開始在自解的時候還是採用轉成List處理過後再轉回Linked List

而在經過幾個練習,熟悉了之後再回去仿寫一次,就只剩下一些小地方卡住

這樣修修改改,偶爾停下來思考邏輯還有寫法真的學得很快

而在這次練習也順利的學會基本語法及概念了,非常開心又將一項新的東西給放進腦袋了。