<a name="readme-top"></a>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#session-token-authentication">Session Token Authentication</a></li>
  </ol>
</details>



<!-- SESSION TOKEN AUTHENTICATION -->
## Session Token Authentication

The session token can be located manually by inspecting the browser.

1. Navigate to `https://chat.openai.com/api/auth/session` in your web browser.

2. Open the browser's developer console by pressing `F12`.

3. In the console, select the `Application` tab and then select `Cookies` from the list on the left.

4. Locate the cookie named `__Secure-next-auth.session-token` and copy the value.

5. Open the file .env in the root directory and paste the copied `session token` value into the appropriate field.

    ```sh
    AI_SESSION_TOKEN=session_token_value
    ```



<p align="right">(<a href="#readme-top">back to top</a>)</p>