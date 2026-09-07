/* CDC adult screening categories; no data storage or network requests. */
(function(root){
  function decimal(value){const s=String(value).trim().replace(',','.');return /^\d+(\.\d+)?$/.test(s)?Number(s):NaN;}
  function calculateBMI(height,weight,age,eligible){
    const h=decimal(height),w=decimal(weight),a=decimal(age);
    if(![h,w,a].every(Number.isFinite)||h<100||h>250||w<25||w>350||a<20||a>120||!Number.isInteger(a))return {error:'Lütfen 20–120 arasında tam sayı yaş, 100–250 cm boy ve 25–350 kg kilo girin. Bu aralıkların dışındaki ölçümler bireysel değerlendirme gerektirir.'};
    if(!eligible)return {error:'Bu yetişkin aracının size uygun olduğunu onaylayın. Gebelikte ve 20 yaş altında bu sınıflandırma kullanılmaz.'};
    const value=w/Math.pow(h/100,2);
    const category=value<18.5?'Düşük vücut ağırlığı aralığı':value<25?'Standart referans aralığı':value<30?'Yüksek vücut ağırlığı aralığı':'Obezite sınıflandırması aralığı';
    return {value,category};
  }
  root.calculateBMI=calculateBMI;
  if(typeof module!=='undefined')module.exports={calculateBMI};
})(typeof window!=='undefined'?window:globalThis);
