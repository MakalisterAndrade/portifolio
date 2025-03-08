"""
 * Projecr Name : Portfolio Website
 * Project repository link : https://github.com/makalisterandrade/portfolio_site
 * File name : wsgi.py
 * Author : Makalister A.
 * Purpose : Debug Runner
"""

from app import app

if __name__ == "__main__":
    app.run(threaded=True, debug=True)
