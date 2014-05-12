#	This is the default standard profile provided to a user.
#	They are expected to edit it to meet their own needs.

MAIL=/usr/mail/${LOGNAME:?}
if [ -f ~/.bashrc ]; then . ~/.bashrc; fi
