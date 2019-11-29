$(document).on("click",".approval_request",approval_request);
$(document).on("click",".approval_request_clear",approval_request_clear);

        function approval_request(e){
        e.submit
        e.stopPropagation(); // 같은 영역에 속해있는 중복 클릭 방지 
        e.preventDefault();  // 이벤트 진행 중지 

        $.ajax({
               type : 'get', // 
               url : 'request/', // 서버로 보낼 url 주소
               data : {  // 서버로 보낼 데이터들 dict형식 
                },
                // 서버에서 리턴받아올 데이터 형식
               dataType : 'html',  

               //서버에서 무사히 html을 리턴하였다면 실행 
               success : function(data, textStatus, jqXHR){ 
                var text= $('.request_text').text()
                $('.post_list').empty();
                if( text == '승인목록'){
                    $('.request_text').text('게시글')
                    $('.approval_list').attr('href', 'list/')
                    $('.post_list').append(data);
                }else{
                    $('.request_text').text('승인목록')
                    $('.approval_list').attr('href', 'approval/')
                    $('.post_list').append(data);
                }
                
               },

               //서버에서 html을 리턴해주지 못했다면 
               error : function(data, textStatus, jqXHR){
               },
               
           });
        }

function approval_request_clear(e){
    e.submit
    e.stopPropagation(); // 같은 영역에 속해있는 중복 클릭 방지 
    e.preventDefault();  // 이벤트 진행 중지 

    var csrf = getCookie("csrftoken");
    username = $('#id_username').val();
    unv_number = $('#id_unv_number').val();
    department = $('#id_department').val();
    user = $(this).attr('name');

    $.ajax({
            type : 'post', // post방식으로 전송
            url : "request/submit/", // 서버로 보낼 url 주소
            data : {  // 서버로 보낼 데이터들 dict형식 
            'csrfmiddlewaretoken': csrf,
            'username':username,
            'unv_number':unv_number,
            'department':department,
            'user':user,
            },
            // 서버에서 리턴받아올 데이터 형식
            dataType : 'html',  

            //서버에서 무사히 html을 리턴하였다면 실행 
            success : function(data, textStatus, jqXHR){ 
             $('.post_list').empty();
             $('.post_list').append(data);
            },

            //서버에서 html을 리턴해주지 못했다면 
            error : function(data, textStatus, jqXHR){
            },
            
        });
    }