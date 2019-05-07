
import keyboard
import time


Shift = ["CTWTB-JTBW5-KFTTT-JTB33-JTBWB",
"5T5B3-CWJSK-KRTJT-TTJJT-9HW63",
"K3K33-3W9JT-6XJJT-TB3JB-HWZZF",
"WTC3B-Z5ZWC-HW6JT-JJJBJ-9FWXR",
"KBWJJ-WTXB9-C59J6-WFBTJ-TK6BJ",
"K3WJT-BFBRW-S5RTT-TBBB3-9XWZ5",
"5JKBJ-K9WHW-WBZTJ-T3TTB-TW9HR",
"W3C3B-5JRZC-WJH33-JBJJB-9S6CJ",
"CBWJ3-S5CJ3-WTTCF-WX333-9STBF",
"WJWJ3-FXC33-KT3CR-KR33J-J9B35",
"WTCJT-J653B-C3TKF-5X333-F6JRH",
"WJKBB-KXC3J-5BBCR-5X33J-XZ6RZ",
"KJKJT-WHBKX-HC9BT-TJBJ3-XJFSJ",
"CBKBJ-6ZJW6-HKH3T-B3T33-F5ZRS",
"CT5BB-XTW5X-9CSBT-3BTTJ-FT5X5",
"KTC3T-WTW5F-ZCHB3-BT3B3-XJ9WR",
"CBKBB-ZHJC6-SWHJT-JJ3BB-3CXHS",
"WBCJJ-33KWR-S5Z33-BJTTB-65WJJ",
"CTC3J-KR9H5-WTZ3T-TJ3TB-6SRRJ",
"KTK3J-FR3JS-ZX55B-B3BJ3-HSRB6",
"535BB-3R3BZ-HF5K3-JJB33-3BF3J",
"CTKJ3-9CBJS-9R5WT-JBJ3T-WKXKF",
"CBCJ3-W5TT9-S65K3-BJJ3B-XHWWC",
"CBKJ3-5FT39-ZRCCT-JTJB3-RFJ5B",
"5J5TT-RCJBS-ZXWCJ-TJ3BJ-TK3FB",
"CBCB3-SW36X-KJXW3-TTT3J-SFBSB",
"C3WBB-W3BRR-5J6WB-3JJJJ-35ZKZ",
"KTK3J-JWT6X-KB65T-3JJ3J-WHBRT",
"CJ5B3-6TTFF-5365T-TBJBB-SKTCB",
"CJ5T3-K5TF6-5TRC3-TBTJB-HZ5ZF",
"5B5TB-XFBX6-WBXWJ-JJ3TJ-9RXZW",
"W3CTJ-BFTFR-KJRK3-JJT3J-H6H36",
"53K3T-JZJX6-WBXKB-BBJJB-SJH3K",
"C35BJ-SRBF6-5TFKB-BBTJT-FSBZK",
"5BC33-CRJRF-WB6WB-3TTTB-655ZX",
"WJW3B-5HBR6-5BXCT-33TJ3-WXT53",
"CT5JB-FSTFX-5TF5T-3JJTT-6CF6T",
"535TJ-3JC6X-KJXCJ-BTBBT-K5WFR",
"CJKBJ-3XWTF-HCJ6K-JJB3T-SB35X",
"CJKBJ-3XWTF-HCJ6K-JJB3T-SB35X",
"CTWTB-RXKTR-SKJXW-3TBTJ-KXKKH",
"CTWTB-RXKTR-SKJXW-3TBTJ-KXKKH",
"KBWT3-WF5TR-SC3XW-T333B-TSCTS",
"W3C33-H653X-9CTR5-3TBJ3-HZ99S",
"53WT3-59KJX-95B65-3J333-S9JW9",
"CTKTJ-JSWJF-SCJXK-3TJJ3-RWTKX",
"5BW3B-F96CT-KXJFK-TB3B3-39BWZ",
"5JWTT-KHTSB-S5TXC-BB33J-HCJ6K",
"K353B-TWSBX-H5BR5-J3T33-6XTCK",
"WBK3T-BKW6T-TXTRK-JTTBT-C6BS5",
"5BWBT-RX5ZH-FJBJB-JBTJT-CRBWX",
"CJWJJ-HR5Z9-6JT3J-J3TBT-6TJ6K",
"WTCTJ-J9CS9-RJJ33-T3J3B-BT9XH",
"CBCJB-K9WHH-63JTJ-B3JJB-HT533",
"C35JB-R9WSH-XBBJT-JJ33B-F3WFB",
"K3WBT-Z95HZ-FTT3J-BTTJB-ZFX63",
"K3CB3-3JF99-RJ3JB-JJ3JJ-BT3RX",
"W3KJJ-KJXHZ-6JJBJ-3TT3T-33XBR",
"C3CTJ-XJ6HZ-FJTTJ-JBBBJ-3WTJZ",
"WTKJ3-9JXZ9-6TJJB-33T3J-FRJC6",
"KB5BJ-WCRZ9-6J33J-BBJ3T-XK96K",
"K3WTT-TKRH9-X3BJT-BJTBT-KXTSB",
"535JJ-XKRHS-XJ3TT-3JJT3-FTSR6",
"KBKJB-S5FSZ-FTTTT-TJJJB-XC95X",
"535T3-JR6ZH-6B3J3-3TJT3-T9JBK",
"WB5JJ-KX6HS-XBJBT-TBJJB-XW3S3",
"KJ53B-RRRSZ-F3TJJ-TJTT3-WBHT6",
"W353B-9FXZZ-RBJ3J-BT3B3-JK9KH",
"WTWJ3-TSXZS-FTJB3-3TTJJ-WBCT3",
"CJW3J-KHXZH-63TTJ-T3J33-R5HXK",
"CBWJ3-6HRZS-6TJJ3-3BJBT-WH3TZ",
"KT5T3-HS6HZ-FBJT3-3TJT3-ZC5KH",
"WBCJB-B3HHZ-RJJJJ-JJT3B-69XHK",
"W3CB3-RXRXB-TFBR5-BBT3T-F3KXS",
"K3CTT-SF6XT-B6JXK-TBJBT-9KZZJ",
"K35TJ-6399H-XTBBT-33TJB-ZZ3BX",
"W3KJB-H9CBW-XRBRW-JTBTJ-9JRXK",
"C35TB-WS6ST-TXBRK-TTTJT-JJH6H",
"53KBB-KXXRC-RZ66Z-WFJBB-WSRZ3",
"5B3BJ-XZWFW-T3KRZ-JBJTB-6WST9",
"ZFKJ3-TT3BB-JTBJT-T3JJT-JWX9H",
"CJKTT-FS5ZT-FXB6K-BBBBJ-93RCT",
"C3K3J-CH59J-XFT6K-T33J3-9WTJ9",
"CTKJJ-T3FS3-R63XW-3J3JT-JBJFH"]

Borderlands2 = ["CTWTB", "JTBW5", "KFTTT", "JTB33", "JTBWB",
"5T5B3", "CWJSK", "KRTJT", "TTJJT", "9HW63",
"K3K33", "3W9JT", "6XJJT", "TB3JB", "HWZZF",
"WTC3B", "Z5ZWC", "HW6JT", "JJJBJ", "9FWXR",
"KBWJJ", "WTXB9", "C59J6", "WFBTJ", "TK6BJ",
"K3WJT", "BFBRW", "S5RTT", "TBBB3", "9XWZ5",
"5JKBJ", "K9WHW", "WBZTJ", "T3TTB", "TW9HR",
"W3C3B", "5JRZC", "WJH33", "JBJJB", "9S6CJ",
"CBWJ3", "S5CJ3", "WTTCF", "WX333", "9STBF",
"WJWJ3", "FXC33", "KT3CR", "KR33J", "J9B35",
"WTCJT", "J653B", "C3TKF", "5X333", "F6JRH",
"WJKBB", "KXC3J", "5BBCR", "5X33J", "XZ6RZ",
"KJKJT", "WHBKX", "HC9BT", "TJBJ3", "XJFSJ",
"CBKBJ", "6ZJW6", "HKH3T", "B3T33", "F5ZRS",
"CT5BB", "XTW5X", "9CSBT", "3BTTJ", "FT5X5",
"KTC3T", "WTW5F", "ZCHB3", "BT3B3", "XJ9WR",
"CBKBB", "ZHJC6", "SWHJT", "JJ3BB", "3CXHS",
"WBCJJ", "33KWR", "S5Z33", "BJTTB", "65WJJ",
"CTC3J", "KR9H5", "WTZ3T", "TJ3TB", "6SRRJ",
"KTK3J", "FR3JS", "ZX55B", "B3BJ3", "HSRB6",
"535BB", "3R3BZ", "HF5K3", "JJB33", "3BF3J",
"CTKJ3", "9CBJS", "9R5WT", "JBJ3T", "WKXKF",
"CBCJ3", "W5TT9", "S65K3", "BJJ3B", "XHWWC",
"CBKJ3", "5FT39", "ZRCCT", "JTJB3", "RFJ5B",
"5J5TT", "RCJBS", "ZXWCJ", "TJ3BJ", "TK3FB",
"CBCB3", "SW36X", "KJXW3", "TTT3J", "SFBSB",
"C3WBB", "W3BRR", "5J6WB", "3JJJJ", "35ZKZ",
"KTK3J", "JWT6X", "KB65T", "3JJ3J", "WHBRT",
"CJ5B3", "6TTFF", "5365T", "TBJBB", "SKTCB",
"CJ5T3", "K5TF6", "5TRC3", "TBTJB", "HZ5ZF",
"5B5TB", "XFBX6", "WBXWJ", "JJ3TJ", "9RXZW",
"W3CTJ", "BFTFR", "KJRK3", "JJT3J", "H6H36",
"53K3T", "JZJX6", "WBXKB", "BBJJB", "SJH3K",
"C35BJ", "SRBF6", "5TFKB", "BBTJT", "FSBZK",
"5BC33", "CRJRF", "WB6WB", "3TTTB", "655ZX",
"WJW3B", "5HBR6", "5BXCT", "33TJ3", "WXT53",
"CT5JB", "FSTFX", "5TF5T", "3JJTT", "6CF6T",
"535TJ", "3JC6X", "KJXCJ", "BTBBT", "K5WFR",
"CJKBJ", "3XWTF", "HCJ6K", "JJB3T", "SB35X",
"CTWTB", "RXKTR", "SKJXW", "3TBTJ", "KXKKH",
"KBWT3", "WF5TR", "SC3XW", "T333B", "TSCTS",
"W3C33", "H653X", "9CTR5", "3TBJ3", "HZ99S",
"53WT3", "59KJX", "95B65", "3J333", "S9JW9",
"CTKTJ", "JSWJF", "SCJXK", "3TJJ3", "RWTKX",
"5BW3B", "F96CT", "KXJFK", "TB3B3", "39BWZ",
"5JWTT", "KHTSB", "S5TXC", "BB33J", "HCJ6K",
"K353B", "TWSBX", "H5BR5", "J3T33", "6XTCK",
"WBK3T", "BKW6T", "TXTRK", "JTTBT", "C6BS5",
"5BWBT", "RX5ZH", "FJBJB", "JBTJT", "CRBWX",
"CJWJJ", "HR5Z9", "6JT3J", "J3TBT", "6TJ6K",
"WTCTJ", "J9CS9", "RJJ33", "T3J3B", "BT9XH",
"CBCJB", "K9WHH", "63JTJ", "B3JJB", "HT533",
"C35JB", "R9WSH", "XBBJT", "JJ33B", "F3WFB",
"K3WBT", "Z95HZ", "FTT3J", "BTTJB", "ZFX63",
"K3CB3", "3JF99", "RJ3JB", "JJ3JJ", "BT3RX",
"W3KJJ", "KJXHZ", "6JJBJ", "3TT3T", "33XBR",
"C3CTJ", "XJ6HZ", "FJTTJ", "JBBBJ", "3WTJZ",
"WTKJ3", "9JXZ9", "6TJJB", "33T3J", "FRJC6",
"KB5BJ", "WCRZ9", "6J33J", "BBJ3T", "XK96K",
"K3WTT", "TKRH9", "X3BJT", "BJTBT", "KXTSB",
"535JJ", "XKRHS", "XJ3TT", "3JJT3", "FTSR6",
"KBKJB", "S5FSZ", "FTTTT", "TJJJB", "XC95X",
"535T3", "JR6ZH", "6B3J3", "3TJT3", "T9JBK",
"WB5JJ", "KX6HS", "XBJBT", "TBJJB", "XW3S3",
"KJ53B", "RRRSZ", "F3TJJ", "TJTT3", "WBHT6",
"W353B", "9FXZZ", "RBJ3J", "BT3B3", "JK9KH",
"WTWJ3", "TSXZS", "FTJB3", "3TTJJ", "WBCT3",
"CJW3J", "KHXZH", "63TTJ", "T3J33", "R5HXK",
"CBWJ3", "6HRZS", "6TJJ3", "3BJBT", "WH3TZ",
"KT5T3", "HS6HZ", "FBJT3", "3TJT3", "ZC5KH",
"WBCJB", "B3HHZ", "RJJJJ", "JJT3B", "69XHK",
"W3CB3", "RXRXB", "TFBR5", "BBT3T", "F3KXS",
"K3CTT", "SF6XT", "B6JXK", "TBJBT", "9KZZJ",
"K35TJ", "6399H", "XTBBT", "33TJB", "ZZ3BX",
"W3KJB", "H9CBW", "XRBRW", "JTBTJ", "9JRXK",
"C35TB", "WS6ST", "TXBRK", "TTTJT", "JJH6H",
"53KBB", "KXXRC", "RZ66Z", "WFJBB", "WSRZ3",
"5B3BJ", "XZWFW", "T3KRZ", "JBJTB", "6WST9",
"ZFKJ3", "TT3BB", "JTBJT", "T3JJT", "JWX9H",
"CJKTT", "FS5ZT", "FXB6K", "BBBBJ", "93RCT",
"C3K3J", "CH59J", "XFT6K", "T33J3", "9WTJ9",
"CTKJJ", "T3FS3", "R63XW", "3J3JT", "JBJFH"]

BorderlandsPre = ["KKWBB","5KS3T","TJBB3","B3JT3","BWBXB",
"C55BT","S95HK","HTT3J","B3J3J","5H5CR",
"5K53J","J9FJ3","BT3JB","3BTT3","9JF5J",
"WK533","CZ6JB","T3BB3","3TB33","W9XXR",
"55WT3","ZFKSW","BFK33","T3TJJ","63XB3",
"WCCJB","JZKSC","BRC33","JJJ3T","WWSW3",
"KKWBB","5SK9W","TRCB3","B3JT3","BWBR9",
"KCCJ3","XHCZ5","J6WBB","TB3J3","6C3WT",
"W5KBB","9S5ZC","J6CBT","J3BBJ","BF9FB",
"5CKBJ","BTFSC","TRCJB","3TBJB","X6J6Z",
"5C5JJ","WJRZ5","T6W33","TJJBT","JRJ9Z",
"WWWTB","F36H5","J6KJ3","3BJ3T","WW9RS",
"WC5JJ","HTXSC","TFWJJ","BJBJJ","HXWXB",
"KK5BT","TKXZ5","JFCJT","TBBJJ","69RCX",
"5CKTB","CCXZK","JXCJB","TJ3JT","H6KJX",
"CC53J","RKRZC","BR5T3","TJBBT","HBW9S",
"W5WJ3","Z5XH5","TFK3T","BTJJB","CRBHC",
"5W53J","TRR9K","JXWBJ","3JJJ3","SFWHK",
"KKWBJ","6B5FJ","3JJBT","JBBJB","WWH6X",
"555B3","ZHF9K","JXC33","JBJBT","BF6FS",
"KKC3T","B3ZSW","TRKJ3","3TB3T","XRBCB",
"CKKT3","K3SHK","3RK3B","3JB33","ZHRZJ",
"CKCJB","FB9ZK","TF5TJ","J333J","WRWS3",
"5K5BB","9JZSK","TRC3B","3JBTJ","JX556",
"KK5B3","35SHK","3F53B","JBTBT","RCR3C",
"5WCT3","55ZZ5","JRCJ3","T3JBT","BHHRJ",
"KW5TJ","X5SSW","B6CJ3","33TJB","RCRRX",
"K553B","ZW9ZC","J65TT","3TBJJ","9F66H",
"KCKJT","36SZW","JRCT3","J33TT","TFSBH",
"KKW3B","C6Z9K","BRKBB","BTJ3T","FKRJX",
"CWCBJ","X6Z9W","36CBT","TT3B3","3RRXZ",
"WW53B","HXSSK","36WTB","TJ3JT","WFBT6",
"WKCTT","J99HC","BXKTJ","JJTB3","JK39J",
"WCW3J","KSSZC","BR5JB","JJTTB","XF9FZ",
"WCKTB","6999K","J6C3T","TJT33","CZCK5",
"K5WTB","SS9ZK","BXKTT","BJ3JT","5BJCJ",
"C5CJ3","JT33X","3FKTB","TJJBT","JWFKX",
"5C5JJ","WBTT6","36KB3","JBB3J","T6CF3",
"W5KBJ","H9FX3","TBTJ3","T3J3T","RRCTS",
"KCCTJ","H5FST","BTBBT","3B33B","BTH5Z",
"5KWT3","J6FKF","JWTBT","BBJ3J","HZ5XW",
"WWCTB","5XRKF","BCJT3","TTJBT","6CK9W"]

Version = 1
#Set Version to 1 for borderlands 2
#Set Versioon to 2 for presequel
#Yes, Hindsight is 20/20, I should've done it differently because it's confusing but fuck it, it works
Automatic = 1
#Set Automatic to 1 if you want the program to just go
#Set it to 2 if you want to babysit it, Meaning it requires you to click a key for another code
#Use this if you know you've used a code in the past but don't know which
#Using Automatic = 1 could break if you have used a code before or if the code is no longer active


time.sleep(5)

if Automatic == 1:

    if Version == 2:
        for x in range(0, 410, 5):
    
            for y in range(5):
                print(Borderlands2[x])
                keyboard.write(Borderlands2[x])
                time.sleep(0.5)
                x+=1
            keyboard.press_and_release('enter')
            time.sleep(5)
            keyboard.press_and_release('enter')
            time.sleep(0.5)
            keyboard.press_and_release('tab')
            time.sleep(0.5)
            keyboard.press_and_release('tab')
            time.sleep(0.5)
            keyboard.press_and_release('enter')
            time.sleep(3)

    else:
        for x in range(0, 210, 5):
    
            for y in range(5):
                print(BorderlandsPre[x])
                keyboard.write(BorderlandsPre[x])
                time.sleep(0.5)
                x+=1
            keyboard.press_and_release('enter')
            time.sleep(5)
            keyboard.press_and_release('enter')
            time.sleep(0.5)
            keyboard.press_and_release('tab')
            time.sleep(0.5)
            keyboard.press_and_release('tab')
            time.sleep(0.5)
            keyboard.press_and_release('enter')
            time.sleep(3)

else:

    if Version == 2:

        for x in range(0, 410, 5):
            for y in range(5):
                print(Borderlands2[x])
                keyboard.write(Borderlands2[x])
                time.sleep(0.5)
                x+=1
            keyboard.press_and_release('enter')
            input('Press any Key to do the next code')

    else:

        for x in range(0, 210, 5):
            for y in range(5):
                print(BorderlandsPre[x])
                keyboard.write(BorderlandsPre[x])
                time.sleep(0.5)
                x+=1
            keyboard.press_and_release('enter')
            input('Press any Key to do the next code')

input('Press Enter to exit')