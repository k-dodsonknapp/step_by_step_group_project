import './footer.css'

const Footer = () => {
    return (
        <footer>
            <div id='footer-top'>
                {/* <div id='categories-list'>Categories
                    <ul id='footer-left'>
                        <li>Circuits</li>
                        <li>Workshop</li>
                        <li>Craft</li>
                        <li>Cooking</li>
                        <li>Living</li>
                        <li>Outside</li>
                        <li>Teachers</li>
                    </ul>
                </div> */}
                <div id='find-us'>
                    <div id='footer-right'>
                    <div>
                        <h5>Developed by:</h5>
                    </div>
                        <ul>Chris Young
                            <a href='https://github.com/Noslepr'>
                                <li>GitHub</li>
                            </a>
                            <li>LinkedIn</li>
                        </ul>
                        <ul>Kenneth Dodson-Knapp
                            <a href='https://github.com/k-dodsonknapp'>
                                <li>GitHub</li>
                            </a>
                            <a href='https://www.linkedin.com/in/kenneth-dodson-knapp-97029022a/'>
                                <li>LinkedIn</li>
                            </a>
                        </ul>
                        <ul>Anthony Adams
                            <a href='https://github.com/awadams198'>
                                <li>GitHub</li>
                            </a>
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
