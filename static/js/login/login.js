window.onload = function () {
    const submit = document.getElementById('submit');
    const username = document.getElementsByName("username")[0];
    const password = document.getElementsByName("password")[0];
    const csrfToken = document.getElementsByName("csrf_token")[0];

    submit.onclick = function () {

        if (!username.value || !password.value) {
            window.alert('账号或密码不能为空');
        } else {

            const xhr = new XMLHttpRequest();
            xhr.open('post', 'http://127.0.0.1:5000/login');
            xhr.setRequestHeader("X-CSRFToken", csrfToken.value);
            xhr.setRequestHeader(
                "Content-Type",
                "application/json"
            );

            let sendData = {
                'username': username.value,
                'password': password.value
            };

            xhr.send(JSON.stringify(sendData));
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4) {
                    if (xhr.status >= 200 && xhr.status < 300) {
                        if ('REDIRECT' === xhr.getResponseHeader('REDIRECT')) {
                            window.location.href = xhr.getResponseHeader("CONTENTPATH")
                        } else {
                            res = JSON.parse(xhr.response);
                            window.alert(res.msg);
                        }
                    }
                }
            }
        }
    }
}