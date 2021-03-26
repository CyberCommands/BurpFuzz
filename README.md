# BurpSuite Extentions using Python

If you’ve ever tried hacking a web application, you’ve likely used Burp Suite to perform spidering, proxy browser traffic, and carry out other attacks. Burp Suite also allows you to create your own tooling, called extensions. Using Python, Ruby, or pure Java, you can add panels in the Burp GUI and build automation techniques into Burp Suite. I will take advantage of this feature to write some handy tooling for performing attacks and extended reconnaissance.

**Setting Up**

Burp Suite comes installed by default on Kali Linux. If you’re using a different machine, download [BurpSuite](https://portswigger.net/) and set it up. You’ll require a modern [Java installation](https://adoptopenjdk.net/). Next, install [Jython Stanalone](https://www.jython.org/), a Python 2 implementation written in Java, since that’s what Jython expects.
