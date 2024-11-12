import { Component, model } from '@angular/core';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { CabecalhoClinicaComponent } from "../../../core/componentes/cabecalho-clinica/cabecalho-clinica.component";
import { RodapeComponent } from "../../../core/componentes/rodape/rodape.component";
import { PacienteService } from '../../../core/services/paciente.service';
import { Router } from '@angular/router';
import { Agendamento } from '../../../core/modelos/agendamento';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    MatDatepickerModule,
    CabecalhoClinicaComponent,
    RodapeComponent,
    MatIconModule
],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent {
  agendamentos: Agendamento[] = [
    {
      nomePaciente: 'Amanda Larissa Santos',
      nomeMedico: 'Medico tal',
      horario: '15:30',
      data: '07/08'
    },
    {
      nomePaciente: 'Amanda Larissa Santos',
      nomeMedico: 'Medico tal',
      horario: '15:30',
      data: '07/08'
    },
    {
      nomePaciente: 'Amanda Larissa Santos',
      nomeMedico: 'Medico tal',
      horario: '15:30',
      data: '07/08'
    }
  ]
  notificacoes: Agendamento[] = [
    {
      nomePaciente: 'Amanda Larissa Santos',
      nomeMedico: 'Medico tal',
      horario: '15:30',
      data: '07/08'
    },
    {
      nomePaciente: 'Amanda Larissa Santos',
      nomeMedico: 'Medico tal',
      horario: '15:30',
      data: '07/08'
    },
    {
      nomePaciente: 'Amanda Larissa Santos',
      nomeMedico: 'Medico tal',
      horario: '15:30',
      data: '07/08'
    },
    {
      nomePaciente: 'Amanda Larissa Santos',
      nomeMedico: 'Medico tal',
      horario: '15:30',
      data: '07/08'
    }
  ]
  selected = model<Date>(new Date());

  constructor(
    private pacienteService: PacienteService,
    private readonly router: Router
  ) { }

  recusarNotificacao(idNotificacao: number | undefined) {
    throw new Error('Method not implemented.');
  }

  confirmarNotificacao(idNotificacao: number | undefined) {
    throw new Error('Method not implemented.');
  }
}
