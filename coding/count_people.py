#!/usr/bin/env python# -*- coding: utf-8 -*-# @Time    : 2018/8/3 下午11:46# @Author  : ziyi# @File    : create_news.py# @Software: PyCharmimport itchatimport timeimport datetime# if __name__ == '__main__':#     nowtime = datetime.datetime.now()#     itchat.auto_login(hotReload=True)  # 首次扫描登录后后续直接确认登录，无需再扫描#     print(nowtime)#     # if nowtime.hour >= 20:#     groups = itchat.get_chatrooms(update=True)#     friends = itchat.get_friends(update=True)#     print("群数量:", len(groups))#     for i in range(0, len(groups)):#         print(i+1, "--", groups[i]['NickName'], groups[i]['MemberCount'], "人")#         time.sleep(1)#         # send.write(contents)import itchat, timefrom itchat.content import TEXT#name = ' 'roomslist = []itchat.auto_login(hotReload=True)def getroom_message(n):    #获取群的username，对群成员进行分析需要用到    itchat.dump_login_status() # 显示所有的群聊信息，默认是返回保存到通讯录中的群聊    RoomList = itchat.search_chatrooms(name=n)    if RoomList is None:        print("%s group is not found!" % (name))    else:        return RoomList[0]['UserName']def getchatrooms():    #获取群聊列表    roomslist = itchat.get_chatrooms()    #print(roomslist)    return roomslistdef get_contents1(path):    # 取消替换空格    send_contents = None    try:        with open(path, encoding='utf16') as f:            contents = f.readlines()        send_contents = ''.join(content for content in contents)    except Exception as e:        pass    try:        with open(path, encoding='utf8') as f:            contents = f.readlines()        send_contents = ''.join(content for content in contents)    except Exception as e:        print('不是utf8的编码格式')    return send_contentsfor i in getchatrooms():    roomslist.append(i['NickName'])total = 0with open('../data/count/member_count_{}.txt'.format(datetime.datetime.now()), 'a', encoding='utf-8')as f:    for i, n in enumerate(roomslist):        ChatRoom = itchat.update_chatroom(getroom_message(n), detailedMember=True)        f.write('\n')        f.write("第 {} 个群聊名称为： {} ".format(i+1, n)+'\n')        f.write("用户总数为： {} ".format(len(ChatRoom['MemberList']))+'\n')        total = total + len(ChatRoom['MemberList'])        # f.write("累计用户数为： {} ".format(total)）        f.write("目前累计的用户数为： {} ".format(total)+'\n'+'\n')        for j, m in enumerate(ChatRoom['MemberList']):            #print (i['Province']+":",i['NickName'])            f.write("第 {} 个用户信息为： ".format(j+1)+m['Province']+":"+m['NickName']+'\n')            print('正在写入第 {} 个群           '.format(i+1)+m['Province']+":", m['NickName'])    f.close()code = input('输入编码格式：')