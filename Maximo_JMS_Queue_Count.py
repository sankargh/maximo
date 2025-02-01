from psdi.iface.jms import JMSQueueBrowser
from psdi.iface.jms import MaxQueueCache
from psdi.iface.jms import QueueConfig
from psdi.iface.jms import JMSData

qbrowser = None

#Declare, set the Maximo JMS queue name
queueName = "jms/maximo/int/queues/cqin"

#Set the condition to filter the Messages
selector = "SENDER='ABC'"

#Connect to JMS queue and Retreive Messages to a List
config = MaxQueueCache.getInstance().getQueueConfig(queueName);
connectionFactory = config.getConfactName();
env = config.getEnv()
qbrowser = JMSQueueBrowser(queueName, connectionFactory, selector, env);
qList = qbrowser.getAllMessages();

#Get Message count
qCount=len(qList)

#raise TypeError("Messages Count - "+str(qCount))
print '-- Number of Messages in the Queue : ' +str(qCount)
