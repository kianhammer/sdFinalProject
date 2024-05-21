/**
 * Info on reusable headers and footers https://www.freecodecamp.org/news/reusable-html-components-how-to-reuse-a-header-and-footer-on-a-website/
 * This is where I got this framework
 * 
 * has useful info if we also add footer (and want different styles)
 */

class Header extends HTMLElement {
    constructor() {
      super();
    }
  
    connectedCallback() {
      this.innerHTML = `
        <style>
          ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
            overflow: hidden;
            background-color: #333;
          }
          
          li {
            float: left;
          }
          
          li a {
            display: block;
            color: white;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
          }
          
          /* Change the link color to #111 (black) on hover */
          li a:hover {
            background-color: #111;
          }
        </style>
        <header>
          <ul>
            <li><a href="/">CUTRULES</a></li>
            <li><a href="/stats/players">Player Stats</a></li>
            <li><a href="/stats/game">Game Stats</a></li>
            <li><a href="/import/">Import</a></li>
          </ul>
        </header>
      `;
    }
}
  
customElements.define('header-component', Header);