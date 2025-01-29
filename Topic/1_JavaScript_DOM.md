### Common DOM Properties and Methods


##### 1.	parentElement
###### Description: Returns the parent element of the specified element.

```
const child = document.getElementById('child');
const parent = child.parentElement;
console.log(parent); // Logs the parent element
```

##### 2.	firstElementChild
###### Description: Returns the first child element of the specified element.

```
const parent = document.getElementById('parent');
const firstChild = parent.firstElementChild;
console.log(firstChild); // Logs the first child element
```

##### 3.	lastElementChild
###### Description: Returns the last child element of the specified element.

```
const parent = document.getElementById('parent');
const lastChild = parent.lastElementChild;
console.log(lastChild); // Logs the last child element
```

##### 4.	appendChild
###### Description: Adds a node to the end of the list of children of a specified parent node.

```
const parent = document.getElementById('parent');
const newChild = document.createElement('div');
parent.appendChild(newChild);
```

##### 5.	insertBefore
###### Description: Inserts a node before a reference node as a child of a specified parent node.

```
const parent = document.getElementById('parent');
const newChild = document.createElement('div');
const referenceNode = parent.firstElementChild;
parent.insertBefore(newChild, referenceNode);
```

##### 6.	insertAdjacentHTML
###### Description: Parses the specified text as HTML and inserts the resulting nodes into the DOM at a specified position.
<h6>
Positions: <br>
-- <code>'beforebegin'</code> : Before the element itself.<br>
-- <code>'afterbegin'</code>: Just inside the element, before its first child.<br>
-- <code>'beforeend'</code>: Just inside the element, after its last child.<br>
-- <code>'afterend'</code>: After the element itself.<br>
</h6>

```
const parent = document.getElementById('parent');
parent.insertAdjacentHTML('beforeend', '<div>New Child</div>');
```




##### 7.	textContent
###### Description: Sets or returns the text content of the specified node and its descendants.
 
```
const element = document.getElementById('element');
console.log(element.textContent); // Logs the text content
element.textContent = 'New Text Content';
```
 
##### 8.	innerHTML
###### Description: Sets or returns the HTML content of an element. 

```
const element = document.getElementById('element');
console.log(element.innerHTML); // Logs the HTML content
element.innerHTML = '<p>New HTML Content</p>';
```
 
##### 9.	querySelector
###### Description: Returns the first element within the document that matches the specified CSS selector.

```
const element = document.querySelector('.myClass');
console.log(element); // Logs the first element with the class 'myClass'
```

##### 10.	querySelectorAll
###### Description: Returns a static NodeList representing a list of elements matching the specified group of CSS selectors.
 
```
const elements = document.querySelectorAll('.myClass');
elements.forEach(element => console.log(element));
```



















##### Example Usage in Context
###### Here’s a complete example that demonstrates some of these methods and properties:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DOM Methods and Properties</title>
</head>
<body>
    <div id="parent">
        <div id="child">Child</div>
    </div>
    <button id="add-button">Add Child</button>

    <script>
        const parent = document.getElementById('parent');
        const child = document.getElementById('child');

        // parentElement
        console.log(child.parentElement); // Logs the parent element

        // firstElementChild
        console.log(parent.firstElementChild); // Logs the first child element

        // lastElementChild
        console.log(parent.lastElementChild); // Logs the last child element

        // appendChild
        document.getElementById('add-button').addEventListener('click', function() {
            const newChild = document.createElement('div');
            newChild.textContent = 'New Child';
            parent.appendChild(newChild);
        });

        // insertAdjacentHTML
        parent.insertAdjacentHTML('beforeend', '<div>Inserted Child</div>');

        // textContent and innerHTML
        console.log(parent.textContent); // Logs the text content
        console.log(parent.innerHTML); // Logs the HTML content

        // querySelector and querySelectorAll
        const firstChild = document.querySelector('#parent div');
        const allDivs = document.querySelectorAll('#parent div');
        console.log(firstChild); // Logs the first div inside #parent
        allDivs.forEach(div => console.log(div)); // Logs all divs inside #parent
    </script>
</body>
</html>
```

##### This example showcases how to use various DOM methods and properties. Let me know if you have any specific questions or need further explanation! 😊










1. Understanding the Basics of the DOM
<h6>
The DOM represents the structure of your HTML document as a tree of objects that can be accessed and modified using JavaScript. Key methods and properties for form customization include:<br>

-- <code> document.getElementById()</code>: Selects an element by its ID.<br>
-- <code>document.querySelector()</code>: Selects the first matching element.<br>
-- <code>document.createElement()</code>: Creates a new HTML element.<br>
-- <code>element.appendChild()</code>: Adds a new child element.<br>
-- <code>element.innerHTML</code> or <code>element.textContent</code>: Updates content.<br>
-- <code>element.style</code>: Applies inline styles to elements.<br>

</h6>










