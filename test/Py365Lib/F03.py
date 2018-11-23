#!/usr/bin/env python3
from Py365Lib import *

path = "/home/user/bin/rmcr.pl"

# �f�B���N�g�����𓾂�B
print(FileSystem.getDirectoryName(path))
# �t�@�C�����𓾂�B
print(FileSystem.getFileName(path))
# �g���q�𓾂�B�i�擪�̓h�b�g�j
print(FileSystem.getExtension(path))

# ���݂̈ʒu�𓾂�B
print(FileSystem.getCurrentDirectory())
# �e�̃f�B���N�g���𓾂�B
print(FileSystem.getParentDirectory("/home/user/bin"))
# ���΃p�X�����΃p�X�ɂ𓾂�B
print(FileSystem.getAbsolutePath("../.."))

# �ꎞ�t�@�C�����𓾂�B
print(FileSystem.getTempFile())

