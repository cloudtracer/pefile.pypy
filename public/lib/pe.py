#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys;
import encodings.utf_16_le;
import encodings.utf_7;
import base64;

import pefile;
import js;



import time
from collections import OrderedDict


bindata=js.eval('bblob');
#tttest=str(ttest);
binarydatastuff=base64.b64decode(str(bindata));
#pe=pefile.PE(data=b);
#print(pe.dump_info());
#import json;
pe2=pefile.PE(data=binarydatastuff)
#testi = pe2.dump_dict()
#print(testi)
print(pe2.dump_info())
#imphash = pe.get_imphash()
#print('Imphash: ' + imphash)
#print("PE PRINT:")
#dd = pe.DOS_HEADER.dump_dict()
#js.globals["pe"] = dd;
#print(pe.dump_info())
