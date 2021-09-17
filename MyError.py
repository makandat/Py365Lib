# 固有の例外クラス
import traceback
import sys
import logging

class Error(Exception) :
  def __init__(self, message="", code=0, line=0) :
    super().__init__()
    self._message = message
    self._code = code
    self._line = line
    return
  
  @property
  def message(self) :
    return self._message

  @property
  def code(self) :
    return self._code

  @property
  def line(self) :
    return self._line

  # エラー情報を表示する。
  @staticmethod
  def print_traceback() :
    traceback.print_exc()
    (ty, v, tb) = sys.exc_info()
    print(ty)
    print(v)
    print(tb)
    return

  # エラーログを出力
  @staticmethod
  def log_traceback(logger:logging.Logger) :
    logger.error(traceback.format_exc())
    (ty, v, tb) = sys.exc_info()
    logger.error(ty)
    logger.error(v)
    logger.error(tb)
    return
