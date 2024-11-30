for password_validate
       here created two files, one is functions other one is main file

in the functions file 
=====================
->imported re module
->declared a function called password_validate and one argument password
->declared a variable passwd_regex and initialize the pattern here.
  pattern is (?=.*[A-Z]) atleast one uppercase A-Z
             (?=.*[a-z]) atleast one lowercase a-z
             (?=.*\d) atleast one number 0-9
             (?=.*[@#$])atleast one these symbols @#$
         and (.{6,12}) 6,12 is for min 6 chars and max 12 chars
->if condition for search pattern with password
->if match it returs valid password
->else it returns not valid

in the main function
====================
import the password_validate function from password_validate_fun
in the main function initialize the input_passwords with commaseparted
split the password using comma
do the forloop for ip_split list
and calling password_validate(with passwrod argument)
