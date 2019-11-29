$(document).on("click",".page_previous",previous);
$(document).on("click",".next_page",next);
$(document).on("click",".page_choice",choice);


function previous(e){
    e.submit
    e.stopPropagation(); // 같은 영역에 속해있는 중복 클릭 방지 
    e.preventDefault();  // 이벤트 진행 중지 

    var text= $('.request_text').text();

    if( text == '승인목록'){
        var url = 'list/';
    }else{
        var url = 'approval/';
    }
    page= $(this).attr("href").slice(6); //특정 문자열부터 끝까지

    $.ajax({
            type : 'get', // post방식으로 전송
            url : url, // 서버로 보낼 url 주소
            data : {  // 서버로 보낼 데이터들 dict형식
            page:page
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

function next(e){
    e.submit
    e.stopPropagation(); // 같은 영역에 속해있는 중복 클릭 방지 
    e.preventDefault();  // 이벤트 진행 중지 

    var text= $('.request_text').text();

    if( text == '승인목록'){
        var url = 'list/';
    }else{
        var url = 'approval/';
    }
    page= $(this).attr("href").slice(6); //특정 문자열부터 끝까지

    $.ajax(
        {
            type : 'get', // post방식으로 전송
            url : url, // 서버로 보낼 url 주소
            data : {  // 서버로 보낼 데이터들 dict형식
            page:page
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

       

function choice(e){
    e.submit
    e.stopPropagation(); // 같은 영역에 속해있는 중복 클릭 방지 
    e.preventDefault();  // 이벤트 진행 중지 
    var text= $('.request_text').text()
    if( text == '승인목록'){
        var url = 'list/'
    }else{
        var url = 'approval/'
    }

    page = $(this).text()

    $.ajax(
        {
            type : 'get', // post방식으로 전송
            url : url, // 서버로 보낼 url 주소
            data : {  // 서버로 보낼 데이터들 dict형식
            page:page
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