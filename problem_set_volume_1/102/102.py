#!/bin/python3
"""
這題的目標是要把瓶子分類
輸入:123456789
123一組456一組789一組
數字順序分別是三個顏色G B C
要把同個顏色的瓶子放到同一組，要找最小步數
所以可能是147 258 369這樣的放置方式
但是要直接計算移動的瓶子數量太久了，所以直接用反過來的方式計算
"用總瓶數-不動的瓶子"

最後的顏色分類有可能是GBC GCB BGC BCG CGB CBG共六種組合

"""
