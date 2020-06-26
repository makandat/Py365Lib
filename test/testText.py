#!/usr/bin/python3
#  Text クラスのテスト
import sys
from Py365Lib import Text as txt, Common

# コマンド引数取得
if Common.count_args() == 0  :
    Common.stop(9, "テスト番号を指定してください。")
else :
    testNo = int(sys.argv[1])
    Common.esc_print(Common.ESC_FG_GREEN, testNo)

# テスト開始
if testNo == 1 :
    # length(s), concat(s1, s2), 
    s = "012３４"
    assert txt.length(s) == 5, "testNo=1 subNo=1"
    s = txt.concat(s, "89")
    assert s == "012３４89", "testNo=1 subNo=2"
    print("Test #1 OK")
elif testNo == 2 :
    # substring(text, start, length), substr(text, start, end)
    tx = "012３４５6789ABCDEF"
    # substring
    print(txt.substring(tx, 2, 4))
    assert txt.substring(tx, 2, 4) == "2３４５", "testNo=2 subNo=1"
    # substr
    print(txt.substr(tx, 2, 4))
    assert txt.substr(tx, 2, 4) == "2３４", "testNo=2 subNo=2"
    print("Test #2 OK")
elif testNo == 3 :
    #  left(text, length), right(text, length), times(c, n)
    tx = "012３４５6789ABCDEF"
    # left
    print(txt.left(tx, 4))
    assert txt.left(tx, 4) == "012３", "testNo=3 subNo=1"
    # right
    print(txt.right(tx, 4))
    assert txt.right(tx, 4) == "CDEF", "testNo=3 subNo=2"
    # times
    assert txt.times('*', 5) == "*****", "testNo=3 subNo=3"
    print("Test #3 OK")
elif testNo == 4 :
    # isdigit(a), isalpha(a), isdelim(a), isprint(a)
    assert txt.isdigit('0'), "testNo=4, subNo=1"
    assert not txt.isdigit('x'), "testNo=4, subNo=2"
    assert txt.isalpha('a'), "testNo=4, subNo=3"
    assert not txt.isalpha('1'), "testNo=4, subNo=4"
    assert txt.isdelim('/'), "testNo=4, subNo=5"
    assert not txt.isdelim('A'), "testNo=4, subNo=6"
    assert not txt.isprint('\b'), "testNo=4, suNo=7"
    assert txt.isprint('*'), "testNo=4, suNo=8"
    print("Test #4 OK.")
elif testNo == 5 :
    # tolower(s), toupper(s), trim(s), chomp(s)
    assert txt.tolower("aB&C") == "ab&c", "testNo=5, subNo=1"
    assert txt.toupper("aB&c") == "AB&C", "testNo=5, subNo=2"
    assert txt.trim("\tabc\n") == "abc",  "testNo=5, subNo=3"
    assert txt.chomp(" abc ") == " abc ",   "testNo=5, subNo=4"
    assert txt.chomp(" abc\n") == " abc",   "testNo=5, subNo=5"
    assert txt.chomp(" abc\r\n") == " abc",   "testNo=5, subNo=6"
    print("Test #5 OK.")
elif testNo == 6 :
    # split(c, s), join(c, array), contain(p, s), indexOf(p, s)
    csv = txt.split(",", "1,-5,75,USD")
    assert csv[0] == "1", "testNo=6, subNo=1"
    assert csv[1] == "-5", "testNo=6, subNo=2"
    assert csv[2] == "75", "testNo=6, subNo=3"
    assert csv[3] == "USD", "testNo=6, subNo=4"
    assert txt.join(",", ["A", "U", "D"]) == "A,U,D", "testNo=6, subNo=5"
    assert txt.contain("!", "Hi!") == True, "testNo=6, subNo=6"
    assert txt.contain("!", "Hello") == False, "testNo=6, subNo=7"
    assert txt.indexOf("!", "Hi!") == 2, "testNo=6, subNo=8"
    assert txt.indexOf("!", "Hello") < 0, "testNo=6, subNo=9"
    print("Test #6 OK.")
elif testNo == 7 :
    # replace(old, new, s), format(f, t), parseInt(s), parseDouble(s), chr(a), asc(a)
    assert txt.replace("/", "-", "2000/12/31") == "2000-12-31", "testNo=7, subNo=1"
    print(txt.format("{0:d} {1:10.4f} {2}", 1000, 4.5e-1, "abc"))
    assert txt.format("{0:d} {1:10.4f} {2}", 1000, 4.5e-1, "abc") == "1000     0.4500 abc", "testNo=7, subNo=2"
    assert txt.parseInt("1024") == 1024, "testNo=7, subNo=3"
    assert txt.parseDouble("-1e1") == -10, "testNo=7, subNo=4"
    assert txt.char(0x41) == "A", "testNo=7, subNo=5"
    assert txt.asc("A") == 0x41, "testNo=7, subNo=6"
    print("Test #7 OK.")
elif testNo == 8 : # re_contain, re_search, re_split, re_replace
    assert txt.re_contain(r'.+[0-9][0-9]', 'map10') == True, "testNo=8, subNo=1"
    assert txt.re_contain(r'.+[0-9][0-9]', 'mapten') == False, "testNo=8, subNo=2"
    m = txt.re_search(r'(\d+)\.(\d+)', "10987.4")
    print(m.groups())
    assert m.groups()[0] =='10987', "testNo=8, subNo=3"
    assert m.groups()[1] =='4', "testNo=8, subNo=4"
    a = txt.re_split(r'\W+', 'Words, words, words.')
    assert a[0] == 'Words', "testNo=8, subNo=5"
    assert a[1] == 'words', "testNo=8, subNo=6"
    assert a[2] == 'words', "testNo=8, subNo=7"
    assert a[3] == '', "testNo=8, subNo=8"
    s = txt.re_replace(r'\w+', '*', 'words, words.')
    print(s)
    assert s == '*, *.', "testNo=8, subNo=9"
    print("Test #8 OK.")
elif testNo == 9 : # s2b(s), b2s(b)
    s = "1234１２"
    b = txt.s2b(s)
    print(type(b))
    print(b)
    s2 = txt.b2s(b)
    print(type(s2))
    print(s2)
elif testNo == 10 : # insert
   s = "0123456789"
   ins = "ABC"
   s2 = txt.insert(s, ins, 2)
   print(s2)
else :
    print("不正な番号です。")
