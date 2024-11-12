import { Component } from '@angular/core';
import { CabecalhoClinicaComponent } from "../../../core/componentes/cabecalho-clinica/cabecalho-clinica.component";
import { RodapeComponent } from "../../../core/componentes/rodape/rodape.component";
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-clinica-base',
  standalone: true,
  imports: [
    CabecalhoClinicaComponent,
    RodapeComponent,
    RouterOutlet
  ],
  templateUrl: './clinica-base.component.html',
  styleUrl: './clinica-base.component.scss'
})
export class ClinicaBaseComponent {

}
