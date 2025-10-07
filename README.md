# python_debug_repl
When I use ai model in situation cannot use jupyter notebook, I write this script for me, because I don't want to copy paste everytime and reload model to continue debug need many time.

# Code
```py
import os, time

#######
The code you need to run first
#######

while 1:
    try:
        cd = input("\033[1;32m$cdebug" + time.strftime("%Y%m%d-%H%M%S", time.localtime()) + ": \033[00m" )
        if cd=="exit":
             break
        cd = cd.replace("\\br","\n")
        if cd and cd[0:1]=="!":
            os.system(cd[1:])
        else:
            exec(cd, globals())
    except Exception as e:
        print(e)
```

# Example
```py
import os, time

######################################################################################################################
print("import torch")
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"

import torch
from diffusers import AutoencoderKLCogVideoX, CogVideoXImageToVideoPipeline, CogVideoXTransformer3DModel
from diffusers.utils import export_to_video, load_image
from transformers import T5EncoderModel

"""#### Load models and create pipeline

Note: `bfloat16`, which is the recommended dtype for running "CogVideoX-5b-I2V" will cause OOM errors due to lack of efficient support on Turing GPUs.

Therefore, we must use `float16`, which might result in poorer generation quality. The recommended solution is to use Ampere or above GPUs, which also support efficient quantization kernels from [TorchAO](https://github.com/pytorch/ao) :(
"""

# model_id = "THUDM/CogVideoX-5b-I2V"

##!!!!!!!REMBER USE r""，NOT ""!!!!!!!!!!!!!!!
##WILL CAUSE BUG!!!!!!!!!!##########

path = r"D:\2\hub\models--THUDM--CogVideoX-5b-I2V\snapshots\a6f0f4858a8395e7429d82493864ce92bf73af11"

print("Load Model")

print("transformer")
transformer = CogVideoXTransformer3DModel.from_pretrained(path, subfolder="transformer", torch_dtype=torch.float16)
print("text_encoder")
text_encoder = T5EncoderModel.from_pretrained(path, subfolder="text_encoder", torch_dtype=torch.float16)
print("vae")
vae = AutoencoderKLCogVideoX.from_pretrained(path, subfolder="vae", torch_dtype=torch.float16)

print("START THE SHELL... Begin INTO DEBUG MODE....")
######################################################################################################################

while 1:
    try:
        cd = input("\033[1;32m$cdebug" + time.strftime("%Y%m%d-%H%M%S", time.localtime()) + ": \033[00m" )
        if cd=="exit":
             break
        cd = cd.replace("\\br","\n")
        if len(cd) and cd[0:1]=="!":
            os.system(cd[1:])
        else:
            exec(cd, globals())
    except Exception as e:
        print(e)
```

# Usage
## ```\br``` is break line
## ```!code``` will run code in terminal
## ```exit``` will exit
```ps
PS C:\Users\原神\Desktop> python cdebug.py
$cdebug20251007-080412: print(1)
1
$cdebug20251007-080419: !dir
 磁碟區 C 中的磁碟是 Windows
 磁碟區序號:  B8C5-1580

 C:\Users\原神\Desktop 的目錄

2025/10/07  上午 02:55    <DIR>          .
2025/10/06  上午 08:39    <DIR>          ..
2025/10/06  下午 10:35            11,407 b.jpg
2025/10/07  上午 07:51               370 cdebug.py
2025/10/07  上午 12:01             3,906 cogvideox_i2v_colab.py
2025/09/19  下午 05:27             2,261 Google Chrome.lnk
2025/09/07  下午 10:41             1,241 LINE.lnk
2025/09/22  上午 12:09               904 Lively Wallpaper.lnk
2025/05/22  下午 04:21             2,335 Microsoft Edge.lnk
2024/05/28  下午 06:57             1,077 OBS Studio (64bit).lnk
2025/05/22  下午 04:59             1,431 Roblox Player.lnk
2025/05/22  下午 04:56             1,259 Roblox Studio.lnk
2025/10/06  下午 10:34    <DIR>          神秘資料夾
2025/10/07  上午 12:23            13,833 系統管理員 命令提示字元 - conda  activate Daii - python  cdebug.py.txt
2025/10/07  上午 01:12            15,933 系統管理員 命令提示字元 - conda  activate Daii - python  cdebug.py1.txt
2025/10/07  上午 02:08            19,874 系統管理員 命令提示字元 - conda  activate Daii - python  cdebug.py111.txt
2025/10/07  上午 02:55            20,513 系統管理員 命令提示字元 - conda  activate Daii - python  cdebug.py3.txt
              14 個檔案          96,344 位元組
               3 個目錄  45,472,346,112 位元組可用
$cdebug20251007-080423: def a():\br  print(2,"\n",end="\n")
$cdebug20251007-080455: a()
2

$cdebug20251007-080500: exit
PS C:\Users\原神\Desktop>
```
