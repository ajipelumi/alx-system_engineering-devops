**Configuration Management** (CM) refers to the process of systematically handling changes to a system in a way that it maintains integrity over time.

Automation plays an essential role in server configuration management.
It’s the mechanism used to make the server reach a desirable state, previously defined by provisioning scripts using a tool’s specific language and features.
Automation is, in fact, the heart of configuration management for servers, and that’s why it’s common to also refer to configuration management tools as *Automation Tools* or *IT Automation Tools*.

There are a number of configuration management tools available in the market. Puppet, Ansible, Chef and Salt are popular choices.
Although each tool will have its own characteristics and work in slightly different ways, they are all driven by the same purpose: to make sure the system’s state matches the state described by your provisioning scripts.

In this project, **Puppet** is the automation tool deployed.

Puppet is an open-source configuration management and automation tool used to manage IT infrastructure at scale.
It is designed to help system administrators automate repetitive tasks, deploy applications and manage infrastructure configurations.
Puppet is based on a client-server architecture where a central server distributes configurations to managed nodes, which are then executed by Puppet agents.

Puppet is built using the Ruby programming language and offers a declarative language for defining system configurations called the Puppet language.
This language allows administrators to define the desired state of their systems and Puppet ensures that the systems are in that state.
Puppet also supports modules, which are collections of pre-written code that can be used to configure common applications and services.

Here's an example of a basic Puppet code that installs the Nginx web server on a Linux machine:
```ruby
class nginx {
  package { 'nginx':
    ensure => installed,
  }
  
  service { 'nginx':
    ensure => running,
    enable => true,
  }
  
  file { '/usr/share/nginx/html/index.html':
    ensure  => present,
    content => "<html><body><h1>Welcome to my Website!</h1></body></html>",
    require => Service['nginx'],
  }
}

```

In this example, we've defined a class called Nginx that contains three resources:
1. A `package` resource that installs the nginx package if it's not already installed.
2. A `service` resource that ensures the nginx service is running and enabled.
3. A `file` resource that creates a simple HTML file at `/usr/share/nginx/html/index.html`.

To apply this code, we would save it as a `.pp` file on the Puppet server, and then use the `puppet apply` command to apply it to the target machine. Once applied, Puppet will ensure that the Nginx web server is installed, running, and serving the specified HTML file.
