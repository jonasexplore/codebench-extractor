# -*- coding: utf-8 -*-
### Codebench Dataset Extractor by Marcos Lima (marcos.lima@icomp.ufam.edu.br)
### Universidade Federal do Amazonas - UFAM
### Instituto de Computação - IComp

import os

import pandas as pd

from model import *
from util import Logger


class CSVParser:
    """Class Responsável por manipular os arquivos de saída '.csv'"""

    # diretório dos arquivos de saída '.csv' (datasets)
    __output_dir = os.path.join(os.getcwd(), 'csv')
    __periodos_csv = 'periodos.csv'
    __turmas_csv = 'turmas.csv'
    __atividades_csv = 'atividades.csv'
    __estudantes_csv = 'estudantes.csv'
    __execucoes_csv = 'execucoes.csv'
    __solucoes_csv = 'solucoes.csv'
    __erros_csv = 'erros.csv'

    @staticmethod
    def create_output_dir():
        """Cria a pasta e os arquivos de saídas '.csv' (datasets)."""
        try:
            # se o diretório de saída existir, apaga seu conteúdo
            if not os.path.exists(CSVParser.__output_dir):
                os.mkdir(CSVParser.__output_dir)
        except OSError:
            Logger.error('Erro ao criar diretório de saída!')

    @staticmethod
    def __write_execucoes_to_csv(entidades, path: str, header: str):
        """
                Salva uma lista de :class:`CsvEntity` num arquivo no formato CSV.

                :param entidades: Lista de Entidades a serem salvas.
                :type entidades: List[CSVEntity]
                :param path: Caminho absoluto do arquivo '.csv' onde as Entidades devam ser salvas.
                :type path: str
                :param mode: Modo de abertura do arquivo.
                :type mode: str
                """
        Logger.info(f'Salvando entidades no arquivo: {path}')

        rows = []

        for entidade in entidades:
            rows.append(entidade.as_row())

        df = pd.DataFrame(rows, columns=header)
        # quoting 2 = NON_NUMERIC (csv.QUOTE_NON_NUMERIC)
        if os.path.isfile(path):
            df.to_csv(path, sep=',', mode='a', header=False, index=False, encoding='utf-8', quoting=2)
        else:
            df.to_csv(path, sep=',', index=False, encoding='utf-8', quoting=2)

    @staticmethod
    def __write_to_csv(entidades, path: str, header: str):
        """
        Salva uma lista de :class:`CsvEntity` num arquivo no formato CSV.

        :param entidades: Lista de Entidades a serem salvas.
        :type entidades: List[CSVEntity]
        :param path: Caminho absoluto do arquivo '.csv' onde as Entidades devam ser salvas.
        :type path: str
        :param mode: Modo de abertura do arquivo.
        :type mode: str
        """
        Logger.info(f'Salvando entidades no arquivo: {path}')

        rows = []

        for entidade in entidades:
            rows.append(entidade.as_row())

        df = pd.DataFrame(rows, columns=header)
        # quoting 2 = NON_NUMERIC (csv.QUOTE_NON_NUMERIC)
        df.to_csv(path, sep=',', index=False, encoding='utf-8', quoting=2)

    @staticmethod
    def salvar_periodos(periodos):
        """
        Salva uma lista de :class:`Periodo` no arquivo '.csv' (dataset).

        :param periodos: Lista de Períodos a serem salvos.
        """
        CSVParser.__write_to_csv(periodos, os.path.join(CSVParser.__output_dir, CSVParser.__periodos_csv),
                                 Periodo.get_csv_header())

    @staticmethod
    def salvar_turmas(turmas):
        """
        Salva uma lista de :class:`Turma` no arquivo '.csv' (dataset).

        :param turmas: Lista de Turmas a serem salvos.
        """
        CSVParser.__write_to_csv(turmas, os.path.join(CSVParser.__output_dir, CSVParser.__turmas_csv),
                                 Turma.get_csv_header())

    @staticmethod
    def salvar_atividades(atividades):
        """
        Salva uma lista de :class:`Atividade` no arquivo '.csv' (dataset).

        :param atividades: Lista de Atividades a serem salvas.
        """
        CSVParser.__write_to_csv(atividades, os.path.join(CSVParser.__output_dir, CSVParser.__atividades_csv),
                                 Atividade.get_csv_header())

    @staticmethod
    def salvar_estudantes(estudantes):
        """
         Salva uma lista de :class:`Estudante` no arquivo '.csv' (dataset).

         :param estudantes: Lista de Estudantes a serem salvos.
         """
        CSVParser.__write_to_csv(estudantes, os.path.join(CSVParser.__output_dir, CSVParser.__estudantes_csv),
                                 Estudante.get_csv_header())

    @staticmethod
    def salvar_execucoes(execucoes):
        """
         Salva uma lista de :class:`Execucao` no arquivo '.csv' (dataset).

         :param execucoes: Lista de Execucões a serem salvas.
        """
        CSVParser.__write_execucoes_to_csv(execucoes, os.path.join(CSVParser.__output_dir, CSVParser.__execucoes_csv),
                                           Execucao.get_csv_header())

    @staticmethod
    def salvar_solucoes(solucoes):
        """
         Salva uma lista de :class:`Solucao` no arquivo '.csv' (dataset).

         :param solucoes: Lista de Solucões a serem salvas.
        """
        CSVParser.__write_to_csv(solucoes, os.path.join(CSVParser.__output_dir, CSVParser.__solucoes_csv),
                                 Solucao.get_csv_header())

    @staticmethod
    def salvar_erros(erros):
        """
         Salva uma lista de :class:`Erro` no arquivo '.csv' (dataset).

         :param erros: Lista de Erros a serem salvos.
        """
        CSVParser.__write_to_csv(erros, os.path.join(CSVParser.__output_dir, CSVParser.__erros_csv),
                                 Erro.get_csv_header())

