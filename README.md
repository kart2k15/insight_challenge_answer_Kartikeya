




<p>On looking closely at the problem, one can observe:
  <ol>
  <li>The sum of the total number of crossing (i.e. Value) can be computed by a groupBy (border, date, measure) query. Now we need to
  convert this "declaritive" query to a "procedural" one. </li>
  <li>Lines 8-24: they read the input & output files as system arguments. Then creates a dictionary with keys as (border, date, measure)
    <li>Lines 26-51: does some addtional computation, to calculate average</li>
   <li>Lines 53-62: Takes the above computation: converts it to array; sorts it inplace, opens report.csv, creates one if doesn't exist, adds a header row and writes the above array to the file.</li>
        
        
        
I created more tests locally by taking random subsets of data available here : https://data.transportation.gov/Research-and-Statistics/Border-Crossing-Entry-Data/keg4-3bc2. Then calculated the result on theses subsets using a SQL query and then compared my results.
        


