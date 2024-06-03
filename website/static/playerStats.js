function populateStatsTableHeader(statCategories, tooltips) {
  var tableHeaderRow = document.getElementById("statsHeaderRow");

  var index = 0;
  for (const [category, description] of Object.entries(tooltips)) {
    var th = document.createElement("th");
    th.setAttribute("class", "clickable");
    th.setAttribute("onclick", "sortTable(" + (index + 1) + ")");
    
    var headerDiv = document.createElement("div");
    headerDiv.setAttribute("class", "tooltip");
    headerDiv.innerHTML = statCategories[index];

    var tooltipTextSpan = document.createElement("span");
    tooltipTextSpan.setAttribute("class", "tooltiptext");

    var tooltipTitle = document.createElement("p");
    tooltipTitle.setAttribute("class", "tooltiptext-title");
    tooltipTitle.innerHTML = category;

    var tooltipBody = document.createElement("p");
    tooltipBody.setAttribute("class", "tooltiptext-body");
    tooltipBody.innerHTML = description;

    tooltipTextSpan.appendChild(tooltipTitle);
    tooltipTextSpan.appendChild(tooltipBody);
    headerDiv.appendChild(tooltipTextSpan);
    th.appendChild(headerDiv);

    tableHeaderRow.appendChild(th);
    index++;
  }
  var th = tableHeaderRow.getElementsByTagName("TH")[index]; // the last th
  console.log("span: " + th.getElementsByTagName("p")[0].innerHTML);
  span = th.getElementsByTagName("SPAN")[0];
  span.style.left = "-50px";
  span.style.margin = "0 60px 0 0";
}

function createStatsTable(playerStats) {
  var tableBody = document.getElementById("statsTableBody");
  let rowIndex = 0;
  for (const [player, stats] of Object.entries(playerStats)) {
    if(player != "") {
      let row = tableBody.insertRow(rowIndex++);
      for(var i = 0; i < stats.length; i++) {
          var cell = row.insertCell(i);
          if (stats[i] != null && stats[i].toString().indexOf('.') != -1) {
            //string a decimal point
            cell.innerHTML = parseFloat(stats[i]).toFixed(2);
          } else {
            cell.innerHTML = stats[i];
          }
      }
    }
  }
}

/**
 * sorting table by header click 
 * example from: https://www.w3schools.com/howto/howto_js_sort_table.asp
 * @param columnIndex the column index to sort by
 */
function sortTable(columnIndex) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("statsTableBody");
  switching = true;
  // Set the sorting direction to descending:
  dir = "desc";
  /* Make a loop that will continue until
  no switching has been done: */
  while (switching) {
    // Start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /* Loop through all table rows (except the
    first, which contains table headers): */
    for (i = 0; i < (rows.length - 1); i++) {
      // Start by saying there should be no switching:
      shouldSwitch = false;
      /* Get the two elements you want to compare,
      one from current row and one from the next: */
      x = rows[i].getElementsByTagName("TD")[columnIndex];
      y = rows[i + 1].getElementsByTagName("TD")[columnIndex];
      /* Check if the two rows should switch place,
      based on the direction, asc or desc: */
      if (dir == "asc") {
        if (parseFloat(x.innerHTML) > parseFloat(y.innerHTML)) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      } else if (dir == "desc") {
        if (parseFloat(x.innerHTML) < parseFloat(y.innerHTML)) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /* If a switch has been marked, make the switch
      and mark that a switch has been done: */
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      // Each time a switch is done, increase this count by 1:
      switchcount ++;
    } else {
      /* If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again. */
      if (switchcount == 0 && dir == "desc") {
        dir = "asc";
        switching = true;
      }
    }
  }
  updateSortedColumnArrow(columnIndex);
  highlight_column(columnIndex);
}

function updateSortedColumnArrow(columnIndex) {
  var columnHeaders = document.getElementById("statsHeaderRow").getElementsByTagName("TH");
  for (var i = 1; i < columnHeaders.length; i++) {
    header = columnHeaders[i];
    if (i == columnIndex) {
      if (header.classList.contains("arrow-down")) {
        header.classList.remove("arrow-down");
        header.classList.add("arrow-up");
      } else {
        header.classList.remove("arrow-up");
        header.classList.add("arrow-down");
      }
    } else {
      header.classList.remove("arrow-up");
      header.classList.remove("arrow-down");
    }
  }
}

function highlight_column(columnIndex) {

  var table = document.getElementById("statsTable");
  var tdsth = table.querySelectorAll("th, td");

  for (var i = 0; i < tdsth.length; i++) {
    var cell = tdsth[i];
    cell.classList.remove('selected-th');
    cell.classList.remove('selected-td');
  }

  const columns = document.querySelectorAll(`td:nth-child(${columnIndex + 1}), th:nth-child(${columnIndex + 1})`);
  columns.forEach(col => {
    if (col.nodeName == 'TH') {
      col.classList.add('selected-th');
    } else {
      col.classList.add('selected-td');
    }
  });
}