import { Component } from '@angular/core';
import { BusinessData } from '../business-data';

@Component({
  selector: 'app-businesses',
  providers: [BusinessData],
  imports: [],
  templateUrl: './businesses.html',
  styleUrl: './businesses.css',
})
export class Businesses {
  businesses_list: any = [];

  constructor(private businessData: BusinessData) { }

  ngOnInit (){
    this.businesses_list = this.businessData.getBusinesses();
  }

}
