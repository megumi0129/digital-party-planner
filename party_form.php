<!DOCTYPE html>
<html>
<head>
    <title>Digital Party Planner</title>
</head>
<body>
    <h1>🎉 Plan Your Party 🎉</h1>
    <form action="/cgi-bin/party_planner.py" method="get">
        <p>Select party items:</p>
        <?php
        $items = [
            "Cake", "Balloons", "Music System", "Lights", "Catering Service",
            "DJ", "Photo Booth", "Tables", "Chairs", "Drinks",
            "Party Hats", "Streamers", "Invitation Cards", "Party Games", "Cleaning Service"
        ];
        foreach ($items as $index => $item) {
            echo "<input type='checkbox' name='items' value='$index'> $item<br>";
        }
        ?>
        <br>
        <input type="submit" value="Get Party Code">
    </form>
</body>
</html>
