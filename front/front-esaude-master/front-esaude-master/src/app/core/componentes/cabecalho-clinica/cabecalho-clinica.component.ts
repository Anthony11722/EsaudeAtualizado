import { CommonModule } from '@angular/common';
import { Component, signal, WritableSignal } from '@angular/core';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { NavigationEnd, Router, RouterLink, RouterOutlet } from '@angular/router';
import { filter } from 'rxjs';

@Component({
  selector: 'app-cabecalho-clinica',
  standalone: true,
  imports: [
    MatInputModule,
    MatIconModule,
    RouterOutlet,
    CommonModule,
    RouterLink
  ],
  templateUrl: './cabecalho-clinica.component.html',
  styleUrl: './cabecalho-clinica.component.scss'
})
export class CabecalhoClinicaComponent {
  rotaSelecionada: WritableSignal<string> = signal('')

  constructor(
    private router: Router,
  ) {
    this.rotaSelecionada.set(this.router.url.substring(1))
  }

  ngOnInit(): void {
    this.router.events
      .pipe(
        filter(event => event instanceof NavigationEnd)
      )
      .subscribe((event: NavigationEnd) => {
        this.rotaSelecionada.set(event.urlAfterRedirects.substring(1))
      });
  }

  sair(): void {
    this.router.navigateByUrl("")
  }
}
