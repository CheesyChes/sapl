from django.core import management
from django.core.management.base import BaseCommand

from sapl.legacy.migracao import migrar


class Command(BaseCommand):

    help = 'Migração de dados do SAPL 2.5 para o SAPL 3.1'

    def add_arguments(self, parser):
        parser.add_argument(
            '-f',
            action='store_true',
            default=False,
            dest='force',
            help='Não interativa: pula confirmação de exclusão dos dados',
        )

    def handle(self, *args, **options):
        management.call_command('migrate')
        migrar(interativo=not options['force'])
