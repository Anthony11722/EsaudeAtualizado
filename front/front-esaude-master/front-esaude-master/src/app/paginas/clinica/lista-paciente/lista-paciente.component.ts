import { Component } from '@angular/core';
import { PacienteService } from '../../../core/services/paciente.service';
import { Router } from '@angular/router';
import { CabecalhoClinicaComponent } from "../../../core/componentes/cabecalho-clinica/cabecalho-clinica.component";
import { PacienteResumo } from '../../../core/modelos/paciente-resumo';
import { MatButtonModule } from '@angular/material/button';


@Component({
  selector: 'app-lista-paciente',
  standalone: true,
  imports: [
    CabecalhoClinicaComponent,
    MatButtonModule
  ],
  templateUrl: './lista-paciente.component.html',
  styleUrl: './lista-paciente.component.scss'
})
export class ListaPacienteComponent {
  pacientes: PacienteResumo[] = [
    {
      id: 1,
      nome: 'paciente 1',
      email: 'email@email.com',
      cpf: '123.456.789-10'
    },
    {
      id: 2,
      nome: 'paciente 2',
      email: 'email@email.com',
      cpf: '123.456.789-10'
    },
    {
      id: 3,
      nome: 'paciente 3',
      email: 'email@email.com',
      cpf: '123.456.789-10'
    },
    {
      id: 4,
      nome: 'paciente 4',
      email: 'email@email.com',
      cpf: '123.456.789-10'
    },
    {
      id: 5,
      nome: 'paciente 5',
      email: 'email@email.com',
      cpf: '123.456.789-10'
    },
  ];

  constructor(
    private pacienteService: PacienteService,
    private readonly router: Router
  ) { }

  verFichaMedica(pacienteId: number) {
    this.router.navigateByUrl(`clinica/ficha-medica/${pacienteId}`)
  }
}
