

![image](https://user-images.githubusercontent.com/101452094/188689555-bba887dd-edce-42d3-b19e-196c870a253f.png)


MySQL is an open-source database management system, commonly installed as part of the popular LAMP (Linux, Apache, MySQL, PHP/Python/Perl) stack. It implements the relational model and uses Structured Query Language (better known as SQL) to manage its data.


Basic SQL statements: DDL and DML

SQL statements are divided into two major categories: data definition language (DDL) and data manipulation language (DML).


Data definition language

DDL statements are used to build and modify the structure of your tables and other objects in the database. When you execute a DDL statement, it takes effect immediately.

The create table statement does exactly that:

        CREATE TABLE <table name> ( 
        <attribute name 1> <data type 1>,
        ...
        <attribute name n> <data type n>);

The data types that you will use most frequently are character strings, which might be called VARCHAR or CHAR for variable or fixed length strings; numeric types such as NUMBER or INTEGER, which will usually specify a precision; and DATE or related types. 


Data manipulation language

DML statements are used to work with the data in tables. When you are connected to most multi-user databases (whether in a client program or by a connection from a Web page script),

The insert statement is used, obviously, to add new rows to a table.

        INSERT INTO <table name>
        VALUES (<value 1>, ... <value n>);
