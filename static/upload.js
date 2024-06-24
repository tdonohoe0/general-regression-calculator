import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";

// why async? yae or nay?
export async function build() {

    let form_container = d3.select("#form-container");
    
    let form = form_container
        .append("form")
        .attr("action", "/upload")
        .attr("enctype", "multipart/form-data")
        .attr("method", "POST");

    // Append input fields to the form. "for" in label must match "id" of input
    form.append("label")
        .attr("for", "independent-variables")
        .text("Independent variable column names: ");

    form.append("input")
        .attr("type", "text")
        .attr("id", "independent-variables")
        .attr("name", "independent-variables");

    form.append("br");
    
    form.append("label")
        .attr("for", "dependent-variable")
        .text("Dependent variable column name: ");

    form.append("input")
        .attr("type", "text")
        .attr("id", "dependent-variable")
        .attr("name", "dependent-variable");

    form.append("br");

    form.append("label")
        .attr("for", "file")
        .text("Upload csv file with data: ");

    form.append('input')
        .attr('type', 'file')
        .attr('id', 'file')
        .attr('name', 'file')
        .attr('accept', '.csv');

    form.append("br")

    form.append("input")
        .attr("type", "submit")
        .attr("value", "Upload");
    

    form.on("submit", function(event) {
        console.log("in here");
    })

}