	# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob

cl = LINETCR.LINE()
cl.login(token="Em4wvUJLMh8mIystZC22.Skq32mqBkuNH3J/isSmUaG.vz4rZ4SMEvXQLafRX9EH4Ht0plYi0xKVDWXqo6friro=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="Em6XefnBOaSE26NAYLOb.ya8IY4yHWbqSBrTHXQ6FoW.6AWtTI2eq2erUO7kE0MjWzUDkgnvL2FyvfGPAiPOBrg=")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="EmlnDJGe8vnu4IaLA1c7.Gn374age48GYK55/lWPKHW.uKoIeA5ecb8tnD5/26eFSJHG9Mgl/s156tFXNoMFAnM=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="EmpiLy2O4vYjZ9v6mDLe./uIiT2swmu5lgZo5ZTlmBG.+DpOq8RKfCHos7lXScpbniKKWb5rugA5OTA5cZWnzvQ=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="EmIl0eQ9W8OgxEEAUzg9.gDuKLVz5mEIlJHcwLw8n/q.P4xAxwE8vwHR7BaJKeRfSegl/e6/NLNdXQJJqinU+cU=")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="Emwy64SSYOfJ9f6JRdm4.gverIQ60Hdx+5CvqmcCv5a.eHd6dRUhtjwCX2MF9PX+1PleNNJz8HR+hh/cXcYfr10=")
ki5.loginResult()

#ki6 = LINETCR.LINE
#ki6.login(qr=True)
#ki6.loginResult()

#ki7 = LINETC.LINE
#ki7.login(qr=True)
#ki7.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" =====[You Know Me La]=====

[C̶̲̅ᴏ̶̲̅ᴍ̶̲̅ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅ᴅ̶̲̅]

❂͜͡☆➣ Me 「Send Your Contact」
❂͜͡☆➣ Mid 「Send Your Mid」
❂͜͡☆➣ Bots mid 「Bots Send Bots Mid」
❂͜͡☆➣ TL: 「Put Your timeline status」
❂͜͡☆➣ MyName: 「Change Your Name」
❂͜͡☆➣ Name 1-5: 「Change Your Bots Name 1 by 1」
❂͜͡☆➣ All: 「Change Bots Name」
❂͜͡☆➣ Bots1-5 Groups 「Show Your Bots Groups」
❂͜͡☆➣ Bots1-5 Gid 「Show Your Bots GID」
❂͜͡☆➣ Bots1-5 Invite:「Put GID Bots Invite You to Groups」
❂͜͡☆➣ Copy1-5「Bots Clone Contact Targets」
❂͜͡☆➣ All Nenen @ 「All of Your Bots Mimic User」
❂͜͡☆➣ Follow1-3: 「Your Bots Mimic User」
❂͜͡☆➣ Tagall 「Mention All Members in Groups」
❂͜͡☆➣ Mybots 「Show Your Bots Contact」
❂͜͡☆➣ Message Confirmation 「Check Your additional Message」
❂͜͡☆➣ Mybio: 「Uodate Your Status」
❂͜͡☆➣ Allbio: 「Update oYur Bots Status」 
  
[C̶̲̅ᴏ̶̲̅ᴍ̶̲̅ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅ᴅ̶̲̅ ̶̲̅ɪ̶̲̅ɴ̶̲̅ ̶̲̅G̶̲̅ʀ̶̲̅ᴏ̶̲̅ᴜ̶̲̅ᴘ̶̲̅]

❂͜͡☆➣ Invite:on:「Put Mid Contact Bots Invite member」
❂͜͡☆➣ Kick:「Put Mid Contact」
❂͜͡☆➣ Ginfo 「Show The Groups Information」
❂͜͡☆➣ Gid 「Show The Groups Id」
❂͜͡☆➣ Cancel 「Change Bots Name」
❂͜͡☆➣ Gn 「Change Group Name」
❂͜͡☆➣ Url 「Qr/Url Join Code」
❂͜͡☆➣ Ourl 「Open Groups QR Code」
❂͜͡☆➣ Curl 「Close Groups QR Code」
==========[MueheheBots✓]==========
"""

setGroup ="""	===[Muehehe ]===

❂͜͡☆➣ Protect on/off
❂͜͡☆➣ Qr on/off
❂͜͡☆➣ Invite on/off
❂͜͡☆➣ Cancel on/off
❂͜͡☆➣ Add on/off
❂͜͡☆➣ Share on/off
❂͜͡☆➣ Contact on/off
❂͜͡☆➣ Group cancel:on/off
❂͜͡☆➣ Leave on/off
❂͜͡☆➣ Unban:on
❂͜͡☆➣ Banlist
❂͜͡☆➣ Mcheck
=====[MueheheBots✓]=====
"""
helo=""

KAC=[cl,ki,ki2,ki3]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
#ki6mid = ki6.getProfile().mid
#ki7mid = ki7.getProfile().mid
Bots=[mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid] #jika mau menambahkan bot jgn lupa taroh disini cth. ki5mid didalem [] jangan lupa tanda koma
admsa = "ub0a437d8c41b2949e1de3f884ac32e02"
wait = {
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"""тнαикѕ fσя α∂∂ιиg мє αѕ α fяιєи∂
≫ ɪғ ɪ ɴᴏᴛ ᴀɴsᴡᴇʀ ᴊᴜsᴛ sᴘᴀᴍ ≪
≫ sʟᴏᴡ ʀᴇsᴘᴏɴ ᴀᴛ 7ᴀᴍ ᴛɪʟʟ 6ᴘᴍ ≪""",
    "lang":"JP",
    "comment":"Thanks For Add Me",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"",
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":True,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }


setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mimic = {
    "status":False,
    "target":{}
    }

Follow = {
    "status":False,
    "target":{}
    }

ikut = {
    "status":False,
    "target":{}
    }

goo = {
    "status":False,
    "target":{}
    }

#---------------------------------------------------------------------------------------------------------------------------------------
def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error
#---------------------------------------------------------------------------------------------------------------------------------------
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    
        #------Open QR Kick start------#
        if op.type == 10:
           if wait["linkprotect"] == True:
               if op.param2 not in Bots:
                   G = cl.getGroup(op.param1)
                   G = ki.getGroup(op.param1)
                   G = ki2.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   ki.kickoutFromGroup(op.param1,[op.param2])
                   cl.updateGroup(G)
        #------Open QR Kick finish-----#
   
        #------Invite User Kick start------#
        if op.type == 13:
           if wait["inviteprotect"] == True:
               if op.param2 not in Bots:
                  random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Invite User Kick Finish------#  
        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
#---------------------------------------------------------------------------------------------------------------------------------------
        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("Dont play Bots !! \n["+op.param1+"]\nの\n["+op.param2+"]\n(*´･ω･*)。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if kimid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("Dont play Bots !!、\n["+op.param1+"]\nの\n["+op.param2+"]\n(*´･ω･*)。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    G = ki2.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    Ticket = ki2.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("Dont play Bots !!、\n["+op.param1+"]\nの\n["+op.param2+"]\n(*´･ω･*)。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

#--------------------------------------------------------------------------------------------
        #if op.type == 15:
            #random.choice(KAC).sendText(op.param1, "Good Bye :)")
            #print op.param3 + "has left the group"

        #if op.type == 17:
            #group = cl.getGroup(op.param1)
            #cb = Message()
            #cb.to = op.param1
            #cb.text = cl.getContact(op.param2).displayName + " Selamat Datang di " + group.name
            #cl.sendMessage(cb)
#--------------------------------------------------------------------------------------------------------------
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
#----------------------------------------------------------------------------------------------------------------
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            ki.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = ki.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            ki.updateGroup(X)
                        except:
                            ki.sendText(msg.to,"error")
#-------------------------------------------------------------------------------------------------------------------
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
#-----------------------------------------------------------------------------------------------------
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)	
                ki.like(url[25:58], url[66:], likeType=1001)
                ki2.like(url[25:58], url[66:], likeType=1001)
                ki3.like(url[25:58], url[66:], likeType=1001)
                ki4.like(url[25:58], url[66:], likeType=1001)
                ki5.like(url[25:58], url[66:], likeType=1001)
                #ki6.like(url[25:58], url[66:], likeType=1001)
                #ki7.like(url[25:58], url[66:], likeType=1001)
        if op.type == 32:
            if wait["protect"] == True:
               if op.param2 not in Bots:

                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Invite User Kick Finish------#
#-----------------------------------------------------------------------------------------------------
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"Already in My Blacklist")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Decided Not to Comment!")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Removed User in My Blacklist , Done..")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"User Not in Blacklist")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"User In My Blacklist Now!")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"User Already In My Blacklist")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done")
#------------------------------------------------------------------------------------------------------------------------------
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
#------------------------------------------------------------------------------------------------------------------------------------------
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "User Post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "User Posting URL\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
#----------------------------------------------------------------------------------------------------------------
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    ki.updateGroup(group)
                else:
                    cl.sendText(msg.to,"This Command only work in Groups")
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn ","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"This Command only work in Groups")
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
#------------------------------------------------------------------------------------------------------
            elif "Invite:on:" in msg.text:
                midd = msg.text.replace("Invite:on:","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
                ki2.findAndAddContactsByMid(midd)
                ki2.inviteIntoGroup(msg.to,[midd])
                ki3.findAndAddContactsByMid(midd)
                ki3.inviteIntoGroup(msg.to,[midd])
                ki4.findAndAddContactsByMid(midd)
                ki4.inviteIntoGroup(msg.to,[midd])
                ki5.findAndAddContactsByMid(midd)
                ki5.inviteIntoGroup(msg.to,[midd])
#---------------------------------------------------------------------------------------------------------
            elif "My Bots" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg)
                #msg.contentType = 13
                #msg.contentMetadata = {'mid': ki6mid}
                #cl.sendMessage(msg)
                #msg.contentType = 13
                #msg.contentMetadata = {'mid': ki7mid}
                #cl.sendMessage(msg)
#----------------------------------------------------------------------------------
            elif "Bots1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif "Bots2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
            elif "Bots3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
            elif "Bots3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
            elif "Bots4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
            elif "Bots5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg)
            #elif "Bots6" == msg.text:
                #msg.contentType = 13
                #msg.contentMetadata = {'mid': ki6mid}
                #ki6.sendMessage(msg)
            #elif "Bots7" == msg.text:
                #msg.contentType = 13
                #msg.contentMetadata = {'mid': ki7mid}
                #ki7.sendMessage(msg)
#---------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["All gift","Gift all"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                #ki6.sendMessage(msg)
                #ki7.sendMessage(msg)
#-----------------------------------------------------------------------------------------------------------------
            elif msg.text.lower() == 'hore':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846756",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                
            elif msg.text.lower() == 'ok':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846755",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
             
            elif msg.text.lower() == 'siap bos':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846757",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                
            elif msg.text.lower() == 'thanks':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846759",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                
            elif msg.text.lower() == 'lol':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846776",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                
            elif msg.text.lower() == 'sue':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846777",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                
            elif msg.text.lower() == 'no':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846777",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                
            elif msg.text.lower() == 'suntuk':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875040",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
                
            elif msg.text.lower() == 'apa?':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875046",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
                
            elif msg.text.lower() == '?':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875046",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
            
            elif msg.text.lower() == 'pose dulu':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875030",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
               
            elif msg.text.lower() == '250c':
                msg.contentType = 9
                msg.contentMetadata={'PRDTYPE': 'STICKER',
                                    'STKVER': '1',
                                    'MSGTPL': '5',
                                    'STKPKGID': '1380280'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == '200c':
                msg.contentType = 9
                msg.contentMetadata={'PRDTYPE': 'STICKER',
                                    'STKVER': '1',
                                    'MSGTPL': '5',
                                    'STKPKGID': '1319678'}
            elif msg.text in ["kam","Welkam","Kam"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                #ki6.sendMessage(msg)
                #ki7.sendMessage(msg)
#---------------------------------------------------------------------------------------------------------------------------
            elif msg.text.lower() in ["hm","Hm","Tags","tags"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                    mention(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention(msg.to, nm5)
                if jml > 500:
                    cl.sendText(msg.to,'Member melebihi batas.')
                cnt = Message()
                cnt.text = "Done : " + str(jml) +  " Members"
                cnt.to = msg.to
                cl.sendMessage(cnt)
#------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in["Tagall"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, jml = [], [], [], len(nama)
                if jml <= 100:
                   mention(msg.to, nama)
                if jml > 100 and jml < 200:
                   for i in range(0, 99):
                       nm1 += [nama[i]]
                   mention(msg.to, nm1)
                   for j in range(100, len(nama)-1):
                       nm2 += [nama[j]]
                   mention(msg.to, nm2)
                if jml > 200  and jml < 300:
                   for i in range(0, 99):
                       nm1 += [nama[i]]
                   mention(msg.to, nm1)
                   for j in range(100, 199):
                       nm2 += [nama[j]]
                   mention(msg.to, nm2)
                   for k in range(200, len(nama)-1):
                       nm3 += [nama[k]]
                   mention(msg.to, nm3)
                if jml > 300:
                    print "Terlalu Banyak Men 300+"
                cnt = Message()
                cnt.text = "Done:"+str(jml)
                cont.to = msg.to
                ki.sendMessage(cnt)
#--------------------------------------------------------------------------------------------------------------
            elif msg.text in ["B Cancel","Cancel say","B cancel"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Ga ada pendingan BosQ ")
                        else:
                            ki.sendText(msg.to,"Invite people inside not")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Ga ada pendingan BosQ")
                    else:
                        ki.sendText(msg.to,"Ga ada pendingan BosQ")

            elif msg.text in ["Cancel","cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"")
                        else:
                            cl.sendText(msg.to,"")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                    else:
                        cl.sendText(msg.to,"")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Ourl"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Url Open")
                    else:
                        cl.sendText(msg.to,"Url Open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done Boss ✓")
                    else:
                        cl.sendText(msg.to,"Done Boss ✓")
#--------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Curl"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Url Close")
                    else:
                        cl.sendText(msg.to,"Url Close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done boss ✓")
                    else:
                        cl.sendText(msg.to,"Done Boss ✓")
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
            elif "Ginfo" == msg.text:
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[Nama]\n" + str(ginfo.name) + "\n\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nAnggota:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                cl.sendMessage(msg)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Kirim Kontak Siapa aja , work diPM .. kalo digroup ntah kontak siapa keluar gajelas ..
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
#-------------------------------------------------------------------------------------------------
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "1 mid" == msg.text:
                ki.sendText(msg.to,kimid)
            elif "2 mid" == msg.text:
                ki2.sendText(msg.to,ki2mid)
            elif "3 mid" == msg.text:
                ki3.sendText(msg.to,ki3mid)
            elif "4 mid" == msg.text:
                ki4.sendText(msg.to,ki4mid)
            elif "5 mid" == msg.text:
                ki5.sendText(msg.to,ki5mid)
            #elif "6 mid" == msg.text:
                #ki6.sendText(msg.to,ki6mid)
            #elif "7 mid" == msg.text:
                #ki7.sendText(msg.to,ki7mid)
            elif "Bots mid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
                #ki6.sendText(msg.to,ki6mid)
                #ki7.sendText(msg.to,ki7mid)
#-------------------------------------------------------------------------------------------------------------------------
            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
#-----------------------------------------------------------------------------------------------------------------------
            elif "All:" in msg.text:
                string = msg.text.replace("All:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                #if len(string.decode('utf-8')) <= 20:
                    #profile = ki6.getProfile()
                    #profile.displayName = string
                    #ki6.updateProfile(profile)
                #if len(string.decode('utf-8')) <= 20:
                    #profile = ki7.getProfile()
                    #profile.displayName = string
                    #ki7.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿All Name of MyBots Was Updated " + string + " ✓" )
#--------------------------------------------------------------------------------------------------------------
            elif "Mybio:" in msg.text:
                string = msg.text.replace("Mybio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Bio✓ :" + string + " done BossQ")
            elif "Allbio:" in msg.text:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                    ki.sendText(msg.to,"􀜁􀇔􏿿All Bio of Bots Was Updated " + string + " ✓" )
            elif "Myname:" in msg.text:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names " + string + " ✓")
#-----------------------------------------------------------
            elif "Copy @" in msg.text:
             if msg.from_ in admsa:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               cl.CloneContactProfile(target)
                               cl.sendText(msg.to, "Succes Copy profile~")
                            except Exception as e:
                                print e
	
            elif msg.text in ["Backup"]:
               if msg.from_ in admsa:
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    cl.sendText(msg.to, "Profile back..")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
#------------------------------------------------------------------------------------------------------------
            elif "Copy1 @" in msg.text:
             if msg.from_ in admsa:
                   print "[COPY] Oya"
                   _name = msg.text.replace("Copy1 @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ki.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki.CloneContactProfile(target)
                               ki.sendText(msg.to, "Succes Copy profile~")
                            except Exception as e:
                                print e
	
            elif msg.text in ["Bots1 Backup"]:
               if msg.from_ in admsa:
                try:
                    ki.updateDisplayPicture(backup.pictureStatus)
                    ki.updateProfile(backup)
                    ki.sendText(msg.to, "Profile back..")
                except Exception as e:
                    ki.sendText(msg.to, str (e))
#-------------+-+---------------&&&&----------_----_--------------------
            elif "Copy2 @" in msg.text:
             if msg.from_ in admsa:
                   print "[COPY] ya"
                   _name = msg.text.replace("Copy2 @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ki2.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki2.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki2.CloneContactProfile(target)
                               ki2.sendText(msg.to, "Succes Copy profile~")
                            except Exception as e:
                                print e
	
            elif msg.text in ["Bots2 Backup"]:
               if msg.from_ in admsa:
                try:
                    ki2.updateDisplayPicture(backup.pictureStatus)
                    ki2.updateProfile(backup)
                    ki2.sendText(msg.to, "Profile back..")
                except Exception as e:
                    ki2.sendText(msg.to, str (e))
#------------------------------------------------------------------------------
            elif "Copy3 @" in msg.text:
             if msg.from_ in admsa:
                   print "[COPY] y"
                   _name = msg.text.replace("Copy3 @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ki3.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki3.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki3.CloneContactProfile(target)
                               ki3.sendText(msg.to, "Succes Copy profile~")
                            except Exception as e:
                                print e
	
            elif msg.text in ["Bots3 Backup"]:
               if msg.from_ in admsa:
                try:
                    ki3.updateDisplayPicture(backup.pictureStatus)
                    ki3.updateProfile(backup)
                    ki3.sendText(msg.to, "Profile back..")
                except Exception as e:
                    ki3.sendText(msg.to, str (e))
#------------------------------------------------------------------------------
            elif "Copy4 @" in msg.text:
             if msg.from_ in admsa:
                   print "[COPY] ay"
                   _name = msg.text.replace("Copy4 @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ki4.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki4.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki4.CloneContactProfile(target)
                               ki4.sendText(msg.to, "Succes Copy profile~")
                            except Exception as e:
                                print e
	
            elif msg.text in ["Bots4 Backup"]:
               if msg.from_ in admsa:
                try:
                    ki4.updateDisplayPicture(backup.pictureStatus)
                    ki4.updateProfile(backup)
                    ki4.sendText(msg.to, "Profile back..")
                except Exception as e:
                    ki4.sendText(msg.to, str (e))
#------------------------------------------------------------------------------------------------------------------------
            elif "Copy5 @" in msg.text:
             if msg.from_ in admsa:
                   print "[COPY] aay"
                   _name = msg.text.replace("Copy5 @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ki5.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki5.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki5.CloneContactProfile(target)
                               ki5.sendText(msg.to, "Succes Copy profile~")
                            except Exception as e:
                                print e
	
            elif msg.text in ["Bots5 Backup"]:
               if msg.from_ in admsa:
                try:
                    ki5.updateDisplayPicture(backup.pictureStatus)
                    ki5.updateProfile(backup)
                    ki5.sendText(msg.to, "Profile back..")
                except Exception as e:
                    ki5.sendText(msg.to, str (e))
#----------------------------------------------------------------------------------------------------
            
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
            elif "Name 1:" in msg.text:
                string = msg.text.replace("Name 1:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"􀜁􀇔􏿿Update Names" + string + " ✓")
#--------------------------------------------------------
            elif "Name 2:" in msg.text:
                string = msg.text.replace("Name 2:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"􀜁􀇔􏿿Update Names" + string + " ✓")
#--------------------------------------------------------
            elif "Name 3:" in msg.text:
                string = msg.text.replace("Name 3:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"􀜁􀇔􏿿Update Names " + string + " ✓")
#--------------------------------------------------------
            elif "Name 4:" in msg.text:
                string = msg.text.replace("Name 4:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"􀜁􀇔􏿿Update Names " + string + " ✓")
#--------_-------------------------------------+-------
            elif "Name 5:" in msg.text:
                string = msg.text.replace("Name 5:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"􀜁􀇔􏿿Update Names " + string + " ✓")
#---------------------------------------------------------------------
            #elif "Name 6:" in msg.text:
                #string = msg.text.replace("Name 6:","")
                #if len(string.decode('utf-8')) <= 20:
                    #profile = ki6.getProfile()
                    #profile.displayName = string
                    #ki6.updateProfile(profile)
                    #ki6.sendText(msg.to,"􀜁􀇔􏿿Update Names " + string + " ✓")
#---------------------------------------------------------------------
            #elif "Name 7:" in msg.text:
                #string = msg.text.replace("Name 7:","")
                #if len(string.decode('utf-8')) <= 20:
                    #profile = ki7.getProfile()
                    #profile.displayName = string
                    #ki7.updateProfile(profile)
                    #ki7.sendText(msg.to,"􀜁􀇔􏿿Update Names " + string + " ✓")
#---------------------------------------------------------------------
#--------------------------------------------------------
            elif "Mid:" in msg.text:
                mmid = msg.text.replace("Mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
#----------------------------------------------------------------------------------------------
            elif msg.text in ["Contact on","contact on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact on 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Contact on 􀜁􀇔􏿿")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact Already on 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Contact Already on 􀜁􀇔􏿿")
            elif msg.text in ["Contact off","contact off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact Already 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Contact Already 􀜁􀇔􏿿")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact Already off 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Contact Already off 􀜁􀇔􏿿")
#-------------------------------------------------------------------------------------------------------
            elif msg.text in ["Protect on","protect on"]:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection on 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Protection on 􀜁􀇔􏿿")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection on 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Protection on 􀜁􀇔􏿿")
            elif msg.text in ["Protect off","protect off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection off 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Protection off 􀜁􀇔􏿿")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection off 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Protection off 􀜁􀇔􏿿")
#----------------------------------------------------------------------------------------------------------
            elif msg.text in ["Qr on","qr on"]:
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Protect on 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Link Protect on 􀜁􀇔􏿿")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Protect on 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Link Protect on 􀜁􀇔􏿿")
            elif msg.text in ["Qr off","qr off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Protect off 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Link Protect off 􀜁􀇔􏿿")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Protect Already off 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Link Protect Already off 􀜁􀇔􏿿")
#-----------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Invite on","invite on"]:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite Protection on 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Invite Protection on 􀜁􀇔􏿿")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite Protection on 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Invite Protection on 􀜁􀇔􏿿")
            elif msg.text in ["Invite off","invite off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite Protection off 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Invite Protection off 􀜁􀇔􏿿")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite Protection off 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Invite Protection off 􀜁􀇔􏿿")
#---------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Cancel on","cancel on"]:
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Members Invitation on 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Cancel Members Invitation on 􀜁􀇔􏿿")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Members Invitation Already on 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Cancel Members Invitation Already on 􀜁􀇔􏿿")
            elif msg.text in ["Cancel off","cancel off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Members Invitation off 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Cancel Members Invitation off 􀜁􀇔􏿿")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Members Invitation off 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Cancel Members Invitation off 􀜁􀇔􏿿")
#------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Autojoin on","autojoin on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join Groups on 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Auto join Groups on 􀜁􀇔􏿿")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join Groups Already on 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Auto join Groups Already on 􀜁􀇔􏿿")
            elif msg.text in ["Autojoin off","autojoin off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join Groups off 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Auto join Groups off 􀜁􀇔􏿿")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join Groups Already off 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Auto join Groups Already off 􀜁􀇔􏿿")
#-------------------------------------------------------------------------------------------------------------------------------
            elif "Group cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Groups Invite Members Will Canceled Auto 􀜁􀇔􏿿")
                        else:
                            cl.sendText(msg.to,"Groups Invite Members Will Canceled Auto 􀜁􀇔􏿿")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Groups Invite Members Will Canceled Auto 􀜁􀇔􏿿")
                        else:
                            cl.sendText(msg.to,strnum + "Groups Invite Members Will Canceled Auto 􀜁􀇔􏿿")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Weird value 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Weird value 􀜁􀇔􏿿")
#-----------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Auto leave on","Leave on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on✓􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah terbuka 􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done✓􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Is already open✓􀜁􀇔􏿿")
            elif msg.text in ["Auto leave off","Leave off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on✓􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah off✓􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done✓􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Is already close✓􀜁􀇔􏿿")
            elif msg.text in ["Share on","K on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka✓")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on✓")
                    else:
                        cl.sendText(msg.to,"on✓")
            elif msg.text in ["Share off","K off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done✓􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already turned off 􀜁􀇔􏿿✓")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off✓")
                    else:
                        cl.sendText(msg.to,"Off✓")
            elif msg.text in ["Blacklist","blacklist"]:
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="This user was kick me before..\nCheck\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
#----------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Help","help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
#----------------------------------------------------------------------------------------------------------------
            elif msg.text.lower() == 'set':
                md = ""
                if wait["contact"] == True: md+="􀠁􀆩􏿿 ✈Contact:on 􀜁􀄯􏿿\n"
                else: md+="􀠁􀆩􏿿 ✈Contact:off􀜁􀄰􏿿\n"
                if wait["autoJoin"] == True: md+="􀠁􀆩􏿿 ✈Auto Join:on 􀜁􀄯􏿿\n"
                else: md +="􀠁􀆩􏿿 ✈Auto Join:off􀜁􀄰􏿿\n"
                if wait["autoCancel"]["on"] == True:md+="􀠁􀆩􏿿 ✈Auto cancel:" + str(wait["autoCancel"]["members"]) + "􀜁􀄯􏿿\n"
                else: md+= "􀠁􀆩􏿿 ✈Group cancel:off 􀜁􀄰􏿿\n"
                if wait["leaveRoom"] == True: md+="􀠁􀆩􏿿 ✈Auto leave:on 􀜁􀄯􏿿\n"
                else: md+="􀠁􀆩􏿿 ✈Auto leave:off 􀜁􀄰􏿿\n"
                if wait["timeline"] == True: md+="􀠁􀆩􏿿 ✈Share:on 􀜁􀄯􏿿\n"
                else:md+="􀠁􀆩􏿿 ✈Share:off 􀜁􀄰􏿿\n"
                if wait["autoAdd"] == True: md+="􀠁􀆩􏿿 ✈Auto add:on 􀜁􀄯􏿿\n"
                else:md+="􀠁􀆩􏿿 ✈Auto add:off 􀜁􀄰􏿿\n"
                if wait["protect"] == True: md+="􀠁􀆩􏿿 ✈Protect:on 􀜁􀄯􏿿\n"
                else:md+="􀠁􀆩􏿿 ✈Protect:off 􀜁􀄰􏿿\n"
                if wait["linkprotect"] == True: md+=" ✈􀠁􀆩􏿿Link Protect:on 􀜁􀄯􏿿\n"
                else:md+="􀠁􀆩􏿿 ✈Link Protect:off 􀜁􀄰􏿿\n"
                if wait["inviteprotect"] == True: md+=" 􀠁􀆩􏿿✈Invitation Protect:on 􀜁􀄯􏿿\n"
                else:md+="􀠁􀆩􏿿 ✈Invitation Protect:off 􀜁􀄰􏿿\n"
                if wait["cancelprotect"] == True: md+="􀠁􀆩􏿿 ✈Cancel Protect:on 􀜁􀄯􏿿\n"
                else:md+="􀠁􀆩􏿿 ✈Cancel Protect:off 􀜁􀄰􏿿\n"
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendMessage(msg)
#----------------------------------------------------------------------------------------------------------------
            elif cms(msg.text,["me","Me"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
#----------------------------------------------------------------------------------------------------------------
            elif cms(msg.text,["Creator","creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendText(msg.to,"􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿")
                cl.sendMessage(msg)
                cl.sendText(msg.to,"􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿")
#----------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Bots out","bots out"]:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki3.leaveGroup(i)
                    ki4.leaveGroup(i)
                    ki5.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Bot Sudah Keluar Di semua grup")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
#----------------------------------------------------------------------------------------------------------
            elif msg.text in ["Bots1 out","bots1 out"]:
                gid = ki.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,"Bot Sudah Keluar Di semua grup")
                else:
                    ki.sendText(msg.to,"He declined all invitations")
#--------------------------------------------------------------------------------------------------------
            elif msg.text in ["Bots2 out","bots2 out"]:
                gid = ki2.getGroupIdsJoined()
                for i in gid:
                    ki2.leaveGroup(i)
                if wait["lang"] == "JP":
                    ki2.sendText(msg.to,"Bot Sudah Keluar Di semua grup")
                else:
                    ki2.sendText(msg.to,"He declined all invitations")
#------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Bots3 out","bots3 out"]:
                gid = ki3.getGroupIdsJoined()
                for i in gid:
                    ki3.leaveGroup(i)
                if wait["lang"] == "JP":
                    ki3.sendText(msg.to,"Bot Sudah Keluar Di semua grup")
                else:
                    ki3.sendText(msg.to,"He declined all invitations")
#------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Bots4 out","bots4 out"]:
                gid = ki4.getGroupIdsJoined()
                for i in gid:
                    ki4.leaveGroup(i)
                if wait["lang"] == "JP":
                    ki4.sendText(msg.to,"Bot Sudah Keluar Di semua grup")
                else:
                    ki4.sendText(msg.to,"He declined all invitations")
#------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Bots5 out","bots5 out"]:
                gid = ki5.getGroupIdsJoined()
                for i in gid:
                    ki5.leaveGroup(i)
                if wait["lang"] == "JP":
                    ki5.sendText(msg.to,"Bot Sudah Keluar Di semua grup")
                else:
                    ki5.sendText(msg.to,"He declined all invitations")
#----------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Group cancelall","Rejectall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                    ki.rejectGroupInvitation(i)
                    ki2.rejectGroupInvitation(i)
                    ki3.rejectGroupInvitation(i)
                    ki4.rejectGroupInvitation(i)
                    ki5.rejectGroupInvitation(i)
                    #ki6.rejectGroupInvitation(i)
                    #ki7.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"I Reject all Groups Invitation")
                else:
                    cl.sendText(msg.to,"I declined all invitations")
#----------------------------------------------------------------------------------------------------------------
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                cl.sendText(msg.to,"We Changed the Message Confirmation")
            elif "Pesan add:" in msg.text:
                wait["message"] = msg.text.replace("Pesan add:","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"We Changed the Message Confirmation")
                else:
                    cl.sendText(msg.to,"Change information")
            elif msg.text in ["Message check","Message Confirmation"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Additional information is automatically set to the following \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan Auto add Telah Ditetapkan sbg Berikut \n\n" + wait["message"])
#----------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"I changed the language to english✓")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"I changed the language to indonesia✓")
            elif "Message set" in msg.text:
                c = msg.text.replace("Message set","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Is a string that can not be changed✓")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"This has been changed✓\n\n" + c)
#---------------------Sc invite owner ke group------------------------------------------------------------
            elif "Bots1 invite:" in msg.text:
              if msg.from_ in admsa:
                gid = msg.text.replace("Bots1 invite:","")
                if gid == "":
                  ki.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    ki.findAndAddContactsByMid(msg.from_)
                    ki.inviteIntoGroup(gid,[msg.from_])
                  except:
                    ki.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
            elif "Bots2 invite:" in msg.text:
              if msg.from_ in admsa:
                gid = msg.text.replace("Bots2 invite:","")
                if gid == "":
                  ki2.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    ki2.findAndAddContactsByMid(msg.from_)
                    ki2.inviteIntoGroup(gid,[msg.from_])
                  except:
                    ki2.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
            elif "Bots3 invite:" in msg.text:
              if msg.from_ in admsa:
                gid = msg.text.replace("Bots3 invite:","")
                if gid == "":
                  ki3.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    ki3.findAndAddContactsByMid(msg.from_)
                    ki3.inviteIntoGroup(gid,[msg.from_])
                  except:
                    ki3.sendText(msg.to,"Saya ga didalem bos")
            elif "Bots4 invite:" in msg.text:
              if msg.from_ in admsa:
                gid = msg.text.replace("Bots4 invite:","")
                if gid == "":
                  ki4.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    ki4.findAndAddContactsByMid(msg.from_)
                    ki4.inviteIntoGroup(gid,[msg.from_])
                  except:
                    ki4.sendText(msg.to,"Saya ga didalem bos")
            elif "Bots5 invite:" in msg.text:
              if msg.from_ in admsa:
                gid = msg.text.replace("Bots5 invite:","")
                if gid == "":
                  ki5.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    ki5.findAndAddContactsByMid(msg.from_)
                    ki5.inviteIntoGroup(gid,[msg.from_])
                  except:
                    ki5.sendText(msg.to,"Saya ga didalem bos")
#---------------------Sc invite owner ke group------------------------------------------------------------
            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
#----------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Ban"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklist👈")
            elif msg.text in ["Bandel"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklist👈")
            elif msg.text in ["Becek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklist")
                else:
                    cl.sendText(msg.to,"The following is a blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
#----------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Clock on","clock on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Clock on ✓")
            elif msg.text in ["Clock off","clock off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Already off")
            elif "Clock say:" in msg.text:
                n = msg.text.replace("Clock say:","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Your Clock name Has Changed " + n)
#-----------------------------------------------
            elif msg.text == "Sider":
                    cl.sendText(msg.to, "Check sider")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "Read":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")
#--------------------------------------------------------------------------------------------------------------
            elif "Nk " in msg.text:                
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                             if target not in Bots:
                                try:
                                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                except:
                                    cl.sendText(msg.to,"Good Bye")
#-----------------------------------------------------------
            elif "Cleanse" in msg.text:
                if msg.toType == 2:
                    print "hm"
                    _name = msg.text.replace("Cleanse","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    ki.sendText(msg.to,"Good Bye (*´･ω･*)")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"What you mean?")
                    else:
                        for target in targets:
                          if target not in Bots:
                             try:
                                 klist=[ki,ki2,ki3,ki4,ki5]
                                 kicker=random.choice(klist)
                                 kicker.kickoutFromGroup(msg.to,[target])
                                 print (msg.to,[g.mid])
                             except:
                                 ki.sendText(msg.to,"Group cleanse (*´･ω･*)")
#========================================
#--------------------------------------------------------------------------------------------------------------
            elif ("Kamu " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
#--------------------------------------------------------------------------------------------------------------
            elif ("Cek " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)
#--------------------------------------------------------------------------------------------------------------
	    elif "Ban @" in msg.text:
                if msg.toType == 2:
                    print "[Ban]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Target Locked")
                            except:
                                cl.sendText(msg.to,"Error")
#--------------------------------------------------------------------------------------------------------------
	    elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Target Unlocked")
                            except:
                                cl.sendText(msg.to,"Error")
#--------------------------------------------------------------------------------------------------------------
            elif "Ban:" in msg.text:                  
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Locked")
                                except:
                                    cl.sendText(msg.to,"Ok BosQ")
#--------------------------------------------------------------------------------------------------------------
            elif "Unban:" in msg.text:                  
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    cl.sendText(msg.to,"Done BosQ")
#--------------------------------------------------------------------------------------------------------------
            elif "Mban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		cl.sendText(msg.to,"Target Lock")
#-----------------------------------------------------------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------
            elif msg.text in ["Responsename","responsename"]:
                profile = ki.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                ki.sendText(msg.to, text)
                profile = ki2.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                ki2.sendText(msg.to, text)
                profile = ki3.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                ki3.sendText(msg.to, text)
                profile = ki4.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                ki4.sendText(msg.to, text)
                profile = ki5.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                ki5.sendText(msg.to, text)
#--------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Ban:on"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unban:on"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["mcheck","Mcheck"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 Nothing in the blacklist")
                else:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 following is a blacklist")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "Nakal 􀜁􀅔􏿿" +cl.getContact(mi_d).displayName + "\n􀜁􀅔􏿿 "
                    cl.sendText(msg.to,mc)
#--------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Banlist","banlist"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "Nakal\n 􀜁􀅔􏿿" +cl.getContact(mm).displayName + "\n􀜁􀅔􏿿 "
                    cl.sendText(msg.to,cocoa + "Daftar Hitam 􀜁􀅔􏿿 ")
#--------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Kill","kill"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Banlist user Nothing")
                        return
                    for jj in matched_list:
                        try:
                            ki.kickoutFromGroup(msg.to,[jj])
                            ki2.kickoutFromGroup(msg.to,[jj])
                            ki3.kickoutFromGroup(msg.to,[jj])
                            ki4.kickoutFromGroup(msg.to,[jj])
                            ki5.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
#--------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Come","Come to papa","Coming"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki.sendText(msg.to,"􀜁􀇔􏿿​ Hello "  +  str(ginfo.name)  + "")
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki2.sendText(msg.to,"􀜁􀇔􏿿​ Hello "  +  str(ginfo.name)  + "")
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki3.sendText(msg.to,"􀜁􀇔􏿿​ Hello "  +  str(ginfo.name)  + "")
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki4.sendText(msg.to,"􀜁􀇔􏿿​ Hello "  +  str(ginfo.name)  + "")
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki5.sendText(msg.to,"􀜁􀇔􏿿​ Hello "  +  str(ginfo.name)  + "")
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
                       
 #-----------------------------------------------
            elif msg.text in ["Dudul come","dudul come"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
#-----------------------------------------------
            elif "Sf1 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "Sf2 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "Sf3 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)
#--------------------------------------------------------------------------------------------------------------
            elif "Sf4 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki4.updateGroup(G)
#--------------------------------------------------------------------------------------------------------------
            elif "Sf5 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki5.updateGroup(G)
#--------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Hush","hush","Pulang","pulang"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.sendText(msg.to,"􀜁􀇔􏿿Bye Bye "  +  str(ginfo.name)  +"")
                        ki.leaveGroup(msg.to)
                        ki2.sendText(msg.to,"􀜁􀇔􏿿Bye Bye "  +  str(ginfo.name)  +"")
                        ki2.leaveGroup(msg.to)
                        ki3.sendText(msg.to,"􀜁􀇔􏿿Bye Bye "  +  str(ginfo.name)  +"")
                        ki3.leaveGroup(msg.to)
                        ki4.sendText(msg.to,"􀜁􀇔􏿿Bye Bye "  +  str(ginfo.name)  +"")
                        ki4.leaveGroup(msg.to)
                        ki5.sendText(msg.to,"􀜁􀇔􏿿Bye Bye "  +  str(ginfo.name)  +"")
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Sf1 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.sendText(msg.to,"􀜁􀇔􏿿Bye Bye "  +  str(ginfo.name)  +"")
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Sf2 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki2.sendText(msg.to,"􀜁􀇔􏿿Bye Bye "  +  str(ginfo.name)  +"")
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Sf3 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.sendText(msg.to,"􀜁􀇔􏿿Bye Bye "  +  str(ginfo.name)  +"")
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Sf4 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki4.sendText(msg.to,"􀜁􀇔􏿿Bye Bye "  +  str(ginfo.name)  +"")
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Sf5 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki5.sendText(msg.to,"􀜁􀇔􏿿Bye Bye "  +  str(ginfo.name)  +"")
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Reinvite" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,"Bye Bye " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                        cl.sendText(msg.to,"􀜁􀇔􏿿Bye Bye "  +  str(ginfo.name)  +"")
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["Welcome","welcome"]:
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[Groups Name]\n" + str(ginfo.name) )
                cl.sendText(msg.to,"Welcome to 👥" + str(ginfo.name) + " 👥 Groups")
                cl.sendText(msg.to,"Group Creator " + str(ginfo.name) + " :\n👤 " + ginfo.creator.displayName )
                cl.sendMessage(msg)
#------------------------------------------------------------------------------------------------------------------------
            elif "Say " in msg.text:
				bctxt = msg.text.replace("Say ","")
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
            elif msg.text in ["Ping","ping"]:
                ki.sendText(msg.to,"Ping 􀜁􀇔􏿿 Bales PM boss Gue oi ! ")
                ki2.sendText(msg.to,"Ping 􀜁􀇔􏿿 Bales PM boss Gue oi ! ")
                ki3.sendText(msg.to,"Ping 􀜁􀇔􏿿 Bales PM boss Gue oi ! ")
                ki4.sendText(msg.to,"Ping 􀜁􀇔􏿿 Bales PM boss Gue oi ! ")
                ki5.sendText(msg.to,"Ping 􀜁􀇔􏿿 Bales PM boss Gue oi ! ")
            elif msg.text in ["Sp","Speed","sp"]:
                start = time.time()
                cl.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s second" % (elapsed_time))
            elif msg.text in ["Botspeed","Botsp","Bspeed"]:
                start = time.time()
                ki.sendText(msg.to, "Wait Boss..")
                elapsed_time = time.time() - start
                ki.sendText(msg.to, "%s second" % (elapsed_time))
#-----------------------------------------------
            #elif msg.text in ["Botspeed","Botsp","Bspeed"]:
                #start = time.time()
                #cl.sendText(msg.to, "Bot show your speed...")
                #elapsed_time = time.time() - start 
         
#----------------------------------------------- 
            elif "Beb " in msg.text:                  
                       nk0 = msg.text.replace("Beb ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                             if not target in Bots:
                                try:
                                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    cl.sendText(msg.to,"")
#-----------------------------------------------------------
            elif msg.text in ["Mprutss","Crotss","Unchh"]:
                  group = ki.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      ki.sendMessage(msg)
                  except Exception as error:
                      print error

    #-------------Fungsi Tag All Finish---------------#                          
            elif "Bc:grup " in msg.text:
                 bctxt = msg.text.replace("Bc:grup ", "")
                 n = cl.getGroupIdsJoined()
                 for manusia in n:
                      cl.sendText(manusia, (bctxt))
#-----------------------------------------------
            elif "Bc:1 " in msg.text:
                 bctxt = msg.text.replace("Bc:1 ", "")
                 n = ki.getGroupIdsJoined()
                 for manusia in n:
                      ki.sendText(manusia, (bctxt))
            elif "Bc:2 " in msg.text:
                 bctxt = msg.text.replace("Bc:2 ", "")
                 n = ki2.getGroupIdsJoined()
                 for manusia in n:
                      ki2.sendText(manusia, (bctxt))
            elif "Bc:3 " in msg.text:
                 bctxt = msg.text.replace("Bc:3 ", "")
                 n = ki3.getGroupIdsJoined()
                 for manusia in n:
                      ki3.sendText(manuisa, (bctxt))
            elif "Bc:4 " in msg.text:
                 bctxt = msg.text.replace("Bc:4 ", "")
                 n = ki4.getGroupIdsJoined()
                 for manusia in n:
                      ki4.sendText(manusia, (bctxt))
            elif "Bc:5 " in msg.text:
                 bctxt = msg.text.replace("Bc:5 ", "")
                 n = ki5.getGroupIdsJoined()
                 for manusia in n:
                      ki5.sendText(manusia, (bctxt))
            elif "Bc:ct " in msg.text:
                 bctxt = msg.text.replace("Bc:ct ", "")
                 t = cl.getAllContactIds()
                 for manusia in t:
                      cl.sendText(manusia, (bctxt))
            elif "Bc:c1 " in msg.text:
                 bctxt = msg.text.replace("Bc:c1 ", "")
                 t = ki.getAllContactIds()
                 for manusia in t:
                      ki.sendText(manusia, (bctxt))
            elif "Bc:c2 " in msg.text:
                 bctxt = msg.text.replace("Bc:c2 ", "")
                 t = ki2.getAllContactIds()
                 for manusia in t:
                      ki2.sendText(manusia, (bctxt))
            elif "Bc:c3 " in msg.text:
                 bctxt = msg.text.replace("Bc:c3 ", "")
                 t = ki3.getAllContactIds()
                 for manusia in t:
                      ki3.sendText(manusia, (bctxt))
            elif "Bc:c4 " in msg.text:
                 bctxt = msg.text.replace("Bc:c4 ", "")
                 t = ki4.getAllContactIds()
                 for manusia in t:
                      ki4.sendText(manusia, (bctxt))
            elif "Bc:c5 " in msg.text:
                 bctxt = msg.text.replace("Bc:c5 ", "")
                 t = ki5.getAllContactIds()
                 for manusia in t:
                      ki5.sendText(manusia, (bctxt))
#-----------------------------------------------
            elif msg.text in ["Group id","ç¾¤çµ„å…¨id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Invite:gcreator"]:
              if msg.toType == 2:
                ginfo = cl.getGroup(msg.to)
                gCreator = ginfo.creator.mid
                try:
                    cl.findAndAddContactsByMid(gCreator)
                    cl.inviteIntoGroup(msg.to,[gCreator])
                    print "SUKSES INVITE GCREATOR"
                except:
                    pass
#-----------------------------------------------
            elif msg.text in ["My Groups"]: #Melihat List Group
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[•]%s Member\n" % (cl.getGroup(i).name   +"👥 "+str(len(cl.getGroup(i).members)))
                cl.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gid)))
            elif msg.text in ["Bots1 Groups"]:
                gid = ki.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[•]%s Member\n" % (ki.getGroup(i).name   +"👥 "+str(len(ki.getGroup(i).members)))
                ki.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gid)))
                
            elif msg.text in ["Bots2 Groups"]:
                gid = ki2.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[•]%s Member\n" % (ki2.getGroup(i).name   +"👥 "+str(len(ki2.getGroup(i).members)))
                ki2.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gid)))

            elif msg.text in ["Bots3 Groups"]:
                gid = ki3.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[•]%s Member\n" % (ki3.getGroup(i).name   +"👥 "+str(len(ki3.getGroup(i).members)))
                ki3.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gid)))
								
            elif msg.text in ["Bots4 Groups"]:
                gid = ki4.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[•]%s Member\n" % (ki4.getGroup(i).name   +"👥 "+str(len(ki4.getGroup(i).members)))
                ki4.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gid)))
								
            elif msg.text in ["Bots5 Groups"]:
                gid = ki5.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[•]%s Member\n" % (ki5.getGroup(i).name   +"👥 "+str(len(ki5.getGroup(i).members)))
                ki5.sendText(msg.to,"=======[List Group]======\n\n"+ h +"\nTotal Group :"+str(len(gid)))
	#-----------------------------------------------
            elif msg.text in ["Bots5 Gid"]:
                gid = ki5.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (ki5.getGroup(i).name,i)
                ki5.sendText(msg.to,"=======[List Group]======\n\n"+ h +"\nTotal Group :"+str(len(gid)))
            elif msg.text in ["Bots4 Gid"]:
                gid = ki4.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (ki4.getGroup(i).name,i)
                ki4.sendText(msg.to,"=======[List Group]======\n\n"+ h +"\nTotal Group :"+str(len(gid)))
            elif msg.text in ["Bots3 Gid"]:
                gid = ki3.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (ki3.getGroup(i).name,i)
                ki3.sendText(msg.to,"=======[List Group]======\n\n"+ h +"\nTotal Group :"+str(len(gid)))
            elif msg.text in ["Bots2 Gid"]:
                gid = ki2.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (ki2.getGroup(i).name,i)
                ki2.sendText(msg.to,"=======[List Group]======\n\n"+ h +"\nTotal Group :"+str(len(gid)))
            elif msg.text in ["Bots5 Gid"]:
                gid = ki.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (ki.getGroup(i).name,i)
                ki.sendText(msg.to,"=======[List Group]======\n\n"+ h +"\nTotal Group :"+str(len(gid)))

#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                            
                        
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                       
                        
                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)

                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki2mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki4mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki6mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        wait["blacklist"][op.param2] = True
            except:
                pass
	#-------------------------------------------------
	elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
             text = msg.text
             if text is not None:
              ki.sendText(msg.to,text)
              ki2.sendText(msg.to,text)
              ki3.sendText(msg.to,text)
              ki4.sendText(msg.to,text)
              ki5.sendText(msg.to,text)
             else:
              if msg.contentType == 7:
               msg.contentType = 7
               msg.text = None
               msg.contentMetadata = {
                      "STKID": "110",
                      "STKPKGID": "1",
                      "STKVER": "100" }
               ki.sendMessage(msg)
               ki2.sendMessage(msg)
               ki3.sendMessage(msg)
               ki4.sendMessage(msg)
               ki5.sendMessage(msg)
              elif msg.contentType == 13:
               msg.contentType = 13
               msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
               cl.sendMessage(msg)
               
	elif "Bots " in msg.text:
             if msg.from_ in admsa:
              cmd = msg.text.replace("Bots ","")
              if cmd == "tt mau?":
               if mimic["status"] == False:
                mimic["status"] = True
                ki.sendText(msg.to,"Mauuuuuuu bosss")
               else:
                ki.sendText(msg.to,"ini lagi nenen boss")
              elif cmd == "udah":
               if mimic["status"] == True:
                mimic["status"] = False
                ki.sendText(msg.to,"Belum puass bossss")
               else:
                ki.sendText(msg.to,"pengen nenen lagi 😚😚")
              elif "nenen" in cmd:
               target0 = msg.text.replace("Bots nenen","")
               target1 = target0.lstrip()
               target2 = target1.replace("@","")
               target3 = target2.rstrip()
               _name = target3
               gInfo = ki.getGroup(msg.to)
               targets = []
               for a in gInfo.members:
                if _name == a.displayName:
                 targets.append(a.mid)
               if targets == []:
                ki.sendText(msg.to,"No targets")
               else:
                for target in targets:
                 try:
                  mimic["target"][target] = True
                  ki.sendText(msg.to,"Nenen 😋😋")
                  ki.sendMessageWithMention(msg.to,target)
                  break
                 except:
                  break
              elif "del" in cmd:
               target0 = msg.text.replace("Bots del","")
               target1 = target0.lstrip()
               target2 = target1.replace("@","")
               target3 = target2.rstrip()
               _name = target3
               gInfo = ki.getGroup(msg.to)
               targets = []
               for a in gInfo.members:
                if _name == a.displayName:
                 targets.append(a.mid)
               if targets == []:
                ki.sendText(msg.to,"No targets")
               else:
                for target in targets:
                 try:
                  del mimic["target"][target]
                  ki.sendText(msg.to,"Udah kurus dia boss, ga ada nenen lagi 😂😂")
                  ki.sendMessageWithMention(msg.to,target)
                  break
                 except:
                  print error


	elif msg.from_ in Follow["target"] and Follow["status"] == True and Follow["target"][msg.from_] == True:
             text = msg.text
             if text is not None:
              ki.sendText(msg.to,text)
             else:
              if msg.contentType == 7:
               msg.contentType = 7
               msg.text = None
               msg.contentMetadata = {
                      "STKID": "4",
                      "STKPKGID": "1",
                      "STKVER": "100" }
               ki.sendMessage(msg)
              elif msg.contentType == 13:
               msg.contentType = 13
               msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
               cl.sendMessage(msg)
	elif "Follow1:" in msg.text:
             if msg.from_ in admsa:
              cmd = msg.text.replace("Follow1:","")
              if cmd == "on":
               if Follow["status"] == False:
                Follow["status"] = True
                ki.sendText(msg.to,"We will Follow The Targets Boss ✓")
               else:
                ki.sendText(msg.to,"Followed already boss")
              elif cmd == "off":
               if Follow["status"] == True:
                Follow["status"] = False
                ki.sendText(msg.to,"We Stopped Following the targets Boss ✓")
               else:
                ki.sendText(msg.to,"We already Stopped Following the targets Boss")
              elif "add" in cmd:
               target0 = msg.text.replace("Follow1:add","")
               target1 = target0.lstrip()
               target2 = target1.replace("@","")
               target3 = target2.rstrip()
               _name = target3
               gInfo = ki.getGroup(msg.to)
               targets = []
               for a in gInfo.members:
                if _name == a.displayName:
                 targets.append(a.mid)
               if targets == []:
                ki.sendText(msg.to,"No targets")
               else:
                for target in targets:
                 try:
                  Follow["target"][target] = True
                  ki.sendText(msg.to,"Succes BosQ ✓")
                  ki.sendMessageWithMention(msg.to,target)
                  break
                 except:
                  break
              elif "del" in cmd:
               target0 = msg.text.replace("Follow1:del","")
               target1 = target0.lstrip()
               target2 = target1.replace("@","")
               target3 = target2.rstrip()
               _name = target3
               gInfo = ki.getGroup(msg.to)
               targets = []
               for a in gInfo.members:
                if _name == a.displayName:
                 targets.append(a.mid)
               if targets == []:
                ki.sendText(msg.to,"No targets")
               else:
                for target in targets:
                 try:
                  del Follow["target"][target]
                  ki.sendText(msg.to,"Targets Has Deleted Boss ✓")
                  ki.sendMessageWithMention(msg.to,target)
                  break
                 except:
                  print succes

	elif msg.from_ in ikut["target"] and ikut["status"] == True and ikut["target"][msg.from_] == True:
             text = msg.text
             if text is not None:
              ki2.sendText(msg.to,text)
             else:
              if msg.contentType == 7:
               msg.contentType = 7
               msg.text = None
               msg.contentMetadata = {
                      "STKID": "6",
                      "STKPKGID": "1",
                      "STKVER": "100" }
               ki2.sendMessage(msg)
              elif msg.contentType == 13:
               msg.contentType = 13
               msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
               cl.sendMessage(msg)
	elif "Follow2:" in msg.text:
             if msg.from_ in admsa:
              cmd = msg.text.replace("Follow2:","")
              if cmd == "on":
               if ikut["status"] == False:
                ikut["status"] = True
                ki2.sendText(msg.to,"We will Follow The Targets Boss ✓")
               else:
                ki2.sendText(msg.to,"Followed already boss")
              elif cmd == "off":
               if ikut["status"] == True:
                ikut["status"] = False
                ki2.sendText(msg.to,"We Stopped Following the targets Boss ✓")
               else:
                ki2.sendText(msg.to,"We already Stopped Following the targets Boss")
              elif "add" in cmd:
               target0 = msg.text.replace("Follow2:add","")
               target1 = target0.lstrip()
               target2 = target1.replace("@","")
               target3 = target2.rstrip()
               _name = target3
               gInfo = ki2.getGroup(msg.to)
               targets = []
               for a in gInfo.members:
                if _name == a.displayName:
                 targets.append(a.mid)
               if targets == []:
                ki2.sendText(msg.to,"No targets")
               else:
                for target in targets:
                 try:
                  ikut["target"][target] = True
                  ki2.sendText(msg.to,"Succes BosQ ✓")
                  ki2.sendMessageWithMention(msg.to,target)
                  break
                 except:
                  break
              elif "del" in cmd:
               target0 = msg.text.replace("Follow2:del","")
               target1 = target0.lstrip()
               target2 = target1.replace("@","")
               target3 = target2.rstrip()
               _name = target3
               gInfo = ki2.getGroup(msg.to)
               targets = []
               for a in gInfo.members:
                if _name == a.displayName:
                 targets.append(a.mid)
               if targets == []:
                ki2.sendText(msg.to,"No targets")
               else:
                for target in targets:
                 try:
                  del ikut["target"][target]
                  ki2.sendText(msg.to,"Targets Has Deleted Boss ✓")
                  ki2.sendMessageWithMention(msg.to,target)
                  break
                 except:
                  print succes

	elif msg.from_ in goo["target"] and goo["status"] == True and goo["target"][msg.from_] == True:
             text = msg.text
             if text is not None:
              ki3.sendText(msg.to,text)
             else:
              if msg.contentType == 7:
               msg.contentType = 7
               msg.text = None
               msg.contentMetadata = {
                      "STKID": "100",
                      "STKPKGID": "1",
                      "STKVER": "100" }
               ki3.sendMessage(msg)
              elif msg.contentType == 13:
               msg.contentType = 13
               msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
               cl.sendMessage(msg)
	elif "Follow3:" in msg.text:
             if msg.from_ in admsa:
              cmd = msg.text.replace("Follow3:","")
              if cmd == "on":
               if goo["status"] == False:
                goo["status"] = True
                ki3.sendText(msg.to,"We will Follow The Targets Boss ✓")
               else:
                ki3.sendText(msg.to,"Followed already boss")
              elif cmd == "off":
               if goo["status"] == True:
                goo["status"] = False
                ki3.sendText(msg.to,"We Stopped Following the targets Boss ✓")
               else:
                ki3.sendText(msg.to,"We already Stopped Following the targets Boss")
              elif "add" in cmd:
               target0 = msg.text.replace("Follow3:add","")
               target1 = target0.lstrip()
               target2 = target1.replace("@","")
               target3 = target2.rstrip()
               _name = target3
               gInfo = ki3.getGroup(msg.to)
               targets = []
               for a in gInfo.members:
                if _name == a.displayName:
                 targets.append(a.mid)
               if targets == []:
                ki3.sendText(msg.to,"No targets")
               else:
                for target in targets:
                 try:
                  goo["target"][target] = True
                  ki3.sendText(msg.to,"Succes BosQ ✓")
                  ki3.sendMessageWithMention(msg.to,target)
                  break
                 except:
                  break
              elif "del" in cmd:
               target0 = msg.text.replace("Follow3:del","")
               target1 = target0.lstrip()
               target2 = target1.replace("@","")
               target3 = target2.rstrip()
               _name = target3
               gInfo = ki3.getGroup(msg.to)
               targets = []
               for a in gInfo.members:
                if _name == a.displayName:
                 targets.append(a.mid)
               if targets == []:
                ki3.sendText(msg.to,"No targets")
               else:
                for target in targets:
                 try:
                  del goo["target"][target]
                  ki3.sendText(msg.to,"Targets Has Deleted Boss ✓")
                  ki3.sendMessageWithMention(msg.to,target)
                  break
                 except:
                  print succes
#-----------------------------------------------
	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			ki.updateGroup(G)
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"༺%H:%M༻")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def autolike():
     for zx in range(0,20):
        hasil = cl.activity(limit=200)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"")
            ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by \n line.me/ti/p/~.whome_ \nLike\n  Like\n     Like\n       Like\n     Like\n   Like\nLike")     
            ki2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by \n line.me/ti/p/~.whome_ \nLike\n  Like\n     Like\n       Like\n     Like\n   Like\nLike")
            ki3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by \n line.me/ti/p/~.whome_ \nLike\n  Like\n     Like\n       Like\n     Like\n   Like\nLike")
            ki4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1004)
            ki4.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by \n line.me/ti/p/~.whome_ \nLike\n  Like\n     Like\n       Like\n     Like\n   Like\nLike")
            ki5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1004)
            ki5.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by \n line.me/ti/p/~.whome_ \nLike\n  Like\n     Like\n       Like\n     Like\n   Like\nLike")
            print "Like"
          except:
            pass
        else:
            print "Already Liked"
     time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)