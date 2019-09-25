# Password Complexity Requirements
1. Minimum length of at least eight (8) characters with at least 3 of the following conditions  (1.1, 1.2, 1.3, and 1.4)
   1.  At least one upper case character (UNICODE or ASCII)
   1. At least one lower case character (UNICODE or ASCII)
   1. At least one number (Base10 digits: 0 through 9)
   1. At least one special character (~!@#$£€%^&*_-+=`|\(){}[]:;"'<>,.?/<space>)
   OR
    If password length is >19, then they can have any combination of the four in section 1  (1.1, 1.2, 1.3, and 1.4)
   AND
1. Must not be based on easily obtainable and/or guessable information (e.g. pwned passwords), and cannot contain any of the below: 
   1. date of birth
   1. account name
   1. first or last name of user
   1. denied passwords (list of commonly used passwords) 
AND
1. Maximum password length should be specified as 127 characters

Regular Expression:
~~~
^(?:(?=.*\d)(?=.*[A-Z])(?=.*[a-z])|(?=.*\d)(?=.*[^A-Za-z0-9])(?=.*[a-z])|(?=.*[^A-Za-z0-9])(?=.*[A-Z])(?=.*[a-z])|(?=.*\d)(?=.*[A-Z])(?=.*[^A-Za-z0-9]))(?!.*(.)\1{2,})[A-Za-z0-9!~<>,;:_=?*+#."&§%°()\|\[\]\-\$\^\@\/]{8,19}$|^([a-z]|[A-Z]|[0-9]|[!~<>,;:_=?*+#."&§%°()\|\[\]\-\$\^\@\/]){20,127}$
~~~