import { ChangeDetectionStrategy, Component, signal } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DadosPaciente } from '../../../core/modelos/dados-paciente';
import { Consulta } from '../../../core/modelos/consulta';
import { Documentos } from '../../../core/modelos/documentos';
import { MatDividerModule } from '@angular/material/divider';
import { Retorno } from '../../../core/modelos/retorno';
import {MatExpansionModule} from '@angular/material/expansion';

@Component({
  selector: 'app-ficha-medica',
  standalone: true,
  imports: [
    MatDividerModule,
    MatExpansionModule
  ],
  templateUrl: './ficha-medica.component.html',
  styleUrl: './ficha-medica.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class FichaMedicaComponent {
  idPaciente: number
  readonly panelOpenState = signal(false);

  dadosPessoais: DadosPaciente[] = [
    {
      nome: 'Amanda',
      sobrenome: 'Larrisa Santos',
      cpf: '165.798.654-73',
      email: 'mendes@gmail.com',
      telefone: '3878738723',
      cep: '83782173',
      rua: 'projetada 1',
      numero: 13,
      bairro: 'centro'
    }
  ]

  proximaConsulta: Retorno[] = [
    {
      id: 1,
      especialidade: 'médico geral',
      medico: 'Adrielly',
      data: '17/09',
      hora: '12:00',
      documentos: [
        'exames',
        'solicitação de exame'
      ]
    }
  ]

  listaConsultas: Consulta[] = [
    {
      id: 1,
      especialidade: 'médico geral',
      medico: 'Adrielly',
      data: '17/09',
      hora: '12:00',
      documentos: [
        'exames',
        'solicitação de exame'
      ]
    },
  ]

  documentos: Documentos[] = [{
    documentos: [
      'exames',
      'solicitação de exame'
    ],
    data: '17:09'
  },
  {
    documentos: [
      'exames',
      'solicitação de exame',
      'prescrição de medicamento',
      'testes'
    ],
    data: '17:09'
  },
  {
    documentos: [
      'exames',
      'solicitação de exame',
      'prescrição de medicamento',
      'testes'
    ],
    data: '17:09'
  },
  {
    documentos: [
      'exames',
      'solicitação de exame',
      'prescrição de medicamento',
      'testes'
    ],
    data: '17:09'
  },
  {
    documentos: [
      'exames',
      'solicitação de exame',
      'prescrição de medicamento',
      'testes'
    ],
    data: '17:09'
  }, {
    documentos: [
      'exames',
      'solicitação de exame',
      'prescrição de medicamento',
      'testes'
    ],
    data: '17:09'
  }
  ]

  retornos: Retorno[] = [
      {
        id: 2,
        especialidade: 'médico geral',
        medico: 'Vitória',
        data: '15/09',
        hora: '14:00',
        documentos: [
          'exames',
          'solicitação de exame'
        ]
      }
  ]

  constructor(
    private route: ActivatedRoute
  ) {
    this.idPaciente = Number(this.route.snapshot.paramMap.get('id'))
  }
}
