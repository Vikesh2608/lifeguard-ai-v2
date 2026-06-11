document.getElementById("root").innerHTML = `
<div style="
max-width:900px;
margin:auto;
font-family:Arial;
padding:30px;
">

<h1>🛡️ LifeGuard AI</h1>

<h2>Emergency Safety Platform</h2>

<button onclick="testAPI()">
Check Backend Status
</button>

<p id="result"></p>

</div>
`;

async function testAPI() {
  const response = await fetch(
    "YOUR_RENDER_BACKEND_URL/"
  );

  const data = await response.json();

  document.getElementById(
    "result"
  ).innerText = data.message;
}
