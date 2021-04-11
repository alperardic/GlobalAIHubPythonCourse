swaplist = ["a", "b", "c", "d", "e", "f", "g", "h"]
yarı = int(len(swaplist) / 2 )
tamamı = int(len(swaplist))

if len(swaplist) %2 == 0:
    swaplist[0:yarı], swaplist[yarı:tamamı] = swaplist[yarı:tamamı], swaplist[0:yarı]
    print("liste uzunluğu:", len(swaplist))
    print(swaplist)
else:
    swaplist[0:(yarı)], swaplist[(yarı+1):tamamı] = swaplist[(yarı+1):tamamı], swaplist[0:(yarı)]
    print("liste uzunluğu tek sayıdan oluştuğu için ortadaki değeri sabit tutarak yer değiştirme yapılmıştır.")
    print("liste uzunluğu:", len(swaplist))
    print(swaplist)
