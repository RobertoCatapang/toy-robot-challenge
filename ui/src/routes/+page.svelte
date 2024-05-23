<script>
    import SVGTriangle from '../components/SVGTriangle.svelte';

    let x;
    let y;
    let facing;
    let moveStatus;
    let robotData;
    let reportData;
    let robotPlaced;
    const apiUrl = 'http://localhost:8000';

    // Use function to place robot
    async function placeRobot() {
        try {
            let data = {x: x, y: y, facing: facing};
            // Call FastAPI backend to place robot
            const response = await fetch(`${apiUrl}/place`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data),
            });

            moveStatus = ''; // Keep moveStatus empty until a successful move is made
            robotPlaced = true; // Set robotPlaced to true to show other actions
            reportData = false; // Set reportData to false to hide report
            robotData = await response.json();
        } catch (error) {
            // Warn user that an error occured
            alert("Something went wrong. Please check API response");
        }
    }

    // Use function for move, left, right and report commands
    async function promptRobot(action) {
        try {
            // Always reset moveStatus and reportData
            moveStatus = ''; 
            reportData = false;
            // Use response from last command to pass to the API
            let data = {
                x: robotData.x,
                y: robotData.y,
                facing: robotData.facing
            };

            // Call FastAPI with the action passed
            const response = await fetch(`${apiUrl}/${action}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data),
            });

            // If action is report, set reportData to true to show report
            if (action == 'report') {
                reportData = true;
                }

            if (!response.ok) {
                throw new Error(`API call failed with status ${response.status}`);
            };

            // Set Move status
            moveStatus = "Move success!";
            robotData = await response.json();
        } catch (error) {
            alert("Invalid move. Robot will fall off the grid!");
        }
    }
</script>


<style>
    /* Set the dimension of the grid and cells */
    .grid-container {
        display: flex;
        flex-wrap: wrap;
        width: 260px;
    }

    .grid-cell {
        width: 50px;
        height: 50px;
        border: 1px solid #ddd;
        text-align: center;
        line-height: 50px;
    }
</style>

<div style="display: flex; justify-content: center; align-items: center;">
    <div>
        <h1 style="text-align: center;">Toy Robot Challenge</h1>

<!-- Generate a grid where 0,0 is at the bottom left -->
        <div class="grid-container">
            {#each [4,3,2,1,0] as row}
            {#each [0,1,2,3,4] as col}
                <div class="grid-cell">
                    {#if robotData}
                        <!-- Use response to set position of robot -->
                        {#if col == robotData.x && row == robotData.y}  
                            <!-- Use SVG component as the robot -->
                            <SVGTriangle style="position: absolute; top: 0; left: 0;"/>
                        {/if}
                    {/if}
                </div>
            {/each}
            {/each}
        </div>

        <br>

        <!-- Use dropdown to select allow only valid inputs  -->
        <!-- Allow only 0 to 4 for x and y coordinates -->
        <label for="select-id">Choose an x and y coordinate:</label>
        <select bind:value={x}>
            {#each [...Array(5).keys()] as number}  <option value="{number}">{number}</option>
            {/each}
        </select>

        <select bind:value={y}>
            {#each [...Array(5).keys()] as number}  <option value="{number}">{number}</option>
            {/each}
        </select>

        <br>

        <!-- Allow only EAST, WEST, NORTH and SOUTH for facing options -->
        <label for="select-id">Choose where the robot will face:</label>
        <select bind:value={facing}>
            <option value="EAST">EAST</option>
            <option value="WEST">WEST</option>
            <option value="NORTH">NORTH</option>
            <option value="SOUTH">SOUTH</option>
        </select>

        <br>
        <br>

        <!-- Use selected inputs to place robot -->
        <button on:click={placeRobot}>Place robot</button>

        <!-- Only show all actions when robot is placed -->
        {#if robotPlaced}
            <button on:click={() => promptRobot('move')}>Move</button>
            <button on:click={() => promptRobot('left')}>Left</button>
            <button on:click={() => promptRobot('right')}>Right</button>
            <button on:click={() => promptRobot('report')}>Report</button>
        {/if}

        <!-- When move is successful show success -->
        {#if moveStatus}
            <h3 style="color: green;">{moveStatus}</h3>
        {/if}


        <!-- Show x,y and facing direction in report -->
        {#if reportData}
            <h3>Robot report</h3>
                <p>X: {robotData.x}</p>
                <p>Y: {robotData.y}</p>
                <p>Facing: {robotData.facing}</p>
            {:else}
                <p></p>
        {/if}
    </div>
</div>
