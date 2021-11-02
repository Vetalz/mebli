"use strict"

// прокрутка при клике
const menuLinks = document.querySelectorAll('.menu__link[data-goto]');
if (menuLinks.length > 0) {
    menuLinks.forEach(menuLink => {
        menuLink.addEventListener("click", onMenuLinkClick);
    });

    function onMenuLinkClick(e) {
        const menuLink = e.target;
        if (menuLink.dataset.goto && document.querySelector(menuLink.dataset.goto)) {
            const gotoBlock = document.querySelector(menuLink.dataset.goto);
            const gotoBlockValue = gotoBlock.getBoundingClientRect().top + pageYOffset - document.querySelector('header').offsetHeight;

            if(iconMenu.classList.contains('_active')) {
                document.body.classList.remove('_lock');
                iconMenu.classList.remove('_active');
                menuBody.classList.remove('_active');
            }

            window.scrollTo({
                top: gotoBlockValue,
                behavior: "smooth"
            });
            e.preventDefault();
        }
    }
}

// меню бургер
const iconMenu = document.querySelector('.menu__icon');
const menuBody = document.querySelector('.menu__body');
if (iconMenu){
    iconMenu.addEventListener("click", function (e) {
        document.body.classList.toggle('_lock');
        iconMenu.classList.toggle('_active');
        menuBody.classList.toggle('_active');
    });
}

// маска телефона
let phoneMask = IMask(
  document.getElementById('phone'), {
    mask: '+{38}(000)000-00-00',
    lazy: false,
    placeholderChar: '_'
  });


// квиз
let answer = {
    kitchen_plan: 'Прямая',
    kitchen_material: 'ДСП',
    kitchen_table: 'Влагостойкая',
    kitchen_fittings: 'Без доводчиков',
    kitchen_size: 'До 3 метров',
    kitchen_phone: ''
}

function next_q(id_button, direction){
    let id_q = Number(id_button.split('_')[3]);
    let prev_q;
    let next_q;
    if(direction === 1){
        prev_q = document.getElementById(`q_${id_q}`)
        next_q = document.getElementById(`q_${id_q + 1}`)
    }
    else{
        prev_q = document.getElementById(`q_${id_q - 1}`)
        next_q = document.getElementById(`q_${id_q}`)
    }

    prev_q.classList.toggle('hidden')
    next_q.classList.toggle('hidden')
}

function check_type(el, question){
    switch (question){
        case 'plan':
            answer['kitchen_plan'] = el.value;
            break;
        case 'material':
            answer['kitchen_material'] = el.value;
            break;
        case 'table':
            answer['kitchen_table'] = el.value;
            break;
        case 'fittings':
            answer['kitchen_fittings'] = el.value;
            break;
        case 'size':
            answer['kitchen_size'] = el.value;
            break;
    }
    console.log(answer);
}

function validate_phone(phone){
    let result = phone.match(/^\+38\(\d{3}\)\d{3}-\d{2}-\d{2}$/);
    if (result){
        return true;
    }
}

function send_request (el){
    let token =  $('input[name="csrfmiddlewaretoken"]').attr('value');
    let el_phone = document.getElementById('phone');
    let el_error = document.getElementById('error');
    let el_success = document.getElementById('success');
    let el_spinner = document.getElementById('spinner');
    let result = validate_phone(el_phone.value)
    if (result){
        answer['kitchen_phone'] = el_phone.value;
        el.classList.toggle('hidden');
        el_error.classList.add('hidden');
        el_spinner.classList.toggle('hidden')
        $.ajax({
            type: "POST",
            headers: {'X-CSRFToken': token},
            url: "/quiz/",
            data: {
                'plan': answer['kitchen_plan'],
                'material': answer['kitchen_material'],
                'table': answer['kitchen_table'],
                'fittings': answer['kitchen_fittings'],
                'size': answer['kitchen_size'],
                'phone': answer['kitchen_phone']
            },
            success: function (response) {
                if(response.status === 'OK'){
                    el_spinner.classList.toggle('hidden')
                    el_success.classList.remove('hidden');
                }
            }
        });
    }
    else{
        el_error.classList.remove('hidden')
    }
}




