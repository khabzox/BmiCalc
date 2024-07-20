async function calculateBMI() {
  const weight = document.getElementById("weight").value;
  const height = document.getElementById("height").value;
  if (!weight || !height) {
    alert("Please enter weight and height");
    return;
  }

  try {
    console.log(
      `Sending request to API with weight=${weight} and height=${height}`
    );
    const response = await fetch(
      `https://bmi-calc-brown.vercel.app/calculate_bmi?weight=${encodeURIComponent(
        weight
      )}&height=${encodeURIComponent(height)}`
    );
    console.log(`Received response: ${response.status} ${response.statusText}`);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await response.json();
    console.log(`Received data: ${JSON.stringify(data)}`);
    document.getElementById(
      "result"
    ).innerHTML = `<strong>BMI:</strong> ${data.bmi.toFixed(
      2
    )}<br><strong>The result:</strong> ${data.message}`;
  } catch (error) {
    console.error("There was a problem with the fetch operation:", error);
    document.getElementById("result").innerHTML =
      "An error occurred while connecting to the server";
  }
}
