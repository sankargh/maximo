
from psdi.iface.jms import JMSQueueBrowser
from psdi.iface.jms import MaxQueueCache
from psdi.iface.jms import QueueConfig
from psdi.iface.jms import JMSData

qbrowser = None

#Declare, Set the JMS Queue name in Maximo
queueName = "jms/maximo/int/queues/cqin"

#Get the JMS queue messages
selector = ''
config = MaxQueueCache.getInstance().getQueueConfig(queueName);
connectionFactory = config.getConfactName();
env = config.getEnv()
qbrowser = JMSQueueBrowser(queueName, connectionFactory, selector, env);
qList = qbrowser.getAllMessages();
qCount=len(qList)

#raise TypeError("Messages Count - "+str(qCount))
print '-- Number of Messages in the Queue : ' +str(qCount)
