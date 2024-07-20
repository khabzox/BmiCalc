async function calculateBMI() {
  const weight = document.getElementById("weight").value;
  const height = document.getElementById("height").value;
  if (!weight || !height) {
    alert("يرجى إدخال الوزن والطول");
    return;
  }

  try {
    console.log(
      `Sending request to API with weight=${weight} and height=${height}`
    );
    const response = await fetch(
      `http://http://127.0.0.1:5500/calculate_bmi?weight=${encodeURIComponent(
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
    ).innerHTML = `<strong>مؤشر كتلة الجسم:</strong> ${data.bmi.toFixed(
      2
    )}<br><strong>النتيجة:</strong> ${data.message}`;
  } catch (error) {
    console.error("There was a problem with the fetch operation:", error);
    document.getElementById("result").innerHTML =
      "حدث خطأ أثناء الاتصال بالخادم";
  }
}
