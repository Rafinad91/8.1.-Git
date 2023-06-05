# Домашнее задание к занятию 12.08 «Резервное копирование баз данных» - `Христинин Артем Олегович`

## Задание 1

Финансовая компания решила увеличить надёжность работы баз данных и их резервного копирования.

Необходимо описать, какие варианты резервного копирования подходят в случаях:

1.1. Необходимо восстанавливать данные в полном объёме за предыдущий день.

1.2. Необходимо восстанавливать данные за час до предполагаемой поломки.

1.3.* Возможен ли кейс, когда при поломке базы происходило моментальное переключение на работающую или починенную базу данных.

- Ответ:
1.1 Для восстановления данных в полном объему потребуется воспользоваться полное резервное копирование (Full backup).

1.2 Для восстаовления данных за последний час воспользуемся инкрементным резервным копированием, так как его можно настроить на опредленный период создания новой полной копии.

1.3 Такое возможно при использование репликации базы данных, например используя Drbd.

## Задание 2

2.1. С помощью официальной документации приведите пример команды резервирования данных и восстановления БД (pgdump/pgrestore).

2.1.* Возможно ли автоматизировать этот процесс? Если да, то как?

 - Ответ:

2.1 pg_dump -U postgres -W -F t dvdrental > /var/tmp/backup.tar 
    pg_restore --dbname=dvdrental --create --verbose /var/tmp/backup.tar 

2.2 Процесс можно автоматизировать, например написать скрипт, сделать фал исполняемым, с помощью крона запскать задание. Либо воспользоваться PgAdmin.

Пример скрипта с habr по созданию бэкапа:

- ~/pg_backup.sh

db_name=dbname

db_user=dbuser

db_host=host

backupfolder=~/postgresql/backups 

recipient_email=youremail@example.ru

- Сколько дней хранить файлы

keep_day=30

sqlfile=$backupfolder/database-$(date +%d-%m-%Y_%H-%M-%S).sql

zipfile=$backupfolder/database-$(date +%d-%m-%Y_%H-%M-%S).zip

mkdir -p $backupfolder

if pg_dump -U $db_user -h $db_host $db_name > $sqlfile ; then

   echo 'Sql dump created'

else

   echo 'pg_dump return non-zero code' | mailx -s 'No backup was created!' $recipient_email

   exit

fi

if gzip -c $sqlfile > $zipfile; then

   echo 'The backup was successfully compressed'

else

   echo 'Error compressing backup' | mailx -s 'Backup was not created!' $recipient_email

   exit

fi

rm $sqlfile 

echo $zipfile | mailx -s -a $sqlfile 'Backup was successfully created' $recipient_email
 
find $backupfolder -mtime +$keep_day -delete


## Задание 3

3.1. С помощью официальной документации приведите пример команды инкрементного резервного копирования базы данных MySQL.

3.1.* В каких случаях использование реплики будет давать преимущество по сравнению с обычным резервным копированием?

- Ответ:

3.1 mysqlbackup --defaults-file=/home/dbadmin/my.cnf \
  --incremental=optimistic --incremental-base=history:last_backup \
  --backup-dir=/home/dbadmin/temp_dir \
  --backup-image=incremental_image1.bi \
   backup-to-image

3.2 Использование реплики является преимуществом, если требуется мгновенное переключение, не тратя время на востановление БД.
