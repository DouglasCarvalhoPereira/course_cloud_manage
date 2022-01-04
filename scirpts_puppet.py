#Puppet Classes

class ntp {
    package { 'ntp':
            ensure => latest,
    }
    file { '/etc/ntp.conf':
            source => 'puppet://modulos/ntp/ntp.conf'
            replace => true,
    }
    service { 'ntp':
            enable => true,
            ensure => running,
    }
}

#PUPPETS DSL, Todas as varáveis são precedidas por '$'

if $facts['is_virtual'] {
    package { 'smartmontools':
        ensure => purged,
        }
} else {
    package { 'smartmontools':
        ensure => installed,
        }
}

#EXEMPLO
#ONLYIF garante que o arquivo só será movido se ele existir e nada acontecerá caso contrário

exec { 'move example file':
    command => 'mv /home/user/example.txt /home/user/Desktop',
    onlyif  => 'test -e /home/user/example.txt',

}