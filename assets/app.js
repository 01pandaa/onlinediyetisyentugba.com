document.documentElement.classList.add('js');
document.querySelectorAll('[data-js-only]').forEach(el=>el.hidden=false);
document.querySelectorAll('[data-bmi-form] fieldset').forEach(el=>el.disabled=false);
const menuButton=document.querySelector('.menu-toggle'),nav=document.querySelector('.nav');
function closeMenu(){nav?.classList.remove('open');menuButton?.setAttribute('aria-expanded','false');}
menuButton?.addEventListener('click',()=>{const open=nav.classList.toggle('open');menuButton.setAttribute('aria-expanded',String(open));});
document.addEventListener('keydown',e=>{if(e.key==='Escape'){closeMenu();}});
nav?.addEventListener('click',e=>{if(e.target.closest('a'))closeMenu();});
document.querySelectorAll('[data-bmi-form]').forEach(form=>{
  form.addEventListener('submit',e=>{
    e.preventDefault();const result=form.querySelector('[data-result]'),err=form.querySelector('[data-error]');
    const data=new FormData(form),r=calculateBMI(data.get('height'),data.get('weight'),data.get('age'),data.get('eligible')==='on');
    err.textContent=r.error||'';result.hidden=Boolean(r.error);if(r.error)return;
    result.querySelector('strong').textContent=r.value.toLocaleString('tr-TR',{minimumFractionDigits:1,maximumFractionDigits:1})+' kg/m²';
    result.querySelector('[data-category]').textContent=r.category;
  });
});
document.querySelectorAll('[data-anatomy]').forEach(section=>{
  const buttons=[...section.querySelectorAll('[data-topic]')];
  function activate(button){
    buttons.forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
    section.querySelectorAll('[data-panel]').forEach(p=>p.hidden=p.dataset.panel!==button.dataset.topic);
    section.querySelectorAll('[data-figure]').forEach(p=>p.hidden=p.dataset.figure!==button.dataset.topic);
  }
  buttons.forEach(b=>b.addEventListener('click',()=>activate(b)));if(buttons.length)activate(buttons[0]);
});
document.querySelectorAll('[data-video]').forEach(button=>button.addEventListener('click',()=>{
  const frame=document.createElement('iframe');frame.src='https://www.youtube-nocookie.com/embed/'+encodeURIComponent(button.dataset.video)+'?autoplay=1';frame.title=button.dataset.title;frame.allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';frame.allowFullscreen=true;frame.referrerPolicy='strict-origin-when-cross-origin';button.replaceWith(frame);
}));
document.querySelector('[data-map-load]')?.addEventListener('click',function(){
  const frame=document.createElement('iframe');frame.src=this.dataset.src;frame.title='Diyetisyen Tuğba Şeker Ağaç, Seyhan Adana konumu';frame.loading='lazy';frame.referrerPolicy='no-referrer-when-downgrade';frame.allowFullscreen=true;this.closest('.map-slot').replaceChildren(frame);
});
const search=document.querySelector('[data-blog-search]'),filters=[...document.querySelectorAll('[data-filter]')];let selected='Tümü';
function normalize(s){return s.toLocaleLowerCase('tr-TR').normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/ı/g,'i');}
function filterPosts(){let total=0;const q=normalize(search?.value||'');document.querySelectorAll('[data-post]').forEach(card=>{const show=(selected==='Tümü'||card.dataset.category===selected)&&normalize(card.dataset.search).includes(q);card.hidden=!show;if(show)total++;});const empty=document.querySelector('[data-empty]');if(empty)empty.hidden=total>0;const count=document.querySelector('[data-count]');if(count)count.textContent=total+' yazı';}
search?.addEventListener('input',filterPosts);filters.forEach(b=>b.addEventListener('click',()=>{selected=b.dataset.filter;filters.forEach(f=>f.setAttribute('aria-pressed',String(f===b)));filterPosts();}));
