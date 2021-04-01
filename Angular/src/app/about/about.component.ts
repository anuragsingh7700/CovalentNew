import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})
export class AboutComponent implements OnInit {
  akash : string = '/assets/img/akash.jpg'
  anurag : string = '/assets/img/anurag.jpeg'
  aman: string = '/assets/img/aman.jpeg'
  akshat : string = '/assets/img/akshat.jpg'
  harsh : string = '/assets/img/harsh.jpg'
  constructor() { }

  ngOnInit(): void {
  }

}
