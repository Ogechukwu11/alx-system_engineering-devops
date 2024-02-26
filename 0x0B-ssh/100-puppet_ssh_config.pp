#!/usr/bin/env bash
# Setting up my client config file

file_line { 'Turn off passwd auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
  match => '^#PasswordAuthentication',
}

file_line { 'Delare identity file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
  match => '^#IdentityFile',
}
