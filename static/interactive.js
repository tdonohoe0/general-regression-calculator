import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";

export async function build(independentvars) {
    let form_container = d3.select("#form-container");
    
    let form = form_container
        .append("form")
        .attr("action", "/interactive")
        .attr("enctype", "multipart/form-data")
        .attr("method", "POST");

    // Append input fields to the form. "for" in label must match "id" of input
    // independent variable names must be unique.
    independentvars.split(',').forEach(element => {
        form.append("label")
            .attr("for", element)
            .text(element + ": ");

        form.append("input")
            .attr("type", "checkbox")
            .attr("id", element)
            .attr("name", element);
        form.append("br")

    })
    form.append("input")
        .attr("type", "submit")
        .attr("value", "Submit");

    form.on("submit", function(event) {
        
    })
}