#!/bin/bash
#  FileSystem テスト用ファイル作成
if [ $# -lt 1 ]
then
    echo ERROR: No Parameters.
    exit 9
fi

echo ~~~ Test No =  $1 ~~~

if [ ! -d ./test ]; then
    mkdir ./test
fi

case $1 in
1) # FileSystem.readAllText(path)
    echo Test test test10 > ./test/test1.txt
    echo oops! lol omg >> ./test/test1.txt
    ;;
2) # writeAllText(file, text, append=False)
    echo append=False
    cat ./test/test2.txt
    echo append=True
    cat ./test/test3.txt
    ;;
3) # readAllLines(file, method)
    echo Tokyo > ./test/test4.txt
    echo Yokohama >> ./test/test4.txt
    echo Kawasaki >> ./test/test4.txt
    echo Chiba >> ./test/test4.txt
    echo Saitama >> ./test/test4.txt
    ;;
4) # readBinary(file)
    echo '\t\b\r\n' > ./test/binary1.bin
    ;;
5) # writeBinary(file, data)
    od -x ./test/binary2.bin
    ;;
*)
    echo This test number is illegal.
    ;;
esac
