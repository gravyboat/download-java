download-java
=============

Python 2.4/2.6 script (tested on RHEL) that can be used to download the java RPMs from Oracle's website, then rebuild the repo so the RPM is available.

Usage Example
=============

You can include this as a function, or call it via the command line. It can also be run as a daily cron job that will automatically download the latest release, and rebuild the repository.

 The following arguments are available:

-u: Lets you set the URL of the JRE page you're downloading from.

-U: Lets you set the URL of the JDK page you're downloading from.

-c: Allows a user to set the cookie in the event it changes.

-i: The i586 (32 bit) directory to download the RPM to.

-x: The x86_64 (64 bit) directory to download the RPM to.

-r: Option that allows you to modify the rebuild command in the event you don't just want to update the repo with the default command.
