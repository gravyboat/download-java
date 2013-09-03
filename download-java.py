#!/usr/bin/python

'''
Author: Forrest Alvarez
Date: 2013/08/23

'''

import os
import urllib
from optparse import OptionParser

def update_jre_rpm(jre_web_page_url = "http://www.oracle.com/technetwork/java/javase/downloads/jre7-downloads-1880261.html",
                    java_terms_cookie = "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F",
                    java_i586_directory = "/usr/src/redhat/RPMS/i586/",
                    java_x86_directory = "/usr/src/redhat/RPMS/x86_64/",
                    rebuild_command = "createrepo --update"):

    # Create the directories if they do not exist.
    if not os.path.exists(java_x86_directory):
        os.makedirs(java_x86_directory)
    if not os.path.exists(java_i586_directory):
        os.makedirs(java_i586_directory)

    # Create our list, and parse the download urls so we have just the rpms.
    url_list = []
    f = urllib.urlopen(jre_web_page_url)
    for line in f:
        if 'rpm' in line:
            url_list.append(line.split('=')[1])

    # Download our RPMs to the respective repo directories, then rebuild the repo.
    # consider stripping the {}, then splitting on ',', and put that into a dict.
    # a.split("=")[1].strip().strip("{};").split(",")
    # wget_cmd = "blah %s blah"
    # if ... arg = thing elif arg = other thing
    for download_details in url_list:
        rpm_url = download_details.split('"')[11]
        rpm_name = download_details.split('"')[11].split("/")[-1]
        i586_rpm_path = os.path.join(java_i586_directory, rpm_name)
        x86_rpm_path = os.path.join(java_x86_directory, rpm_name)
        if 'i586' in download_details and not os.path.exists(i586_rpm_path):
            os.system("wget -O %s --no-cookies --no-check-certificate --header '%s' '%s'" % (i586_rpm_path,
                                                                                            java_terms_cookie,
                                                                                            rpm_url))
            os.system(rebuild_command + ' ' + java_i586_directory)
        elif 'x64' in download_details and not os.path.exists(x86_rpm_path):
            os.system("wget -O %s --no-cookies --no-check-certificate --header '%s' '%s'" % (x86_rpm_path,
                                                                                            java_terms_cookie,
                                                                                            rpm_url))
            os.system(rebuild_command + ' ' + java_x86_directory)

def update_jdk_rpm(jdk_web_page_url = "http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html",
                    java_terms_cookie = "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F",
                    java_i586_directory = "/usr/src/redhat/RPMS/i586/",
                    java_x86_directory = "/usr/src/redhat/RPMS/x86_64/",
                    rebuild_command = "createrepo --update"):

    # Create the directories if they do not exist.
    if not os.path.exists(java_x86_directory):
        os.makedirs(java_x86_directory)
    if not os.path.exists(java_i586_directory):
        os.makedirs(java_i586_directory)

    # Create our list, and parse the download urls so we have just the rpms.
    url_list = []
    f = urllib.urlopen(jdk_web_page_url)
    for line in f:
        if 'rpm' in line:
            url_list.append(line.split('=')[1])

    # Download our RPMs to the respective repo directories, then rebuild the repo.
    # consider stripping the {}, then splitting on ',', and put that into a dict.
    # a.split("=")[1].strip().strip("{};").split(",")
    # wget_cmd = "blah %s blah"
    # if ... arg = thing elif arg = other thing
    for download_details in url_list:
        rpm_url = download_details.split('"')[11]
        rpm_name = download_details.split('"')[11].split("/")[-1]
        i586_rpm_path = os.path.join(java_i586_directory, rpm_name)
        x86_rpm_path = os.path.join(java_x86_directory, rpm_name)
        if 'i586.rpm' in download_details and not os.path.exists(i586_rpm_path):
            os.system("wget -O %s --no-cookies --no-check-certificate --header '%s' '%s'" % (i586_rpm_path,
                                                                                            java_terms_cookie,
                                                                                            rpm_url))
            os.system(rebuild_command + ' ' + java_i586_directory)
        elif 'x64.rpm' in download_details and not os.path.exists(x86_rpm_path):
            os.system("wget -O %s --no-cookies --no-check-certificate --header '%s' '%s'" % (x86_rpm_path,
                                                                                            java_terms_cookie,
                                                                                            rpm_url))
            os.system(rebuild_command + ' ' + java_i586_directory)


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-u",
                    "--jre_web_page_url",
                    dest = "jre_web_page_url",
                    default = "http://www.oracle.com/technetwork/java/javase/downloads/jre7-downloads-1880261.html",
                    help = "The url of the java website.")
    parser.add_option("-U",
                    "--jdk_web_page_url",
                    dest = "jdk_web_page_url",
                    default = "http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html",
                    help = "The url of the java website.")
    parser.add_option("-c",
                    "--java_terms_cookie",
                    dest = "java_terms_cookie",
                    default = "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F",
                    help = "The license agreement cookie.")
    parser.add_option("-i",
                    "--java_i586_directory",
                    dest = "java_i586_directory",
                    default = "/usr/src/redhat/RPMS/i586/",
                    help = "The i586 directory (32 bit).")
    parser.add_option("-x",
                    "--java_x86_directory",
                    dest = "java_x86_directory",
                    default = "/usr/src/redhat/RPMS/x86_64/",
                    help = "The x86_64 directory (64 bit).")
    parser.add_option("-r",
                    "--rebuild_command",
                    dest = "rebuild_command",
                    default = "repo-update",
                    help = "The command to rebuild your repository.")
    (options, args) = parser.parse_args()

    update_jre_rpm(options.jre_web_page_url,
                options.java_terms_cookie,
                options.java_i586_directory,
                options.java_x86_directory,
                options.rebuild_command)
    
    update_jdk_rpm(options.jdk_web_page_url,
                options.java_terms_cookie,
                options.java_i586_directory,
                options.java_x86_directory,
                options.rebuild_command)