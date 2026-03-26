import { Injectable } from '@angular/core';
import jsonData from './assets/business.json';

@Injectable({
  providedIn: 'root',
})
//ng g service businessData
export class BusinessData {

  getBusinesses() {
    return jsonData;
  }
}
