import { Routes } from '@angular/router';
import { LoginPacienteComponent } from './paginas/login/login-paciente/login-paciente.component';
import { RecuperarSenhaComponent } from './paginas/login/recuperar-senha/recuperar-senha.component';
import { HomeComponent } from './paginas/clinica/home/home.component';
import { ListaPacienteComponent } from './paginas/clinica/lista-paciente/lista-paciente.component';
import { ClinicaBaseComponent } from './paginas/clinica/clinica-base/clinica-base.component';
import { FichaMedicaComponent } from './paginas/clinica/ficha-medica/ficha-medica.component';

export const routes: Routes = [
  {
    path: '',
    component: LoginPacienteComponent
  },
  {
    path: 'recuperar-senha',
    component: RecuperarSenhaComponent
  },
  {
    path: 'clinica',
    component: ClinicaBaseComponent,
    children: [
      {
        path: '',
        component: HomeComponent
      },
      {
        path: 'lista-pacientes',
        component: ListaPacienteComponent
      },
      {
        path: 'ficha-medica/:id',
        component: FichaMedicaComponent
      }
    ]
  }
];
