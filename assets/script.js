var menuButton=document.querySelector('.menu');
var navigation=document.querySelector('.nav');
if(menuButton&&navigation){
  menuButton.addEventListener('click',function(){var open=navigation.classList.toggle('open');menuButton.setAttribute('aria-expanded',String(open))});
  navigation.querySelectorAll('a').forEach(function(link){link.addEventListener('click',function(){navigation.classList.remove('open');menuButton.setAttribute('aria-expanded','false')})});
}
var year=document.querySelector('#year');
if(year){year.textContent=new Date().getFullYear()}
var form=document.querySelector('#enquiry-form');
if(form){form.addEventListener('submit',function(event){event.preventDefault();var data=new FormData(event.currentTarget);var subject=encodeURIComponent('Salon enquiry from '+data.get('name'));var body=encodeURIComponent('Name: '+data.get('name')+'\nPhone: '+data.get('phone')+'\n\nService enquiry:\n'+data.get('message'));window.location.href='mailto:'+document.body.dataset.email+'?subject='+subject+'&body='+body})}
