テストプログラム諸元

1 test_CursesApp1.py
  画面の列数と行数を表示する。
  列数については、カラーペア番号１８を使用する。
  カラーペア番号１８は setColor で再定義している。

  次のキーをコマンドとして使用する。
   'c'  画面クリア
   'h'  カーソルを表示しない
   'i'  カーソルを表示する
   'm'  カーソルを (x=4, y=10) へ移動する (座標を取得して表示も行う)
   'a'  属性をセットする
   'o'  属性を OFF する
   'n'  属性を ON する
   'q'  アプリ終了

  次のメソッドを使用している。
    setColor
    print
    clear
    putchar
    hideCursor
    showCursor
    setCursorPosition
    getCursorPosition
    setAttr
    setAttrOff
    setAttrOn


