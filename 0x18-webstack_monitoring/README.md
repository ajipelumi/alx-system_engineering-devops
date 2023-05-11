**Monitoring** is important because it allows system administrators to keep track of the health and performance of their systems and applications, detect and troubleshoot issues, and identify areas for optimization and improvement.
Without monitoring, it can be difficult to know if a system is running smoothly or if there are issues that need attention.

The *two* main areas of monitoring are **system monitoring** and **application monitoring**.

**System monitoring** involves tracking the health and performance of the underlying infrastructure, such as servers, network devices, and storage systems.

**Application monitoring** involves tracking the health and performance of the applications running on top of the infrastructure, such as web servers, databases, and other software.


Here are few famous monitoring tools:

### NewRelic
NewRelic requires you to add a piece of JavaScript to your website, this agent will collect information and send it back to the New Relic servers.
It will give you a detailed analysis of how quickly your website loads in a browser, with a detailed analysis at every level of the stack.
If the website is loading too slowly or users are experiencing error (500), there is a feature that allows you to trigger an alert.
NewRelic now does much more than this, I’ll let you discover the rest.

### DataDog
DataDog allows you to measure and monitor everything with graphs.
It gathers performance data from all your application components.
The service has a lot of integrations. You usually just need to properly configure your alert and you are good to go with solid monitoring coverage.

### Uptime Robot
Uptime Robot is a simple service that will check that your website is responding from multiple locations in the world.
This is the bare minimum when you host a website.

### Nagios
Nagios is an open source project started in 1999, it is among the most widely used monitoring tools in the tech industry.
It is, however, seen as outdated. Nagios had trouble adapting to the rise of the Cloud but is slowly trying to catch up.

### WaveFront
Wavefront is a cutting edge monitoring service funded by great software engineers who’ve built monitoring tools for the best tech companies in Silicon Valley.
The idea is to be able to analyze anything that can produce data points.
A query language that looks like SQL allows users to apply mathematical operations to these data points to extract values or detect anomalies from the time series data.
While it takes some time to get used to the tool, it’s the type of monitoring that the best companies are using.
LinkedIn, Facebook and DropBox are using a very similar tool for their monitoring needs.