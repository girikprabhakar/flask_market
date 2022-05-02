from market import app
import os

if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG')=='1', host='0.0.0.0', port=5000)