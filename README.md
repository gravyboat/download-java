download-java
=============

Python 2.4/2.6 script (test on RHEL) that can be used to download the java RPMs from Oracle's website, then rebuild the repo so the RPM is available.

Usage Example
=============

You can include this as a function, or call it via the command line. It can also be run as a daily cron job that will automatically download the latest release, and rebuild the repository.

 The following arguments are available:

-u: Lets you set the java web page URL you're downloading from.

-c: Allows a user to set the cookie in the event it changes.

-i: The i586 (32 bit) directory to download the RPM to.

-x: The x86_64 (64 bit) directory to download the RPM to.

-r: Option that allows you to modify the rebuild command in the event you don't just want to update the repo with the default command.

   Copyright [2013] [Forrest Alvarez]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
