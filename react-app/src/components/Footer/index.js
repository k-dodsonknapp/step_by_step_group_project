import './footer.css'

const Footer = () => {
    return (
        <footer>
            <div id='footer-top'>
                <div id='categories-list'>Categories
                    <ul id='footer-left'>
                        <li>Circuits</li>
                        <li>Workshop</li>
                        <li>Craft</li>
                        <li>Cooking</li>
                        <li>Living</li>
                        <li>Outside</li>
                        <li>Teachers</li>
                    </ul>
                </div>
                <div id='find-us'>Find Us
                    <div id='footer-right'>
                        <ul>Chris Young
                            <li>GitHub</li>
                            <li>LinkedIn</li>
                        </ul>
                        <ul>Kenneth Dodson-Knapp
                            <li>GitHub</li>
                            <li>LinkedIn</li>
                        </ul>
                        <ul>Anthony Adams
                            <li>GitHub</li>
                            <li>LinkedIn</li>
                        </ul>
                    </div>
                </div>
            </div>
            <ul id='footer-bottom'>
                <li>Java Script</li>
                <li>React</li>
                <li>Redux</li>
                <li>Flask</li>
                <li>Postgres</li>
                <li>SqlAlchemy</li>
                <li>HTML</li>
                <li>CSS</li>
            </ul>
        </footer>
    )

}

export default Footer
