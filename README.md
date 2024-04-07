## v2.0 版本更新
游戏版本更新为可执行文件.exe，用户双击`PandaHeadBeatDown.exe`即可使用。使用方法不变。
#### 注意事项：需要将\image文件夹一同下载下来，和`PandaHeadBeatDown.exe`处于同一目录。同样可以调换\image文件夹里的照片内容（文件名不变），使得游戏中的图片发生变更。

============================================================================================================

### 【进阶内容】打包方法：使用pyinstaller工具包。
用管理员身份打开命令行窗口![image](https://github.com/xqmkkd/Game-Panda-Head-Beatdown/assets/143811250/845d9c6c-d7fc-474d-b099-46c4db497df7)
，运行`pip install pyinstaller`  
得到如下结果，我这边已经安装过了![image](https://github.com/xqmkkd/Game-Panda-Head-Beatdown/assets/143811250/d2707258-1bde-494d-a1eb-50073d43dcdd)  
然后可以输入`pip list`查询到![image](https://github.com/xqmkkd/Game-Panda-Head-Beatdown/assets/143811250/6cd72790-fcc2-4b33-b78a-090aea1d8516)的版本，说明安装完成。    
<br/><br/>
------------------------------------------------------
#### 添加环境变量 
想使用`pyinstaller`命令需要添加环境变量。在`高级系统设置`中![image](https://github.com/xqmkkd/Game-Panda-Head-Beatdown/assets/143811250/160c1cc8-cbf7-4000-bfaa-d42c005e22e8)点击`环境变量` $\Rightarrow$ `系统变量` $\Rightarrow$ `找到Path`![image](https://github.com/xqmkkd/Game-Panda-Head-Beatdown/assets/143811250/0bd9d6ad-0ac5-47df-a128-f5af87accb65)。点开Path编辑添加python的目录（装过python的应该已经添加过了）$\Rightarrow$ 添加`pyinstaller.exe`的目录。  
用`Everything`很快找到![image](https://github.com/xqmkkd/Game-Panda-Head-Beatdown/assets/143811250/793a3212-b694-4ea9-867e-29b950258985)，然后复制目录![image](https://github.com/xqmkkd/Game-Panda-Head-Beatdown/assets/143811250/94677c30-bf00-4f2c-86b6-63ec09bfd1ca)添加到`Path`里：![image](https://github.com/xqmkkd/Game-Panda-Head-Beatdown/assets/143811250/aa4f2aff-3935-4fc6-b402-9c35664862b7)。至此`pyinstaller`环境变量应该添加好了。  

<br/><br/>
---------------------------------------------
#### 打包项目  
然后进入项目文件的目录，输入打包命令`pyinstall -F 主项目文件.py 其他项目文件(允许多个).py`。  
比如我现在需要打包![image](https://github.com/xqmkkd/Game-Panda-Head-Beatdown/assets/143811250/6765294a-402e-415f-892b-3cb717f79c32) `alien.py`,`alien_invasion.py`,`bullet.py`,`button.py`,`game_functions.py`,`game_stats.py`,`scoreboard.py`,`settings.py`,`ship.py`这9个文件,其中`alien_invasion.py`是主文件。那么我就输入命令`pyinstaller -F alien_invasion.py alien.py bullet.py button.py game_functions.py game_stats.py scoreboard.py settings.py ship.py`![image](https://github.com/xqmkkd/Game-Panda-Head-Beatdown/assets/143811250/3fb85eb8-c341-4efb-8bcd-1f77740d79d6)`Successfully`就代表打包成功。  
回到文件夹发现多了一个`\dist`文件![image](https://github.com/xqmkkd/Game-Panda-Head-Beatdown/assets/143811250/5f050b13-6987-40d3-ac6e-44a9e2421788)里面就有我们需要的`.exe`,![image](https://github.com/xqmkkd/Game-Panda-Head-Beatdown/assets/143811250/8f9911ef-95ab-4bb3-8f08-f9d2357850a7)我这是打包了两次演示给你们看所以有两个。  
然后把`\image`文件夹复制进去即可使用了~（没有`\image`文件夹就会报错！）  
---------------------------------
#### v2.0版本的可执行文件的开发过程就介绍完毕了，小朋友们，你们学会了吗？

  











