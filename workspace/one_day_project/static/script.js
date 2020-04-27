var invite = $("invite_set")

var invite_str = `<input type="text"
`

//$(document).ready(function(){
//    var sock = io.connect('http://127.0.0.1:9999');
//    sock.on('connect', function(){
//        var connect_string = 'new_connect';
//        sock.send(connect_string);
//    });
//
//    sock.on('message', function(msg){
//        console.log(type(msg));
//        if(msg.type === 'normal'){
//            $('#messages').append('>> '+msg.message+'<br>');
//        }else{
//            $('#messages').append('<li>' + msg.message + '</li>');
//        }
//        console.log('Received Message : '+msg.type);
//    });
//
//    $('#send_chat').on('click', function(){
//        sock.send($('#text_box').val());
//        $('#text_box').val('');
//    });
//});
//