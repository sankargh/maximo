from psdi.server import MXServer
from psdi.mbo import SqlFormat

#Declare the variable of SendEmail method
sendFrom='';sendTo='';cc='';bcc='';subject='';replyTo='';message='';
fileNames=[]; urlNames=[]

#Get the Email Details from Communication Template
mxServer=MXServer.getMXServer()
userInfo=mbo.getUserInfo()
commTmpSet=mxServer.getMboSet("COMMTEMPLATE",userInfo)
commTmpSet.setWhere("templateid='WO_APPR_EMAIL' and status='ACTIVE'")
if not commTmpSet.isEmpty():
    commTmp=commTmpSet.moveFirst()
    sendFrom=commTmp.getString("SENDFROM")
    sendTo=commTmp.convertSendTo("COMMTMPLT_TO",mbo)
    cc=commTmp.convertSendTo("COMMTMPLT_CC",mbo)
    bcc=commTmp.convertSendTo("COMMTMPLT_BCC",mbo)

    subject=commTmp.getString("SUBJECT")
    sqf=SqlFormat(mbo,subject)
    subject=sqf.resolveContent()

    replyTo=commTmp.getString("REPLYTO")
    sqf=SqlFormat(mbo,replyTo)
    replyTo=sqf.resolveContent()
    
    message=commTmp.getString("MESSAGE")
    sqf=SqlFormat(mbo,message)
    message=sqf.resolveContent()

#Get the Doclink, Docinfo of current Mbo
doclinkSet=mbo.getMboSet("TYPE_A_DOCS")
docCnt=doclinkSet.count()
for i in range (0,docCnt):
    doclink=doclinkSet.getMbo(i)
    docinfoSet=doclink.getMboSet("DOCINFO")
    docinfo=docinfoSet.moveFirst()
    if docinfo.getString("URLTYPE")=='FILE':
        urlName=docinfo.getString("URLNAME")
        fileNames.append(urlName)

#Send Email using the above content
MXServer.sendEMail(sendTo, cc, bcc, sendFrom, subject, message, replyTo, fileNames, urlNames)