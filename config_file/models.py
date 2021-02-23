from django.db import models
from multiselectfield import MultiSelectField


class Company(models.Model):
    name = models.CharField('Empresa', max_length=155)
    time_stamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.name


class File(models.Model):
    list_days_of_week = (
        ('monday', 'Seg'),
        ('tuesday', 'Ter'),
        ('wednesday', 'Qua'),
        ('thursday', 'Qui'),
        ('friday', 'Sex'),
        ('saturday', 'Sab'),
        ('sunday', 'Dom')
    )

    models_date = (
        ('%d-%m-%Y', 'DD-MM-YYYY'),
        ('%d-%m-%y', 'DD-MM-YY'),
        ('%Y-%m-%d', 'YYYY-MM-DD'),
        ('%y-%m-%d', 'YY-MM-DD'),
        ('%Y%m%d', 'YYYYMMDD'),
        ('%y%m%d', 'YYMMDD'),
        ('%d%m%Y', 'DDMMYYYY'),
        ('%d%m%y', 'DDMMYY')
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Nome empresa')
    file_model_name = models.CharField('Nome modelo da base', max_length=155, null=False)
    extension = models.CharField('Extensão do arquivo', max_length=10, default='')
    importer_name = models.CharField('Nome do importer', max_length=155, null=False)
    name_exported = models.CharField('Nome de exportação do arquivo', max_length=155, null=False)
    log_error = models.CharField('Nome do log de erro', max_length=155, null=False)
    log_success = models.CharField('Nome do log de sucesso', max_length=155, null=False)
    prerequisite = models.TextField('Pré requisito para processamento', max_length=255, default='Null')
    file_model_date = models.CharField('Modelo de data arquivo', choices=models_date, max_length=30, default=[], null=False)
    project_directory = models.CharField('Diretório da automação', max_length=255)
    days_of_week = MultiSelectField('Escolha os dias da semana para processar', choices=list_days_of_week,
                                    max_choices=7,
                                    max_length=80,
                                    default=[],
                                    null=False)

    time_stamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Configuração do arquivo'
        verbose_name_plural = 'Configuração dos arquivos'

    def __str__(self):
        return self.file_model_name


class Historic(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Empresa')
    file = models.ForeignKey(File, on_delete=models.CASCADE, verbose_name='Arquivo')
    file_name = models.CharField('Nome do arquivo', max_length=155)
    size = models.PositiveIntegerField('Tamanho', default=0)
    entry_date = models.DateTimeField('Data de entrada')
    extension = models.CharField('Extensão', max_length=10)
    status = models.CharField('Status do arquivo', max_length=155)

    def __str__(self):
        return f'{self.company.name} {self.file.file_model_name} {self.file_name}'

    class Meta:
        verbose_name = 'Histórico'
        verbose_name_plural = 'Histórico dos arquivos'
