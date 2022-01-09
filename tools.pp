package { 'htop':
	ensure => present,
}

Para configurarções especificas(Por webserver por exemplo) usamos o comando,
'node'.

node webserver.example.com {

	class { 'sudo': }
	class { 'ntp': 
		servers => ['ntp1.example.com','ntp2.example.com']
	}
	class { 'apache': }
}

Usarando a estrutura Puppet para verificar se as conexões 'node' possuem realmente o nome que dizem