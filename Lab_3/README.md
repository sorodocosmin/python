## Requirements
<ol>
<li>
<p>Write a function that receives as parameters two lists a and b and returns a list of sets containing: (<code class="hljs">a</code> intersected with <code class="hljs">b</code>, <code class="hljs">a</code> reunited with <code class="hljs">b</code>, <code class="hljs">a - b</code>, <code class="hljs">b - a</code>)</p>
</li>
<li>
<p>Write a function that receives a string as a parameter and returns a dictionary in which the keys are the characters in the character string and the values are the number of occurrences of that character in the given text.
<strong>Example</strong>: For string <code class="hljs">"Ana has apples."</code> given as a parameter the function will return the dictionary: </p>
</li>
</ol>
<pre><div class="buttons"><button class="fa fa-copy clip-button" title="Copy to clipboard" aria-label="Copy to clipboard"><i class="tooltiptext"></i></button></div><code class="language-python hljs">{<span class="hljs-string">'a'</span>: <span class="hljs-number">3</span>, <span class="hljs-string">'s'</span>: <span class="hljs-number">2</span>, <span class="hljs-string">'.'</span>: <span class="hljs-number">1</span>, <span class="hljs-string">'e'</span>: <span class="hljs-number">1</span>, <span class="hljs-string">'h'</span>: <span class="hljs-number">1</span>, <span class="hljs-string">'l'</span>: <span class="hljs-number">1</span>, <span class="hljs-string">'p'</span>: <span class="hljs-number">2</span>, <span class="hljs-string">' '</span>: <span class="hljs-number">2</span>, <span class="hljs-string">'A'</span>: <span class="hljs-number">1</span>, <span class="hljs-string">'n'</span>: <span class="hljs-number">1</span>} .
</code></pre>
<ol start="3">
<li>
<p>Compare two dictionaries without using the operator "==" returning True or False. (Attention, dictionaries must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)</p>
</li>
<li>
<p>The build_xml_element function receives the following parameters: tag, content, and key-value elements given as name-parameters. Build and return a string that represents the corresponding XML element.
<strong>Example</strong>: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") returns  the string = "&lt;a href="http://python.org \ "_class = " my-link \ "id = " someid \ "&gt; Hello there "</p>
</li>
<li>
<p>The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules for a dictionary that has strings as keys and values) and a dictionary. A rule is defined as follows: (key, "prefix", "middle", "suffix"). A value is considered valid if it starts with "prefix", "middle" is inside the value (not at the beginning or end) and ends with "suffix". The function will return True if the given dictionary matches all the rules, False otherwise.
<strong>Example</strong>: the rules  s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}  and d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} =&gt; False because although the rules are respected for "key1" and "key2" "key3" that does not appear in the rules.</p>
</li>
<li>
<p>Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of unique elements in the list, and b representing the number of duplicate elements in the list (use sets to achieve this objective).</p>
</li>
<li>
<p>Write a function that receives a variable number of sets and returns a dictionary with the following operations from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b", where a and b are two sets, and op is the applied operator: |, &amp;, -. 
Ex:</p>
</li>
</ol>
<pre><div class="buttons"><button class="fa fa-copy clip-button" title="Copy to clipboard" aria-label="Copy to clipboard"><i class="tooltiptext"></i></button></div><code class="language-python hljs">{<span class="hljs-number">1</span>,<span class="hljs-number">2</span>}, {<span class="hljs-number">2</span>, <span class="hljs-number">3</span>} =&gt;
{
    <span class="hljs-string">"{1, 2} | {2, 3}"</span>:  {<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>},
    <span class="hljs-string">"{1, 2} &amp; {2, 3}"</span>:  { <span class="hljs-number">2</span> },
    <span class="hljs-string">"{1, 2} - {2, 3}"</span>:  { <span class="hljs-number">1</span> },
    ...
}
</code></pre>
<ol start="10">
<li>Write a function that receives a single dict parameter named mapping. This dictionary always contains a string key "start". Starting with the value of this key you must obtain a list of objects by iterating over mapping in the following way: the value of the current key is the key for the next value, until you find a loop (a key that was visited before). The function must return the list of objects obtained as previously described.
Ex: </li>
</ol>
<pre><div class="buttons"><button class="fa fa-copy clip-button" title="Copy to clipboard" aria-label="Copy to clipboard"><i class="tooltiptext"></i></button></div><code class="language-python hljs">loop({<span class="hljs-string">'start'</span>: <span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>: <span class="hljs-string">'a'</span>, <span class="hljs-string">'a'</span>: <span class="hljs-string">'6'</span>, <span class="hljs-string">'6'</span>: <span class="hljs-string">'z'</span>, <span class="hljs-string">'x'</span>: <span class="hljs-string">'2'</span>, <span class="hljs-string">'z'</span>: <span class="hljs-string">'2'</span>, <span class="hljs-string">'2'</span>: <span class="hljs-string">'2'</span>, <span class="hljs-string">'y'</span>: <span class="hljs-string">'start'</span>}) will <span class="hljs-keyword">return</span> [<span class="hljs-string">'a'</span>, <span class="hljs-string">'6'</span>, <span class="hljs-string">'z'</span>, <span class="hljs-string">'2'</span>]
</code></pre>
<ol start="11">
<li>Write a function that receives a variable number of positional arguments and a variable number of keyword arguments adn will return the number of positional arguments whose values can be found among keyword arguments values.
Ex: </li>
</ol>
<pre><div class="buttons"><button class="fa fa-copy clip-button" title="Copy to clipboard" aria-label="Copy to clipboard"><i class="tooltiptext"></i></button></div><code class="language-python hljs">my_function(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, x=<span class="hljs-number">1</span>, y=<span class="hljs-number">2</span>, z=<span class="hljs-number">3</span>, w=<span class="hljs-number">5</span>) will <span class="hljs-keyword">return</span> returna <span class="hljs-number">3</span>
</code></pre>
