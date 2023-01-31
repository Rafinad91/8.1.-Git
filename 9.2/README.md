# Домашнее задание к занятию "9.2 «Zabbix. Часть 1»" - `Христинин Артем Олегович`

## Задание 1
![alt text](https://github.com/Rafinad91/8.1.-Git/blob/main/9.2/img/Zabbix.png)
![alt text](https://github.com/Rafinad91/8.1.-Git/blob/main/9.2/img/zabbix1.png)
# wget https://repo.zabbix.com/zabbix/6.0/debian/pool/main/z/zabbix-release/zabbix-release_6.0-4%2Bdebian11_all.deb
# dpkg -i zabbix-release_6.0-4+debian11_all.deb
# apt update
# apt install zabbix-server-pgsql zabbix-frontend-php php7.4-pgsql zabbix-apache-conf zabbix-sql-scripts zabbix-agent
# sudo apt install postgresql
# sudo -u postgres createuser --pwprompt zabbix
# sudo -u postgres createdb -O zabbix zabbix
# zcat /usr/share/zabbix-sql-scripts/postgresql/server.sql.gz | sudo -u zabbix psql zabbix
# Отредактировать файл /etc/zabbix/zabbix_server.conf (DBPassword=password)
# systemctl restart zabbix-server zabbix-agent apache2
# systemctl enable zabbix-server zabbix-agent apache2
## Задание 2
![alt text](https://github.com/Rafinad91/8.1.-Git/blob/main/9.2/img/hosts_agent.png) - агенты подключенные к серверу
![alt text](https://github.com/Rafinad91/8.1.-Git/blob/main/9.2/img/log_agent.png) - лог агента
![alt text](https://github.com/Rafinad91/8.1.-Git/blob/main/9.2/img/latest_data.png) - Latest data
# wget https://repo.zabbix.com/zabbix/6.0/debian/pool/main/z/zabbix-release/zabbix-release_6.0-4%2Bdebian11_all.deb
# dpkg -i zabbix-release_6.0-4+debian11_all.deb
# apt update
# sudo apt install zabbix-agent -y
# sudo systemctl restart zabbix-agent
# sudo systemctl enable zabbix-agent
# sudo nano /etc/zabbix/zabbix_agentd.conf (В разделе Server добвать адрес нашего сервера)
# sudo systemctl restart zabbix-agent


## Задание 3







