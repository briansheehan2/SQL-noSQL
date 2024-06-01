<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html><head></head><body>

 

    <h1> ITEC 2701 SQL/NoSQL Database Design</h1>
    <h2> Program developed by Sam Espana - Spring 2024</h2>
    <h3> Customer Stock Portfolio</h3>
    <p>Symbol: AAPL, Company: Apple Inc, Price: $165.00</p>
    <p>Symbol: INTC, Company: Intel Corporation, Price: $34.20</p>
    <p>Symbol: GOOG, Company: Google Inc, Price: $155.72</p>
    <p>Symbol: UNH, Company: United Health Group, Price: $501.13</p>
    <p>Symbol: MMM, Company: 3M, Price: $92.27</p>
	<p>Symbol: PNR, Company: Pentair Plc, Price: $78.53</p>

	<a href="#" onclick= 'downloadCSV({filename: "NYSE2024.csv"});'>Download CSV</a>
	<script type="text/javascript">var StockData = [
	{
	Symbol: "AAPL",
	Company: "Apple Inc.",
	Price: "$165.00"
	}
	];
		function convertArrayOfObjectsToCSV(args) {
			var result, ctr, keys, columnDelimiter, lineDelimiter, data;
			
			data = args.data || null;
			if (data == null || !data.length) {
				return null;
			}
			
			columnDelimiter = args.columnDelimiter || ',';
			lineDelimiter = args.lineDelimiter || '\n';
			
			keys = Object.keys(data[0]);
			
			result = '';
			result +=keys.join(columnDelimiter);
			result +=lineDelimiter;
			
			data.forEach(function(item) {
				ctr = 0;
				keys.forEach(function(key) {
					if (ctr >0) result += columnDelimiter;
					
					result += item[key];
					ctr++;
				});
				result += lineDelimiter;
			});
			
			return resilt;
			
		}
		
		function downloadCSV(args) {
			var data, filename, link;
			
			var csv = convertArrayOfObjectsToCSV({
				data: StockData
			});
			if(csv == null) return;
			
			filename = args.filename || 'export.csv';
			
			if(!csv.match(/^data:text\/csv/i)){
				csv = 'data:text/csv;charset=utf-8,'+csv;
			}
			data = encodeURI(csv);
			
			link = document.createElement('a');
			link.setAttribute('href',data);
			link.setAttribute('download',filename);
			link.click();
		}
		
		document.getElementById("Demo").innerHTML = stockData.Symbol[0];
		
	</script>
			
					



<footer>  <br>Program enhanced by: Brian Sheehan <br> Date: 4/20/2024</footer>
</body></html>
